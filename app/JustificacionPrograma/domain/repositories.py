from abc import ABC, abstractmethod

from app.JustificacionPrograma.domain.entities import JustificacionProgramaEntity


class JustificacionProgramaRepository(ABC):
    @abstractmethod
    def save(
        self, programa: JustificacionProgramaEntity
    ) -> JustificacionProgramaEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> JustificacionProgramaEntity:
        pass
