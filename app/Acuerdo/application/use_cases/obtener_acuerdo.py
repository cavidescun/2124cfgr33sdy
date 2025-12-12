from app.Acuerdo.domain.entities import AcuerdoEntity
from app.Acuerdo.domain.repositories import AcuerdoRepository

class ObtenerAcuerdo:
    def __init__(self, acuerdo_repo: AcuerdoRepository):
        self.acuerdo_repo = acuerdo_repo

    def ejecutar(self, llave_id: str) -> AcuerdoEntity:
        acuerdo_entity = self.acuerdo_repo.find_by_llave(llave_id)
        return acuerdo_entity