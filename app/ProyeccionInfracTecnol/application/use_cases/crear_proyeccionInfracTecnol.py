import uuid
from app.ProyeccionInfracTecnol.domain.entities import ProyeccionInfracTecnolEntity
from app.ProyeccionInfracTecnol.domain.repositories import ProyeccionInfracTecnolRepository
from app.Core.domain.entities import RegistroCalificadoEntity
from app.Core.domain.repositories import RegistroCalificadoRepository

class CrearProyeccionInfracTecnol:
    def __init__(self, proyeccion_repo: ProyeccionInfracTecnolRepository, registro_repo: RegistroCalificadoRepository):
        self.proyeccion_repo = proyeccion_repo
        self.registro_repo = registro_repo
        pass

    def ejecutar(self, **data) -> ProyeccionInfracTecnolEntity:
        creado_por = data.pop("creado_por", None)
        llave_maestra = data.pop("llave_maestra", None)
        proyeccion = ProyeccionInfracTecnolEntity(
            id = None,
            llave_maestra=llave_maestra,
            etiquetas_dinamicas=data,
            creado_por=creado_por.id if creado_por else None,
        )
        return self.proyeccion_repo.save(proyeccion)