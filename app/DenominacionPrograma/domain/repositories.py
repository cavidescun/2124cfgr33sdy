from abc import ABC, abstractmethod

from app.DenominacionPrograma.domain.entities import DenominacionProgramaEntity


class DenominacionProgramaRepository(ABC):
    """Interfaz abstracta del repositorio de DenominacionPrograma."""

    @abstractmethod
    def save(self, programa: DenominacionProgramaEntity) -> DenominacionProgramaEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> DenominacionProgramaEntity:
        pass
