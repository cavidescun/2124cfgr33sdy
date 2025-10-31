from app.Profesores.domain.entities import ProfesoresEntity
from app.Profesores.domain.repositories import (
    ProfesoresRepository,
)
from app.shared.CrearDocumento import CrearDocumento
from app.shared.logic.contextoreporte import ContextoReporte


class CrearProfesores:
    def __init__(self, repo: ProfesoresRepository):
        self.repo = repo

    def ejectutar(self, **data) -> ProfesoresEntity:
        programa = ProfesoresEntity(id=None, **data)
        servicio = CrearDocumento()
        etiquetas = data.get("etiquetas_dinamicas", {})
        contexto = ContextoReporte(**etiquetas)
        plantillas = [f"app/shared/data/Nuevo/profesores.docx"]
        num = 7
        llave_maestra = data.get("llave_maestra", {})
        servicio.generar_multiples_en_segundo_plano(
            contexto, plantillas, llave_maestra.llave_documento, num
        )
        return self.repo.save(programa)
