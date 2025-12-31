from typing import List, Dict, Any
from django.db import connections
from app.Core.domain.repositories.repositories_sqlserver import SqlServerRepository


class SqlServerRepositoryImpl(SqlServerRepository):
    
    def ejecutar_query(self, query: str, params: tuple = None, database: str = "sqlserver_db1") -> List[Dict[str, Any]]:
        """
        Ejecuta una query SQL directa en SQL Server y retorna resultados
        
        Args:
            query: Query SQL a ejecutar
            params: Tupla con parámetros para la query (usa %s como placeholder)
            database: Nombre de la conexión (sqlserver_db1, sqlserver_db2, etc)
            
        Returns:
            Lista de diccionarios donde cada dict es una fila
            
        Ejemplo:
            # Consultar en base de datos 1
            query = "SELECT * FROM tabla WHERE campo = %s"
            params = ("valor",)
            resultados = repo.ejecutar_query(query, params, database="sqlserver_db1")
            
            # Consultar en base de datos 2
            resultados2 = repo.ejecutar_query(query, params, database="sqlserver_db2")
        """
        resultados = []
        
        try:
            with connections[database].cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                
                # Obtener nombres de columnas
                columns = [col[0] for col in cursor.description]
                
                # Convertir cada fila a diccionario
                for row in cursor.fetchall():
                    resultados.append(dict(zip(columns, row)))
        
        except Exception as e:
            print(f"Error ejecutando query en {database}: {e}")
            raise
        
        return resultados
    
    def ejecutar_query_unica(self, query: str, params: tuple = None, database: str = "sqlserver_db1") -> Dict[str, Any]:
        """
        Ejecuta una query que retorna un único registro
        
        Args:
            query: Query SQL a ejecutar
            params: Parámetros para la query
            database: Nombre de la conexión de base de datos
            
        Returns:
            Diccionario con el primer resultado o {} si no hay resultados
        """
        resultados = self.ejecutar_query(query, params, database)
        return resultados[0] if resultados else {}
    
    def ejecutar_query_escalar(self, query: str, params: tuple = None, database: str = "sqlserver_db1") -> Any:
        """
        Ejecuta una query que retorna un único valor (COUNT, SUM, etc)
        
        Args:
            query: Query SQL a ejecutar
            params: Parámetros para la query
            database: Nombre de la conexión de base de datos
            
        Returns:
            El valor escalar o None
        """
        try:
            with connections[database].cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                
                row = cursor.fetchone()
                return row[0] if row else None
        
        except Exception as e:
            print(f"Error ejecutando query escalar en {database}: {e}")
            raise