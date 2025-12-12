import os
from datetime import datetime
from typing import Optional, List, Dict
from app.Core.domain.repositories import RegistroCalificadoRepository


class DescargarInforme:
    
    def __init__(self, registro_calificado_repo: RegistroCalificadoRepository, output_path: str = "/app/output"):
        self.registro_calificado_repo = registro_calificado_repo
        self.output_path = output_path

    def _fecha_mod(self, ruta: str) -> str:
        """Convierte timestamp a formato ISO 8601"""
        timestamp = os.path.getmtime(ruta)
        return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%dT%H:%M:%S")

    def _carpeta_existe(self, llave: str) -> bool:
        """Verifica si existe la carpeta para una llave"""
        ruta_carpeta = os.path.join(self.output_path, llave)
        return os.path.exists(ruta_carpeta) and os.path.isdir(ruta_carpeta)

    def _obtener_estado_llave(self, llave: str) -> str:
        """Determina el estado según la existencia de la carpeta"""
        return "success" if self._carpeta_existe(llave) else "proceso"

    def obtener_archivo(self, llave: str, filename: str) -> Optional[str]:
        """
        Retorna la ruta completa del archivo si existe.
        Returns None si no existe.
        """
        # Validar que la llave existe en BD
        if not self.registro_calificado_repo.exists_by_llave(llave):
            raise ValueError(f"La llave '{llave}' no existe en la base de datos")

        ruta_archivo = os.path.join(self.output_path, llave, filename)
        
        if not os.path.exists(ruta_archivo):
            return None
            
        return ruta_archivo

    def listar_archivos(
        self, 
        llave: Optional[str] = None,
        page: int = 1,
        page_size: int = 10,
        base_url: str = ""
    ) -> Dict:
        """
        Lista archivos disponibles. Si se proporciona llave, filtra por esa llave.
        Solo muestra llaves que existen en la base de datos.
        """
        archivos = []

        if not os.path.exists(self.output_path):
            return {
                "count": 0,
                "page": page,
                "page_size": page_size,
                "results": []
            }

        # Si se proporciona llave específica
        if llave:
            # Validar que existe en BD
            if not self.registro_calificado_repo.exists_by_llave(llave):
                raise ValueError(f"La llave '{llave}' no existe en la base de datos")

            archivos = self._listar_archivos_de_llave(llave, base_url)
        
        # Si no se proporciona llave, listar todas las llaves de BD
        else:
            # Obtener todas las llaves registradas en BD
            registros = self.registro_calificado_repo.all()
            
            for registro in registros:
                llave_bd = registro.llave_documento
                archivos.extend(self._listar_archivos_de_llave(llave_bd, base_url))

        # Paginación
        total = len(archivos)
        start = (page - 1) * page_size
        end = start + page_size
        resultados = archivos[start:end]

        return {
            "count": total,
            "page": page,
            "page_size": page_size,
            "results": resultados
        }

    def _listar_archivos_de_llave(self, llave: str, base_url: str) -> List[Dict]:
        """
        Lista archivos de una llave específica.
        Si la carpeta no existe, retorna info básica sin archivos.
        """
        archivos = []
        ruta_carpeta = os.path.join(self.output_path, llave)
        estado = self._obtener_estado_llave(llave)

        # Si la carpeta no existe, solo retornar info de la llave con estado "proceso"
        if not os.path.exists(ruta_carpeta):
            return [{
                "llave_maestra": llave,
                "status": estado,
                "message": "Procesando documentos..."
            }]

        # Si existe la carpeta, listar archivos
        for nombre in os.listdir(ruta_carpeta):
            ruta_archivo = os.path.join(ruta_carpeta, nombre)

            if os.path.isfile(ruta_archivo):
                download_url = f"{base_url}?llave_maestra={llave}&file={nombre}"
                
                archivos.append({
                    "llave_maestra": llave,
                    "filename": nombre,
                    "size": os.path.getsize(ruta_archivo),
                    "modified": self._fecha_mod(ruta_archivo),
                    "status": estado,
                    "download_url": download_url,
                })

        return archivos