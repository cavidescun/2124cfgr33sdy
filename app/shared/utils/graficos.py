import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")
import numpy as np


def crear_grafico_barras(output_path, titulo, categorias, valores, color="skyblue"):
    """Crea un gráfico de barras verticales con valores"""
    if len(categorias) != len(valores):
        raise ValueError(
            f"Mismatch: {len(categorias)} categorías vs {len(valores)} valores"
        )

    fig, ax = plt.subplots(figsize=(10, 6))
    barras = ax.bar(categorias, valores, color=color)

    # ✅ Añadir valores encima de cada barra
    for barra in barras:
        altura = barra.get_height()
        ax.text(
            barra.get_x() + barra.get_width() / 2.0,
            altura,
            f"{altura:,.0f}",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
        )

    ax.set_title(titulo, fontsize=14, fontweight="bold")
    ax.set_xlabel("Categorías", fontsize=11)
    ax.set_ylabel("Valores", fontsize=11)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()


def crear_grafico_barras_horizontales(
    output_path, titulo, categorias, valores, color="mediumseagreen"
):
    """Crea un gráfico de barras horizontales con valores"""
    if len(categorias) != len(valores):
        raise ValueError(
            f"Mismatch: {len(categorias)} categorías vs {len(valores)} valores"
        )

    fig, ax = plt.subplots(figsize=(10, 6))
    barras = ax.barh(categorias, valores, color=color)

    # ✅ Añadir valores al final de cada barra
    for barra in barras:
        ancho = barra.get_width()
        ax.text(
            ancho,
            barra.get_y() + barra.get_height() / 2.0,
            f"  {ancho:,.0f}",
            ha="left",
            va="center",
            fontsize=10,
            fontweight="bold",
        )

    ax.set_title(titulo, fontsize=14, fontweight="bold")
    ax.set_xlabel("Valores", fontsize=11)
    ax.set_ylabel("Categorías", fontsize=11)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()


def crear_grafico_torta(output_path, titulo, categorias, valores):
    """Crea un gráfico de torta con porcentajes y valores"""
    if len(categorias) != len(valores):
        raise ValueError(
            f"Mismatch: {len(categorias)} categorías vs {len(valores)} valores"
        )

    fig, ax = plt.subplots(figsize=(10, 8))

    # ✅ Función personalizada para mostrar porcentaje y valor
    def autopct_format(pct, allvals):
        absolute = int(pct / 100.0 * sum(allvals))
        return f"{pct:.1f}%\n({absolute:,})"

    wedges, texts, autotexts = ax.pie(
        valores,
        labels=categorias,
        autopct=lambda pct: autopct_format(pct, valores),
        startangle=90,
        textprops={"fontsize": 10},
    )

    # ✅ Hacer los textos en negrita
    for autotext in autotexts:
        autotext.set_color("white")
        autotext.set_fontweight("bold")

    ax.set_title(titulo, fontsize=14, fontweight="bold", pad=20)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()


def crear_grafico_lineas(output_path, titulo, categorias, valores):
    """Crea un gráfico de líneas con valores en los puntos"""
    if len(categorias) != len(valores):
        raise ValueError(
            f"Mismatch: {len(categorias)} categorías vs {len(valores)} valores"
        )

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(categorias, valores, marker="o", linewidth=2, markersize=8)

    # ✅ Añadir valores en cada punto
    for i, (cat, val) in enumerate(zip(categorias, valores)):
        ax.text(
            i,
            val,
            f"{val:,.0f}",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
        )

    ax.set_title(titulo, fontsize=14, fontweight="bold")
    ax.set_xlabel("Categorías", fontsize=11)
    ax.set_ylabel("Valores", fontsize=11)
    plt.xticks(rotation=45, ha="right")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()


def crear_grafico_barras_agrupadas(
    output_path, titulo, categorias, data, valores_campos, etiquetas_x, colores=None
):
    """Crea un gráfico de barras agrupadas con valores"""
    if not data or not valores_campos:
        raise ValueError("Se requieren datos y campos de valores")

    if colores is None:
        colores = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

    num_grupos = len(valores_campos)
    num_categorias = len(categorias)
    ancho_barra = 0.8 / num_grupos
    x = np.arange(num_categorias)

    fig, ax = plt.subplots(figsize=(12, 6))

    # ✅ Extraer valores limpios para cada campo
    def limpiar_valor(valor):
        if valor is None:
            return 0.0
        valor_limpio = str(valor).replace("$", "").replace(",", "").strip()
        try:
            return float(valor_limpio)
        except ValueError:
            return 0.0

    for i, campo in enumerate(valores_campos):
        # Extraer valores para este campo específico
        valores = [limpiar_valor(fila.get(campo, 0)) for fila in data]

        # ✅ Verificar dimensiones
        if len(valores) != num_categorias:
            print(
                f"⚠️ Ajustando valores de '{campo}': {len(valores)} -> {num_categorias}"
            )
            # Ajustar según sea necesario
            if len(valores) > num_categorias:
                valores = valores[:num_categorias]
            else:
                valores.extend([0] * (num_categorias - len(valores)))

        offset = (i - num_grupos / 2) * ancho_barra + ancho_barra / 2
        barras = ax.bar(
            x + offset,
            valores,
            ancho_barra,
            label=etiquetas_x[i] if i < len(etiquetas_x) else campo,
            color=colores[i % len(colores)],
        )

        # ✅ Añadir valores encima de cada barra
        for barra in barras:
            altura = barra.get_height()
            if altura > 0:
                ax.text(
                    barra.get_x() + barra.get_width() / 2.0,
                    altura,
                    f"{altura:,.0f}",
                    ha="center",
                    va="bottom",
                    fontsize=9,
                    fontweight="bold",
                )

    ax.set_title(titulo, fontsize=14, fontweight="bold")
    ax.set_xlabel("Categorías", fontsize=11)
    ax.set_ylabel("Valores", fontsize=11)
    ax.set_xticks(x)
    ax.set_xticklabels(categorias, rotation=45, ha="right")
    ax.legend()
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
