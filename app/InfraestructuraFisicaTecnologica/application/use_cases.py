from app.InfraestructuraFisicaTecnologica.domain.entities import (
    InfraestructuraFisicaTecnologicaEntity,
)
from app.InfraestructuraFisicaTecnologica.domain.repositories import (
    InfraestructuraFisicaTecnologicaRepository,
)
from app.shared.CrearDocumento import CrearDocumento
from app.shared.utils.construir_contexto import ConstruirContextoDinamico


class CrearInfraestructuraFisicaTecnologica:
    def __init__(self, repo: InfraestructuraFisicaTecnologicaRepository):
        self.repo = repo

    def ejecutar(self, **data) -> InfraestructuraFisicaTecnologicaEntity:
        programa = InfraestructuraFisicaTecnologicaEntity(id=None, **data)
        servicio = CrearDocumento()
        etiquetas = data.get("etiquetas_dinamicas", {})
        contexto = ConstruirContextoDinamico.construir_contexto_dinamico(etiquetas)
        plantillas = [f"app/shared/data/Nuevo/infraestructura_física_tecnológica.docx"]
        num = 9
        llave_maestra = data.get("llave_maestra", {})
        servicio.generar_multiples_en_segundo_plano(
            contexto, plantillas, llave_maestra.llave_documento, num
        )
        return self.repo.save(programa)
