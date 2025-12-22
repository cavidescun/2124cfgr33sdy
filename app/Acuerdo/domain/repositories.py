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

    @abstractmethod
    def estatus(self, id: int) -> AcuerdoEntity:
        pass

    @abstractmethod
    def estatus_flag(self, id: int) -> None:
        pass

    @abstractmethod
    def find_by_llave_update(self, llave_id: str) -> AcuerdoEntity:
        pass

    @abstractmethod
    def update(self, proyeccion_tecnologica: AcuerdoEntity) -> AcuerdoEntity:
        """Actualiza una AcuerdoEntity existente"""
        pass


