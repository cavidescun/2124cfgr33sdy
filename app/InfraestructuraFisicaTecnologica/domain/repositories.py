from abc import ABC, abstractmethod

from app.InfraestructuraFisicaTecnologica.domain.entities import (
    InfraestructuraFisicaTecnologicaEntity,
)


class InfraestructuraFisicaTecnologicaRepository(ABC):
    """Interfaz abstracta del repositorio de DenominacionPrograma."""

    @abstractmethod
    def save(
        self, programa: InfraestructuraFisicaTecnologicaEntity
    ) -> InfraestructuraFisicaTecnologicaEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> InfraestructuraFisicaTecnologicaEntity:
        pass
