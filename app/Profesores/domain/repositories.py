from abc import ABC, abstractmethod

from app.Profesores.domain.entities import ProfesoresEntity


class ProfesoresRepository(ABC):
    @abstractmethod
    def save(self, programa: ProfesoresEntity) -> ProfesoresEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> ProfesoresEntity:
        pass
