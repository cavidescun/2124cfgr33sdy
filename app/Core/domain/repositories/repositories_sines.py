from abc import ABC, abstractmethod
from typing import Any, Dict, List

class SniesRepository(ABC):

    @abstractmethod
    def buscar_programas_similares(self, filtros: Dict[str, Any]):
        """
        Retorna programas académicos similares según criterios SNIES
        """
        pass
    
    @abstractmethod
    def buscar_por_nombres(self, nombres_programas: List[str]) -> List:
        """
        Busca programas académicos por sus nombres
        
        Args:
            nombres_programas: Lista de nombres de programas a buscar
            
        Returns:
            Lista de objetos ProgramaAcademico (uno por cada coincidencia)
        """
        pass

    