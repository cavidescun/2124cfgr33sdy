from app.MediosEducativos.domain.entities import MediosEducativosEntity
from app.MediosEducativos.domain.repositories import (
    MediosEducativosRepository,
)
from app.shared.CrearDocumento import CrearDocumento
from app.shared.logic.contextoreporte import ContextoReporte


class CrearMediosEducativos:
    def __init__(self, repo: MediosEducativosRepository):
        self.repo = repo

    def ejectutar(self, **data) -> MediosEducativosEntity:
        programa = MediosEducativosEntity(id=None, **data)
        servicio = CrearDocumento()
        etiquetas = data.get("etiquetas_dinamicas", {})
        contexto = ContextoReporte(**etiquetas)
        plantillas = [f"app/shared/data/Nuevo/medios_educativos.docx"]
        num = 8
        llave_maestra = data.get("llave_maestra", {})
        servicio.generar_multiples_en_segundo_plano(contexto, plantillas, llave_maestra.llave_documento, num)
        return self.repo.save(programa)
