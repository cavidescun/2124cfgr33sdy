from abc import ABC, abstractmethod
from app.ProyeccionInfracTecnol.domain.entities import ProyeccionInfracTecnolEntity

class ProyeccionInfracTecnolRepository(ABC):
    @abstractmethod
    def save(
        self, programa: ProyeccionInfracTecnolEntity
    ) -> ProyeccionInfracTecnolEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> ProyeccionInfracTecnolEntity:
        pass

    @abstractmethod
    def find_by_llave(self, id: int) -> ProyeccionInfracTecnolEntity:
        pass