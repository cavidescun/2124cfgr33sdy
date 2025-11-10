from app.Acta.domain.repositories import ActaRepository
from app.Acta.application.mappers import FormularioPosgradoMapper

class ObtenerActa:
    def __init__(self, acta_repo: ActaRepository):
        self.acta_repo = acta_repo

    def ejecutar(self, acta_id: int) -> dict:
        acta = self.acta_repo.find_by_id(acta_id)
        return FormularioPosgradoMapper.from_etiquetas(acta.etiquetas_dinamicas)
