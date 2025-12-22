from typing import Optional, List, Dict
from datetime import datetime
import boto3
from botocore.exceptions import ClientError
from app.Core.domain.repositories.repositories import RegistroCalificadoRepository


class DescargarInforme:

    def __init__(
        self,
        registro_calificado_repo: RegistroCalificadoRepository,
        bucket_name: str = "cun-repo-registrocalificado"
    ):
        self.registro_calificado_repo = registro_calificado_repo
        self.bucket = bucket_name
        self.s3 = boto3.client("s3")

    def _fecha_iso(self, last_modified) -> str:
        return last_modified.strftime("%Y-%m-%dT%H:%M:%S")

    def obtener_archivo(self, llave: str, filename: str):
        if not self.registro_calificado_repo.exists_by_llave(llave):
            raise ValueError(f"La llave '{llave}' no existe en la base de datos")

        key = f"{llave}/{filename}"

        obj = self.s3.get_object(
            Bucket=self.bucket,
            Key=key
        )

        return obj["Body"], obj["ContentLength"]

    def listar_archivos(
        self,
        llave: Optional[str] = None,
        page: int = 1,
        page_size: int = 10,
        base_url: str = ""
    ) -> Dict:
        """
        Lista archivos manteniendo el formato original del frontend.
        
        IMPORTANTE: Ahora pagina correctamente a nivel de REGISTROS.
        Cada archivo incluye información de su registro padre.
        """
        
        archivos = []

        if llave:
            # Caso específico: una sola llave
            if not self.registro_calificado_repo.exists_by_llave(llave):
                raise ValueError(f"La llave '{llave}' no existe en la base de datos")

            archivos = self._listar_por_llave(llave, base_url)

        else:
            # Caso general: paginar registros y listar archivos de cada uno
            registros = self.registro_calificado_repo.all(page=page, page_size=page_size)
            
            for registro in registros:
                archivos.extend(
                    self._listar_por_llave(registro.llave_documento, base_url)
                )

        # Obtener conteo total de REGISTROS (no de archivos)
        total_registros = self.registro_calificado_repo.count_all() if not llave else 1

        return {
            "count": total_registros,
            "page": page,
            "page_size": page_size,
            "total_pages": (total_registros + page_size - 1) // page_size if total_registros else 0,
            "results": archivos
        }

    def _listar_por_llave(self, llave: str, base_url: str) -> List[Dict]:
        """Lista archivos de una llave específica en S3."""
        prefix = f"{llave}/"

        try:
            response = self.s3.list_objects_v2(
                Bucket=self.bucket,
                Prefix=prefix
            )

            if "Contents" not in response:
                return [{
                    "llave_maestra": llave,
                    "status": "proceso",
                    "message": "Procesando documentos...",
                    "filename": None,
                    "size": None,
                    "modified": None,
                    "download_url": None
                }]

            archivos = []

            for obj in response["Contents"]:
                if obj["Key"].endswith("/"):
                    continue

                nombre = obj["Key"].split("/")[-1]

                archivos.append({
                    "llave_maestra": llave,
                    "filename": nombre,
                    "size": obj["Size"],
                    "modified": self._fecha_iso(obj["LastModified"]),
                    "status": "success",
                    "download_url": f"{base_url}?llave_maestra={llave}&file={nombre}"
                })

            return archivos or [{
                "llave_maestra": llave,
                "status": "success",
                "message": "Carpeta vacía - sin archivos disponibles",
                "filename": None,
                "size": None,
                "modified": None,
                "download_url": None
            }]

        except ClientError as e:
            return [{
                "llave_maestra": llave,
                "status": "error",
                "message": str(e),
                "filename": None,
                "size": None,
                "modified": None,
                "download_url": None
            }]