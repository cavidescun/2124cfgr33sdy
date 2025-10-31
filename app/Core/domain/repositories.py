from abc import ABC, abstractmethod

from app.Core.domain.entities import RegistroCalificadoEntity


class RegistroCalificadoRepository(ABC):
    """Interfaz abstracta del repositorio de DenominacionPrograma."""

    @abstractmethod
    def save(self, programa: RegistroCalificadoEntity) -> RegistroCalificadoEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> RegistroCalificadoEntity:
        pass
