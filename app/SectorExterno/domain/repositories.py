from abc import ABC, abstractmethod

from app.SectorExterno.domain.entities import SectorExternoEntity


class SectorExternoRepository(ABC):
    @abstractmethod
    def save(
        self, programa: SectorExternoEntity
    ) -> SectorExternoEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> SectorExternoEntity:
        pass
