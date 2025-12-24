from abc import ABC, abstractmethod
from typing import Any, Dict

class SniesRepository(ABC):

    @abstractmethod
    def buscar_programas_similares(self, filtros: Dict[str, Any]):
        """
        Retorna programas académicos similares según criterios SNIES
        """
        pass
