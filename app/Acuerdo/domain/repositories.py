from abc import ABC, abstractmethod
from app.Acuerdo.domain.entities import AcuerdoEntity

class AcuerdoRepository(ABC):
    @abstractmethod
    def save(
        self, programa: AcuerdoEntity
    ) -> AcuerdoEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> AcuerdoEntity:
        pass

    @abstractmethod
    def find_by_llave(self, id: int) -> AcuerdoEntity:
        pass