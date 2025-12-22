from app.Acta.domain.repositories import ActaRepository
from app.Acuerdo.domain.entities import AcuerdoEntity
from app.Acuerdo.domain.repositories import AcuerdoRepository
from app.Core.domain.repositories.repositories import RegistroCalificadoRepository
from rest_framework.exceptions import NotFound
class CrearAcuerdo:
    def __init__(self, acuerdo_repo: AcuerdoRepository, registro_repo: RegistroCalificadoRepository,acta_repo: ActaRepository):
        self.acuerdo_repo = acuerdo_repo
        self.registro_repo = registro_repo
        self.acta_repo = acta_repo
        pass

    def ejecutar(self, **data) -> AcuerdoEntity:
        creado_por = data.pop("creado_por", None)
        llave_maestra = data.pop("llave_maestra", None)
        acta=self.acta_repo.find_by_llave(llave_maestra) 
        if not acta.aprobado:
            raise NotFound(f"no se ha aprobado la acta de la llave {llave_maestra}")
        self.acuerdo_repo.estatus_flag(llave_maestra)
        acuerdo = AcuerdoEntity(
            id=None,
            estatus=True,
            llave_maestra=llave_maestra,
            etiquetas_dinamicas=data,
            creado_por_id=creado_por.id if creado_por else None,  
        )
        return self.acuerdo_repo.save(acuerdo)