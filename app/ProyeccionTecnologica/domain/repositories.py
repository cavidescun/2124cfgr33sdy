from abc import ABC, abstractmethod
from app.ProyeccionTecnologica.domain.entities import ProyeccionTecnologicaEntity

class ProyeccionTecnologicaRepository(ABC):
    @abstractmethod
    def save(
        self, programa: ProyeccionTecnologicaEntity
    ) -> ProyeccionTecnologicaEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> ProyeccionTecnologicaEntity:
        pass

    @abstractmethod
    def find_by_llave(self, id: int) -> ProyeccionTecnologicaEntity:
        pass

    @abstractmethod
    def estatus(self, id: int) -> ProyeccionTecnologicaEntity:
        pass
    @abstractmethod
    def estatus_flag(self, llave_id: str) -> None:
        pass

    @abstractmethod
    def find_by_llave_update(self, llave_id: str) -> ProyeccionTecnologicaEntity:
        pass

    @abstractmethod
    def update(self, proyeccion_tecnologica: ProyeccionTecnologicaEntity) -> ProyeccionTecnologicaEntity:
        """Actualiza una ProyeccionTecnologicaEntity existente"""
        pass

