from app.Core.domain.entities import RegistroCalificadoEntity
from app.Core.domain.repositories.repositories import RegistroCalificadoRepository
import uuid

class CrearLlave:
    def __init__(self, registro_calificado_repo: RegistroCalificadoRepository):
        self.registro_calificado_repo = registro_calificado_repo

    def ejecutar(self) -> dict:

        llave_maestra = f"LLAVE-{uuid.uuid4().hex[:8].upper()}"
        registro = RegistroCalificadoEntity(
            id=None,
            llave_documento=llave_maestra,
            tipo="Posgrado",
            snies=llave_maestra,
        )
        registro = self.registro_calificado_repo.save(registro)
        return registro
