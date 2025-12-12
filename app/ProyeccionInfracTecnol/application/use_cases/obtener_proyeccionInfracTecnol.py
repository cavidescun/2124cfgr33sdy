from app.ProyeccionInfracTecnol.domain.entities import ProyeccionInfracTecnolEntity
from app.ProyeccionInfracTecnol.domain.repositories import ProyeccionInfracTecnolRepository

class ObtenerProyeccionInfracTecnol:
    def __init__(self, proyeccion_repo: ProyeccionInfracTecnolRepository):
        self.proyeccion_repo = proyeccion_repo
    def ejecutar(self, llave_id: str) -> ProyeccionInfracTecnolEntity:
        proyeccion_entity = self.proyeccion_repo.find_by_llave(llave_id)
        return proyeccion_entity