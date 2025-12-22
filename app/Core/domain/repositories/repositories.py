from abc import ABC, abstractmethod
from typing import Dict
from app.Core.domain.entities import RegistroCalificadoEntity


class RegistroCalificadoRepository(ABC):
    """Interfaz abstracta del repositorio de DenominacionPrograma."""

    @abstractmethod
    def save(self, programa: RegistroCalificadoEntity) -> RegistroCalificadoEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> RegistroCalificadoEntity:
        pass

    @abstractmethod
    def find_by_llave(self, llave: str) -> RegistroCalificadoEntity:
        pass

    @abstractmethod
    def all(self, page: int = None, page_size: int = None):
        pass

    @abstractmethod
    def count_all(self) -> int:
        """Retorna el conteo total de registros."""
        pass

    @abstractmethod
    def exists_by_llave(self, id: int) -> bool:
        pass

    @abstractmethod
    def update_by_llave(llave: str, data: dict) -> RegistroCalificadoEntity:
        pass