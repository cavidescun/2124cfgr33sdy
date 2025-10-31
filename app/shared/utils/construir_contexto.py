import os
import math
from typing import Any, Dict, List

from app.shared.logic.contextoreporte import ContextoReporte, ImagenConfig
from app.shared.utils.graficos import (
    crear_grafico_barras,
    crear_grafico_barras_agrupadas,
    crear_grafico_torta,
    crear_grafico_lineas,
    crear_grafico_barras_horizontales,
)


class ConstruirContextoDinamico:
    """Clase encargada de construir un contexto dinámico de reporte con tablas y gráficos."""

    @staticmethod
    def construir_contexto_dinamico(etiquetas: Dict[str, Any]) -> ContextoReporte:
        """
        Construye un contexto de reporte con tablas, variables y gráficos generados dinámicamente.

        Args:
            etiquetas (dict): Estructura con tablas, variables y configuración de gráficos.

        Returns:
            ContextoReporte: Objeto con datos, variables e imágenes generadas.
        """
        contexto = ContextoReporte()
        tablas = etiquetas.get("tablas", {})
        graficos_config = etiquetas.get("_graficos_config", {})
        variables = etiquetas.get("variables", {})

        contexto.tablas = tablas
        contexto.variables = variables
        os.makedirs("output", exist_ok=True)

        for nombre_tabla, config_grafico in graficos_config.items():
            if nombre_tabla not in tablas:
                print(f"⚠️ Tabla '{nombre_tabla}' no encontrada para gráfico.")
                continue

            data = tablas[nombre_tabla]
            tipo = config_grafico.get("tipo")
            titulo = config_grafico.get("titulo", f"Gráfico de {nombre_tabla}")
            filename = config_grafico.get("filename", f"{nombre_tabla}_grafico.png")
            output_path = os.path.join("output", filename)

            try:
                categorias = ConstruirContextoDinamico.extraer_categorias(
                    data, config_grafico
                )
                valores = ConstruirContextoDinamico.extraer_valores(
                    data, config_grafico
                )

                # --- Debug info ---
                print(f"📊 Gráfico '{titulo}':")
                print(f"   - Tipo: {tipo}")
                print(f"   - Categorías ({len(categorias)}): {categorias}")
                print(f"   - Valores ({len(valores)}): {valores}")

                # Validar longitud en gráficos simples
                if tipo in ["barras", "torta", "lineas", "barras_horizontales"] and len(
                    categorias
                ) != len(valores):
                    print(
                        f"⚠️ ERROR: Mismatch en '{titulo}' - categorías: {len(categorias)}, valores: {len(valores)}"
                    )
                    continue

                # --- Generación de gráfico según tipo ---
                ConstruirContextoDinamico._crear_grafico(
                    tipo=tipo,
                    output_path=output_path,
                    titulo=titulo,
                    categorias=categorias,
                    valores=valores,
                    data=data,
                    config=config_grafico,
                )

                # Agregar imagen generada al contexto
                contexto.imagenes.append(
                    ImagenConfig(key=titulo, path=output_path, width=12)
                )

                print(f"✅ Gráfico '{titulo}' creado exitosamente.\n")

            except Exception as e:
                print(f"❌ Error al crear gráfico '{titulo}': {e}")
                import traceback

                traceback.print_exc()
                continue

        return contexto

    # ------------------------------------------------------------------
    # Métodos auxiliares
    # ------------------------------------------------------------------

    @staticmethod
    def extraer_categorias(
        data: List[Dict[str, Any]], config: Dict[str, Any]
    ) -> List[str]:
        """Extrae las categorías de los datos según la configuración."""
        etiquetas_x = config.get("etiquetas_x")
        categorias_campo = config.get("categorias_campo")

        if etiquetas_x:
            return etiquetas_x
        if categorias_campo and data:
            return [str(fila.get(categorias_campo, "")) for fila in data]
        if data:
            return [f"Item {i+1}" for i in range(len(data))]

        return []

    @staticmethod
    def extraer_valores(
        data: List[Dict[str, Any]], config: Dict[str, Any]
    ) -> List[float]:
        """Extrae los valores numéricos según la configuración del gráfico."""
        valores_campo = config.get("valores_campo")
        valores_campos = config.get("valores_campos")

        def limpiar_valor(valor: Any) -> float:
            """Convierte valores a float, eliminando símbolos y comas."""
            if valor is None:
                return 0.0
            valor_limpio = str(valor).replace("$", "").replace(",", "").strip()
            try:
                return float(valor_limpio)
            except ValueError:
                return 0.0

        # Caso 1: gráfico simple
        if valores_campo:
            return (
                [limpiar_valor(fila.get(valores_campo, 0)) for fila in data]
                if data
                else []
            )

        # Caso 2: gráfico agrupado
        if valores_campos:
            valores_agregados = [0.0] * len(valores_campos)
            for fila in data:
                for i, campo in enumerate(valores_campos):
                    valores_agregados[i] += limpiar_valor(fila.get(campo, 0))
            return valores_agregados

        return []

    # ------------------------------------------------------------------
    # Generador de gráficos
    # ------------------------------------------------------------------

    @staticmethod
    def _crear_grafico(
        tipo: str,
        output_path: str,
        titulo: str,
        categorias: List[str],
        valores: List[float],
        data: List[Dict[str, Any]],
        config: Dict[str, Any],
    ) -> None:
        """Genera un gráfico según el tipo especificado."""
        color = config.get("color", "skyblue")

        if tipo == "barras":
            crear_grafico_barras(output_path, titulo, categorias, valores, color)
        elif tipo == "torta":
            crear_grafico_torta(output_path, titulo, categorias, valores)
        elif tipo == "lineas":
            crear_grafico_lineas(output_path, titulo, categorias, valores)
        elif tipo == "barras_horizontales":
            crear_grafico_barras_horizontales(
                output_path, titulo, categorias, valores, color
            )
        elif tipo == "barras_agrupadas":
            crear_grafico_barras_agrupadas(
                output_path,
                titulo,
                categorias,
                data,
                config.get("valores_campos", []),
                config.get("etiquetas_x", []),
                colores=None,
            )
        else:
            raise ValueError(f"Tipo de gráfico desconocido: {tipo}")
