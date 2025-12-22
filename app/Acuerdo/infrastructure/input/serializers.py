from rest_framework import serializers
from django.core.validators import validate_email
from datetime import datetime

from app.shared.validators.fields import LlaveMaestraField
from app.Acuerdo.domain.services import ExcelProcessor

class EtiquetasDinamicasSerializer(serializers.Serializer):
    etiquetas_dinamicas = serializers.DictField()
    llave_maestra = LlaveMaestraField()
    archivo_excel = serializers.FileField(
        required = True,
        help_text="Archivo Excel con la malla curricular",
    )

    def validate_archivo_excel(self, value):
        if value is None:
            return value
        
        if not value.name.endswith(('.xls', '.xlsx')):
            raise serializers.ValidationError("El archivo debe tener una extensión .xls o .xlsx")
        
        if value.size > ExcelProcessor.MAX_FILE_SIZE:
            raise serializers.ValidationError("El tamaño del archivo excede el límite de 20MB.")
        
        if not ExcelProcessor.validate_excel_structure(value):
            raise serializers.ValidationError(f"El archivo debe contener la hoja '{ExcelProcessor.REQUIRED_SHEET}'.")
        
        value.seek(0)
        return value

    def validate(self, data):
        etiquetas = data.get("etiquetas_dinamicas", {})
        if "variables" not in etiquetas:
            raise serializers.ValidationError({"etiquetas_dinamicas": "Debe contener la clave variables."})
        
        variables = etiquetas.get("variables", {})
        if not isinstance(variables, dict):
            raise serializers.ValidationError({"variables": "El valor de varibales debe ser un objeto"})
        
        arhivo_excel = data.get("archivo_excel")
        if arhivo_excel:
            try:
                malla_data = ExcelProcessor.proccess_excel(arhivo_excel)
                variables.update(malla_data)
                etiquetas["variables"] = variables
                data["etiquetas_dinamicas"] = etiquetas
            except Exception as e:
                raise serializers.ValidationError({"archivo_excel": str(e)})
        
        errores = {}
        for nombre, valor in variables.items():
            if nombre == "malla_curricular":
                continue
            
            error = self._validar_variable(nombre, valor)
            if error:
                errores[nombre] = error

            if errores:
                raise serializers.ValidationError({"variables": errores})
            
            return data
    
    def _validar_variable(sef, nombre, valor):
        if valor is None or valor == "":
            return "El Campo no puede estar vacio"
        
        # hacer validador para los campos que lo requieran
        return None
    
class AcuerdoQuerySerializer(serializers.Serializer):
    llave_id = serializers.CharField(
        required=True,
        help_text="ID del llave_id que desea obtener"
    )



class AcuerdoUpdateSerializer(serializers.Serializer):
    llave_id = serializers.CharField(required=True)
    etiquetas_dinamicas = serializers.DictField(child=serializers.DictField())

    def validate(self, data):
        container = self.context["container"]
        obtener_uc = container.acuerdo().obtener_acuerdo()
        acuerdo = obtener_uc.ejecutar(llave_id=data["llave_id"])

        if not acuerdo:
            raise serializers.ValidationError({"error": "Programa no encontrado"})

        data["acuerdo"] = acuerdo

        etiquetas_raw = acuerdo.etiquetas_dinamicas

        if "variables" in etiquetas_raw:
  
            actuales = etiquetas_raw["variables"]
        else:
            # Estructura anidada (lo que TIENES actualmente)
            actuales = etiquetas_raw.get("etiquetas_dinamicas", {}).get("variables", {})

        # Nuevos datos enviados por el usuario
        nuevas = data["etiquetas_dinamicas"].get("variables", {})

        # Validar tipos
        if not isinstance(nuevas, dict):
            raise serializers.ValidationError(
                {"error": "El campo 'variables' debe ser un objeto."}
            )

        # Buscar campos no válidos
        campos_invalidos = set(nuevas.keys()) - set(actuales.keys())
        if campos_invalidos:
            raise serializers.ValidationError(
                {
                    "error": [
                        "No se pueden actualizar campos no existentes.",
                        f"Campos inválidos: {list(campos_invalidos)}"
                    ]
                }
            )

        # Guardar validaciones
        data["campos_actualizados"] = list(nuevas.keys())

        # Fusionar los datos
        actuales_actualizados = {**actuales, **nuevas}

        # Mantener la misma estructura del ACTA
        if "variables" in etiquetas_raw:
            # Estructura simple
            data["etiquetas_finales"] = {
                "variables": actuales_actualizados
            }
        else:
            # Estructura anidada
            data["etiquetas_finales"] = {
                "etiquetas_dinamicas": {
                    "variables": actuales_actualizados
                }
            }

        return data