from app.SectorExterno.domain.entities import SectorExternoEntity
from app.SectorExterno.domain.repositories import (
    SectorExternoRepository,
)
from app.shared.CrearDocumento import CrearDocumento
from app.shared.utils.construir_contexto import ConstruirContextoDinamico


class CrearSectorExterno:
    def __init__(self, repo: SectorExternoRepository):
        self.repo = repo

    def ejectutar(self, **data) -> SectorExternoEntity:
        programa = SectorExternoEntity(id=None, **data)
        servicio = CrearDocumento()
        etiquetas = data.get("etiquetas_dinamicas", {})
        contexto = ConstruirContextoDinamico.construir_contexto_dinamico(etiquetas)
        plantillas = [f"app/shared/data/Nuevo/relacion_sector_externo.docx"]
        num = 6
        llave_maestra = data.get("llave_maestra", {})
        servicio.generar_multiples_en_segundo_plano(
            contexto, plantillas, llave_maestra.llave_documento, num
        )
        return self.repo.save(programa)
