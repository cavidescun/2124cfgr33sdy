from abc import ABC, abstractmethod

from app.Acta.domain.entities import ActaEntity


class ActaRepository(ABC):
    @abstractmethod
    def save(
        self, programa: ActaEntity
    ) -> ActaEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> ActaEntity:
        pass

    @abstractmethod
    def find_by_llave(self, llave_id: str) -> ActaEntity:
        pass


    @abstractmethod
    def find_by_llave_update(self, llave_id: str) -> ActaEntity:
        pass

    
    @abstractmethod
    def find_by_llave_approved(self, llave_id: str) -> ActaEntity:
        pass


    @abstractmethod
    def update(self, acta: ActaEntity) -> ActaEntity:
        """Actualiza una acta existente"""
        pass

    @abstractmethod
    def estatus(self, acta: ActaEntity) -> ActaEntity:
        """Actualiza una acta existente"""
        pass


    @abstractmethod
    def aprobar_acta(self, llave_id: str, aprobado: bool, usuario_id: int) -> ActaEntity:
        pass