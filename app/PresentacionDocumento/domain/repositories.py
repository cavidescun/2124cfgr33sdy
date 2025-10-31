from abc import ABC, abstractmethod

from app.PresentacionDocumento.domain.entities import PresentacionDocumentoEntity


class PresentacionDocumentoRepository(ABC):
    """Interfaz abstracta del repositorio de DenominacionPrograma."""

    @abstractmethod
    def save(self, programa: PresentacionDocumentoEntity) -> PresentacionDocumentoEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> PresentacionDocumentoEntity:
        pass
