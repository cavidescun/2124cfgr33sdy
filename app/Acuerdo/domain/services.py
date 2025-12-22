import pandas as pd
from typing import List, Dict, Any
from rest_framework.exceptions import ValidationError

class ExcelProcessor:

    REQUIRED_SHEET = 'ASIGNATURAS'
    MAX_FILE_SIZE = 20*1024*1024
    ALLOWED_EXTENSIONS = ['.xls', '.xlsx']

    @staticmethod
    def proccess_excel(file) -> Dict[str, Any]:
        try:
            xls = pd.ExcelFile(file)

            if ExcelProcessor.REQUIRED_SHEET not in xls.sheet_names:
                raise ValidationError(f"El archivo debe contener la hoja '{ExcelProcessor.REQUIRED_SHEET}'.")
        
            df = pd.read_excel(file, sheet_name=ExcelProcessor.REQUIRED_SHEET)

            if df.empty:
                raise ValidationError("La hoja 'ASIGNATURAS' está vacía.")
            
            malla_curricular = ExcelProcessor._clean_dataframe(df)
            return {"malla_curricular": malla_curricular}
        
        except ValidationError:
            raise
        except Exception as e:
            raise ValidationError(f"Error al procesar el archivo Excel: {str(e)}")
    
    @staticmethod
    def _clean_dataframe(df: pd.DataFrame) -> List[Dict[str, Any]]:
        df = df.where(pd.notna(df), None)
        records = df.to_dict('records')
        cleaned_records = []
        for record in records:
            cleaned_record = {}
            for key, value in record.items():
                if pd.isna(value):
                    cleaned_record[key] = None
                elif isinstance(value, (pd.Timestamp, pd.DatetimeTZDtype)):
                    cleaned_record[key] = value.isoformat()
                elif hasattr(value, 'item'):
                    cleaned_record[key] = value.item()
                else:
                    cleaned_record[key] = value
            cleaned_records.append(cleaned_record)
        return cleaned_records
    
    @staticmethod
    def validate_excel_structure(file) -> bool:
        try:
            xls = pd.ExcelFile(file)
            file.seek(0)
            return ExcelProcessor.REQUIRED_SHEET in xls.sheet_names
        except Exception:
            return False
    
    @staticmethod
    def get_malla_statistics(malla_curricular: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not malla_curricular:
            return {
                "total_asignaturas": 0,
                "semestres": {}, 
                "total_creditos": 0
                }
        
        semestres = {}
        total_creditos = 0

        for asignatura in malla_curricular:
            semestre = asignatura.get('TR_Semestre', 'Sin Semestre')
            semestres[semestre] = semestres.get(semestre, 0) + 1
            creditos = asignatura.get('TR_CreditosAcademicos', 0)
            if creditos:
                total_creditos += creditos
        return {
            "total_asignaturas": len(malla_curricular),
            "semestres": semestres,
            "total_creditos": total_creditos
        }