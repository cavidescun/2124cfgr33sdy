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

    @abstractmethod
    def estatus(self, id: int) -> ProyeccionInfracTecnolEntity:
        pass

    @abstractmethod
    def estatus_flag(self, llave_id: str) -> None:
        pass

    @abstractmethod
    def find_by_llave_update(self, llave_id: str) -> ProyeccionInfracTecnolEntity:
        pass

    @abstractmethod
    def update(self, proyeccion_tecnologica: ProyeccionInfracTecnolEntity) -> ProyeccionInfracTecnolEntity:
        """Actualiza una ProyeccionInfracTecnolEntity existente"""
        pass


    