from app.PresentacionDocumento.domain.entities import PresentacionDocumentoEntity
from app.PresentacionDocumento.domain.repositories import PresentacionDocumentoRepository
from app.shared.CrearDocumento import CrearDocumento
from app.shared.logic.contextoreporte import ContextoReporte


class PresentacionDocumento:
    def __init__(self, repo: PresentacionDocumentoRepository):
        self.repo = repo

    def ejecutar(self, **data) -> PresentacionDocumentoEntity:
        programa = PresentacionDocumentoEntity(id=None, **data)
        servicio = CrearDocumento()
        etiquetas = data.get("etiquetas_dinamicas", {})
        contexto = ContextoReporte(**etiquetas)
        plantillas = [f"app/shared/data/Nuevo/presentacion_documento.docx"]
        num = 0
        llave_maestra = data.get("llave_maestra", {})
        servicio.generar_multiples_en_segundo_plano(
            contexto, plantillas, llave_maestra.llave_documento, num
        )
        return self.repo.save(programa)
