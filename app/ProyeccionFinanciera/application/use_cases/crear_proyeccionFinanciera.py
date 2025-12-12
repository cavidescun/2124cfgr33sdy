import uuid
from app.ProyeccionFinanciera.domain.entities import ProyeccionFinancieraEntity
from app.ProyeccionFinanciera.domain.repositories import ProyeccionFinancieraRepository
from app.Core.domain.entities import RegistroCalificadoEntity
from app.Core.domain.repositories import RegistroCalificadoRepository

class CrearProyeccionFinanciera:
    def __init__(self, proyeccion_repo: ProyeccionFinancieraRepository, registro_repo: RegistroCalificadoRepository):
        self.proyeccion_repo = proyeccion_repo
        self.registro_repo = registro_repo
        pass

    def ejecutar(self, **data) -> ProyeccionFinancieraEntity:
        creado_por = data.pop("creado_por", None)
        llave_maestra = data.pop("llave_maestra", None)
        proyeccion = ProyeccionFinancieraEntity(
            id = None,
            llave_maestra=llave_maestra,
            etiquetas_dinamicas=data,
            creado_por=creado_por.id if creado_por else None,
        )
        return self.proyeccion_repo.save(proyeccion)