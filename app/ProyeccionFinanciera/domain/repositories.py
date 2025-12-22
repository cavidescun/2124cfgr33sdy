from abc import ABC, abstractmethod
from app.ProyeccionFinanciera.domain.entities import ProyeccionFinancieraEntity

class ProyeccionFinancieraRepository(ABC):
    @abstractmethod
    def save(
        self, programa: ProyeccionFinancieraEntity
    ) -> ProyeccionFinancieraEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> ProyeccionFinancieraEntity:
        pass

    @abstractmethod
    def find_by_llave(self, id: int) -> ProyeccionFinancieraEntity:
        pass

    @abstractmethod
    def estatus(self, id: int) -> ProyeccionFinancieraEntity:
        pass

    @abstractmethod
    def estatus_flag(self, llave_id: str) -> None:
        pass

    @abstractmethod
    def find_by_llave_update(self, llave_id: str) -> ProyeccionFinancieraEntity:
        pass

    @abstractmethod
    def update(self, proyeccion_tecnologica: ProyeccionFinancieraEntity) -> ProyeccionFinancieraEntity:
        """Actualiza una ProyeccionFinancieraEntity existente"""
        pass

