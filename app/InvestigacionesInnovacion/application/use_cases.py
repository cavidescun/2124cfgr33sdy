from app.InvestigacionesInnovacion.domain.entities import InvestigacionesInnovacionEntity
from app.InvestigacionesInnovacion.domain.repositories import (
    InvestigacionesInnovacionRepository,
)
from app.shared.CrearDocumento import CrearDocumento
from app.shared.utils.construir_contexto import ConstruirContextoDinamico


class CrearInvestigacionesInnovacion:
    def __init__(self, repo: InvestigacionesInnovacionRepository):
        self.repo = repo

    def ejectutar(self, **data) -> InvestigacionesInnovacionEntity:
        programa = InvestigacionesInnovacionEntity(id=None, **data)
        servicio = CrearDocumento()
        etiquetas = data.get("etiquetas_dinamicas", {})
        contexto = ConstruirContextoDinamico.construir_contexto_dinamico(etiquetas)
        plantillas = [f"app/shared/data/Nuevo/investigacion.docx"]
        num = 5
        llave_maestra = data.get("llave_maestra", {})
        servicio.generar_multiples_en_segundo_plano(
            contexto, plantillas, llave_maestra.llave_documento, num
        )
        return self.repo.save(programa)
