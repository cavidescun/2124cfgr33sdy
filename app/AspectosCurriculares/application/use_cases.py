from app.AspectosCurriculares.domain.entities import AspectosCurricularesEntity
from app.AspectosCurriculares.domain.repositories import (
    AspectosCurricularesRepository,
)
from app.shared.CrearDocumento import CrearDocumento
from app.shared.logic.contextoreporte import ContextoReporte


class CrearAspectosCurriculares:
    def __init__(self, repo: AspectosCurricularesRepository):
        self.repo = repo

    def ejectutar(self, **data) -> AspectosCurricularesEntity:
        programa = AspectosCurricularesEntity(id=None, **data)
        servicio = CrearDocumento()
        etiquetas = data.get("etiquetas_dinamicas", {})
        contexto = ContextoReporte(**etiquetas)
        plantillas = [f"app/shared/data/Nuevo/aspectos_curriculares.docx"]
        num = 3
        llave_maestra = data.get("llave_maestra", {})
        servicio.generar_multiples_en_segundo_plano(
            contexto, plantillas, llave_maestra.llave_documento, num
        )
        return self.repo.save(programa)
