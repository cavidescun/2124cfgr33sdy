from app.Acta.domain.repositories import ActaRepository
from app.ProyeccionTecnologica.domain.entities import ProyeccionTecnologicaEntity
from app.ProyeccionTecnologica.domain.repositories import ProyeccionTecnologicaRepository
from app.Core.domain.repositories.repositories import RegistroCalificadoRepository
from rest_framework.exceptions import NotFound
class CrearProyeccionTecnologica:
    def __init__(self, proyeccion_repo: ProyeccionTecnologicaRepository, registro_repo: RegistroCalificadoRepository,acta_repo: ActaRepository):
        self.proyeccion_repo = proyeccion_repo
        self.registro_repo = registro_repo
        self.acta_repo = acta_repo
        pass

    def ejecutar(self, **data) -> ProyeccionTecnologicaEntity:
        creado_por = data.pop("creado_por", None)
        llave_maestra = data.pop("llave_maestra", None)
        acta=self.acta_repo.find_by_llave(llave_maestra) 
        if not acta.aprobado:
            raise NotFound(f"no se ha aprobado la acta de la llave {llave_maestra}")
        self.proyeccion_repo.estatus_flag(llave_maestra)
        proyeccion = ProyeccionTecnologicaEntity(
            id=None,
            estatus=True,
            llave_maestra=llave_maestra,
            etiquetas_dinamicas=data,
            creado_por_id=creado_por.id if creado_por else None,  
        )
        return self.proyeccion_repo.save(proyeccion)