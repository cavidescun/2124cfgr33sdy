from app.ActividadesAcademicas.domain.entities import ActividadesAcademicasEntity
from app.ActividadesAcademicas.domain.repositories import (
    ActividadesAcademicasRepository,
)
from app.shared.CrearDocumento import CrearDocumento
from app.shared.utils.construir_contexto import ConstruirContextoDinamico


class CrearActividadesAcademicas:
    def __init__(self, repo: ActividadesAcademicasRepository):
        self.repo = repo

    def ejectutar(self, **data) -> ActividadesAcademicasEntity:
        programa = ActividadesAcademicasEntity(id=None, **data)
        servicio = CrearDocumento()
        etiquetas = data.get("etiquetas_dinamicas", {})
        contexto = ConstruirContextoDinamico.construir_contexto_dinamico(etiquetas)
        plantillas = [f"app/shared/data/Nuevo/actividades_academicas.docx"]
        num = 4
        llave_maestra = data.get("llave_maestra", {})
        servicio.generar_multiples_en_segundo_plano(
            contexto, plantillas, llave_maestra.llave_documento, num
        )
        return self.repo.save(programa)
