
from app.Acta.domain.repositories import ActaRepository
from app.ProyeccionFinanciera.domain.entities import ProyeccionFinancieraEntity
from app.ProyeccionFinanciera.domain.repositories import ProyeccionFinancieraRepository

from app.Core.domain.repositories.repositories import RegistroCalificadoRepository
from rest_framework.exceptions import NotFound
class CrearProyeccionFinanciera:
    def __init__(self, proyeccion_repo: ProyeccionFinancieraRepository, registro_repo: RegistroCalificadoRepository,acta_repo: ActaRepository):
        self.proyeccion_repo = proyeccion_repo
        self.registro_repo = registro_repo
        self.acta_repo = acta_repo
        pass

    def ejecutar(self, **data) -> ProyeccionFinancieraEntity:
        creado_por = data.pop("creado_por", None)
        llave_maestra = data.pop("llave_maestra", None)
        acta=self.acta_repo.find_by_llave(llave_maestra) 
        if not acta.aprobado:
            raise NotFound(f"no se ha aprobado la Proyeccion Financiera de la llave {llave_maestra}")
        self.proyeccion_repo.estatus_flag(llave_maestra)
        proyeccion = ProyeccionFinancieraEntity(
            id=None,
            estatus=True,
            llave_maestra=llave_maestra,
            etiquetas_dinamicas=data,
            creado_por_id=creado_por.id if creado_por else None,  
        )
        return self.proyeccion_repo.save(proyeccion)