from app.JustificacionPrograma.domain.entities import JustificacionProgramaEntity
from app.JustificacionPrograma.domain.repositories import (
    JustificacionProgramaRepository,
)
from app.shared.CrearDocumento import CrearDocumento
from app.shared.utils.construir_contexto import ConstruirContextoDinamico


class CrearJustificacionPrograma:
    def __init__(self, repo: JustificacionProgramaRepository):
        self.repo = repo

    def ejectutar(self, **data) -> JustificacionProgramaEntity:
        programa = JustificacionProgramaEntity(id=None, **data)
        servicio = CrearDocumento()
        etiquetas = data.get("etiquetas_dinamicas", {})
        contexto = ConstruirContextoDinamico.construir_contexto_dinamico(etiquetas)
        plantillas = [f"app/shared/data/Nuevo/justificacion_del_programa.docx"]
        num = 2
        llave_maestra = data.get("llave_maestra", {})
        servicio.generar_multiples_en_segundo_plano(
            contexto, plantillas, llave_maestra.llave_documento, num
        )
        return self.repo.save(programa)
