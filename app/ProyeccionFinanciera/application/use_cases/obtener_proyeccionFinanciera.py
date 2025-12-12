from app.ProyeccionFinanciera.domain.entities import ProyeccionFinancieraEntity
from app.ProyeccionFinanciera.domain.repositories import ProyeccionFinancieraRepository

class ObtenerProyeccionFinanciera:
    def __init__(self, proyeccion_repo: ProyeccionFinancieraRepository):
        self.proyeccion_repo = proyeccion_repo

    def ejecutar(self, llave_id: str) -> ProyeccionFinancieraEntity:
        proyeccion_entity = self.proyeccion_repo.find_by_llave(llave_id)
        return proyeccion_entity