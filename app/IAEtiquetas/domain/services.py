from abc import ABC, abstractmethod
from typing import Dict, Any

class IAService(ABC):
    @abstractmethod
    def analizar(self, prompt: str, datos: Dict[str, Any]) -> str:
        pass
