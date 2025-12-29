from typing import Dict, Any
from app.Core.domain.repositories.repositories_spadies import SpadiesRepository
from app.Core.infrastructure.models.models_spadies import TasaDesercionIES


class SpadiesRepositoryImpl(SpadiesRepository):

    def obtener_tasas_desercion_por_institucion(self, nombre_ies: str, ultimos_años: int = 6) -> Dict[str, Any]:
        """
        Obtiene las tasas de deserción de una institución en los últimos N años
        
        Args:
            nombre_ies: Nombre de la institución educativa
            ultimos_años: Cantidad de años hacia atrás (por defecto 6)
            
        Returns:
            Diccionario con IES y años (añouno hasta añoseis)
        """
        if not nombre_ies or not nombre_ies.strip():
            return self._estructura_vacia()
        
        # Buscar registros de la institución (coincidencia parcial, case-insensitive)
        # Ordenar por año descendente y tomar los últimos N años
        registros = (
            TasaDesercionIES.objects
            .filter(nombre_ies__icontains=nombre_ies.strip())
            .order_by('-año')[:ultimos_años]
        )
        
        if not registros:
            return self._estructura_vacia()
        
        # Convertir a lista para poder acceder por índice
        registros_list = list(registros)
        
        # Construir resultado
        # añoseis = más reciente, añouno = hace 6 años
        resultado = {
            "IES": registros_list[0].nombre_ies if registros_list else ""
        }
        
        # Mapear los registros a los campos (invertido porque vienen ordenados desc)
        # registros_list[0] = año más reciente -> añoseis
        # registros_list[5] = año más antiguo -> añouno
        nombres_años = ["añoseis", "añocinco", "añocuatro", "añotres", "añodos", "añouno"]
        
        for i, nombre_año in enumerate(nombres_años):
            if i < len(registros_list):
                tasa = registros_list[i].tasa_desercion
                # Convertir Decimal a float
                resultado[nombre_año] = float(tasa) if tasa is not None else 0.0
            else:
                resultado[nombre_año] = 0.0
        
        return resultado
    
    def _estructura_vacia(self) -> Dict[str, Any]:
        """Retorna estructura vacía cuando no hay datos"""
        return {
            "IES": "",
            "añoseis": 0.0,
            "añocinco": 0.0,
            "añocuatro": 0.0,
            "añotres": 0.0,
            "añodos": 0.0,
            "añouno": 0.0
        }