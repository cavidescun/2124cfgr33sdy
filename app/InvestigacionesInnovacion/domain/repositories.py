from abc import ABC, abstractmethod

from app.InvestigacionesInnovacion.domain.entities import InvestigacionesInnovacionEntity


class InvestigacionesInnovacionRepository(ABC):
    @abstractmethod
    def save(
        self, programa: InvestigacionesInnovacionEntity
    ) -> InvestigacionesInnovacionEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> InvestigacionesInnovacionEntity:
        pass
