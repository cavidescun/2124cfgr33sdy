from abc import ABC, abstractmethod

from app.MediosEducativos.domain.entities import MediosEducativosEntity


class MediosEducativosRepository(ABC):
    @abstractmethod
    def save(
        self, programa: MediosEducativosEntity
    ) -> MediosEducativosEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> MediosEducativosEntity:
        pass
