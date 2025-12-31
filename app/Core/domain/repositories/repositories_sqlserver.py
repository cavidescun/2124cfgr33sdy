from abc import ABC, abstractmethod
from typing import List, Dict, Any


class SqlServerRepository(ABC):
    
    @abstractmethod
    def ejecutar_query(self, query: str, params: tuple = None, database: str = "sqlserver_db1") -> List[Dict[str, Any]]:
        """
        Ejecuta una query SQL y retorna los resultados como lista de diccionarios
        
        Args:
            query: Query SQL a ejecutar
            params: Parámetros para la query (opcional)
            database: Nombre de la conexión de base de datos a usar
            
        Returns:
            Lista de diccionarios con los resultados
        """
        pass
    
    @abstractmethod
    def ejecutar_query_unica(self, query: str, params: tuple = None, database: str = "sqlserver_db1") -> Dict[str, Any]:
        """
        Ejecuta una query que retorna un único registro
        """
        pass
    
    @abstractmethod
    def ejecutar_query_escalar(self, query: str, params: tuple = None, database: str = "sqlserver_db1") -> Any:
        """
        Ejecuta una query que retorna un único valor
        """
        pass