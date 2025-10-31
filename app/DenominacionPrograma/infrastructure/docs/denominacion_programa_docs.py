from drf_yasg import openapi
from ..serializers import DenominacionProgramaSerializer

etiquetas_dinamicas_example = {
    "variables": {
        "nombre_de_programa": "Especialización en Producción Láctea",
        "área_de_conocimiento": "Ciencias Agrarias",
        "título_especialista": "Especialista en Producción Láctea",
        "perfil_especialista": (
            "es un profesional con capacidad para diseñar, implementar y optimizar procesos "
            "de producción y transformación de leche bajo estándares de calidad y sostenibilidad."
        ),
        "exigencias_mercado": (
            "las necesidades del sector agroindustrial y los estándares de competitividad "
            "global del mercado lácteo colombiano"
        ),
        "pertinencia_titulo": (
            "la naturaleza del programa y la formación avanzada en el área de producción "
            "y transformación láctea"
        ),
        "pertinencia_duracion": "de tres semestres académicos en modalidad presencial",
        "Num_creditos": 40,
        "Modalidad_programa": "Presencial",
        "Regional_programa": "Bogotá D.C.",
        "Duracion_programa": "1.5 años",
        "Periodicidad_programa": "Semestral",
        "Admitidos_programa": 25,
        "Num_acuerdo": "Acuerdo No. 023 del Consejo Académico 2025",
        "competencias_habilidades_programa": (
            "funciones de planeación, control de calidad, innovación tecnológica "
            "y gestión productiva en empresas del sector lácteo y agroindustrial"
        ),
        "campo_amplio": "Ciencias Agropecuarias",
        "campo_especifico": "Producción Animal",
        "campo_detallado": "Tecnología de Productos Lácteos",
        "referencias": (
            "Ministerio de Agricultura y Desarrollo Rural (2024). Informe de competitividad "
            "del sector lácteo colombiano. ICA (2023). Buenas prácticas ganaderas y lácteas en Colombia."
        ),
    }
}

crear_programa_doc = {
    "operation_summary": "Crear un nuevo programa de especialización",
    "operation_description": (
        "Este endpoint permite registrar un nuevo programa de especialización. "
        "Utiliza todas las validaciones del serializer, incluyendo verificaciones de créditos, "
        "admitidos y coherencia entre modalidad, duración y periodicidad."
    ),
    "tags": ["Denominacion Programa"],
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "llave_maestra": openapi.Schema(
                type=openapi.TYPE_STRING,
                example="E121244",
            ),
            "etiquetas_dinamicas": openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example=etiquetas_dinamicas_example,
            ),
        },
        required=[
            "llave_maestra",
            "etiquetas_dinamicas",
        ],
    ),
    "responses": {
        201: openapi.Response(
            description="Programa creado exitosamente",
            schema=DenominacionProgramaSerializer,
        ),
        400: openapi.Response(description="Error de validación en los datos enviados"),
    },
}
