from abc import ABC, abstractmethod
from typing import Optional, List
from .entities import AnalisisIaEntity, PromptPlantilla

class AnalisisIARepository(ABC):
    @abstractmethod
    def save(self, analisis: AnalisisIaEntity) -> AnalisisIaEntity:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[AnalisisIaEntity]:
        pass

class PromptPlantillaRepository(ABC):
    @abstractmethod
    def get_by_nombre_etiqueta(self, nombre_etiqueta: str) -> Optional[PromptPlantilla]:
        pass

    @abstractmethod
    def save(self, template: PromptPlantilla) -> PromptPlantilla:
        pass
    
    @abstractmethod
    def get_all(self) -> List[PromptPlantilla]:
        pass
    
    @abstractmethod
    def delete_by_nombre_etiqueta(self, nombre_etiqueta: str) -> bool:
        pass