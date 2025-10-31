from abc import ABC, abstractmethod

from app.AspectosCurriculares.domain.entities import AspectosCurricularesEntity


class AspectosCurricularesRepository(ABC):
    @abstractmethod
    def save(
        self, programa: AspectosCurricularesEntity
    ) -> AspectosCurricularesEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> AspectosCurricularesEntity:
        pass
