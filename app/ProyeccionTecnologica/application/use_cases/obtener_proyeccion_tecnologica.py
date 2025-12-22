from app.ProyeccionTecnologica.domain.entities import ProyeccionTecnologicaEntity
from app.ProyeccionTecnologica.domain.repositories import ProyeccionTecnologicaRepository

class ObtenerProyeccionTecnologica:
    def __init__(self, proyeccion_repo: ProyeccionTecnologicaRepository):
        self.proyeccion_repo = proyeccion_repo
    def ejecutar(self, llave_id: str) -> ProyeccionTecnologicaEntity:
        proyeccion_entity = self.proyeccion_repo.find_by_llave(llave_id)
        return proyeccion_entity