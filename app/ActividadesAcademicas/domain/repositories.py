from abc import ABC, abstractmethod

from app.ActividadesAcademicas.domain.entities import ActividadesAcademicasEntity


class ActividadesAcademicasRepository(ABC):
    @abstractmethod
    def save(
        self, programa: ActividadesAcademicasEntity
    ) -> ActividadesAcademicasEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> ActividadesAcademicasEntity:
        pass
