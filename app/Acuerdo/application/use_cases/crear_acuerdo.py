import uuid
from app.Acuerdo.domain.entities import AcuerdoEntity
from app.Acuerdo.domain.repositories import AcuerdoRepository
from app.Core.domain.entities import RegistroCalificadoEntity
from app.Core.domain.repositories import RegistroCalificadoRepository

class CrearAcuerdo:
    def __init__(self, acuerdo_repo: AcuerdoRepository, registro_repo: RegistroCalificadoRepository):
        self.acuerdo_repo = acuerdo_repo
        self.registro_repo = registro_repo
        pass

    def ejecutar(self, **data) -> AcuerdoEntity:
        creado_por = data.pop("creado_por", None)
        llave_maestra = data.pop("llave_maestra", None)
        acuerdo = AcuerdoEntity(
            id = None,
            llave_maestra=llave_maestra,
            etiquetas_dinamicas=data,
            creado_por=creado_por.id if creado_por else None,
        )
        return self.acuerdo_repo.save(acuerdo)