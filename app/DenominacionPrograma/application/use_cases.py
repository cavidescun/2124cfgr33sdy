from app.DenominacionPrograma.domain.entities import DenominacionProgramaEntity
from app.DenominacionPrograma.domain.repositories import DenominacionProgramaRepository
from app.shared.CrearDocumento import CrearDocumento
from app.shared.logic.contextoreporte import ContextoReporte


class CrearDenominacionPrograma:
    def __init__(self, repo: DenominacionProgramaRepository):
        self.repo = repo

    def ejecutar(self, **data) -> DenominacionProgramaEntity:
        programa = DenominacionProgramaEntity(id=None, **data)
        servicio = CrearDocumento()
        etiquetas = data.get("etiquetas_dinamicas", {})
        contexto = ContextoReporte(**etiquetas)
        plantillas = [f"app/shared/data/Nuevo/denominacion_del_programa.docx"]
        num = 1
        llave_maestra = data.get("llave_maestra", {})
        servicio.generar_multiples_en_segundo_plano(
            contexto, plantillas, llave_maestra.llave_documento, num
        )
        return self.repo.save(programa)
