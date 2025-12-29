from abc import ABC, abstractmethod
from typing import List, Dict, Any

class SpadiesRepository(ABC):

    @abstractmethod
    def obtener_tasas_desercion_por_institucion(self, nombre_ies: str, ultimos_años: int = 6) -> Dict[str, Any]:
        pass