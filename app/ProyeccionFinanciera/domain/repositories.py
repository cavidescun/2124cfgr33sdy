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