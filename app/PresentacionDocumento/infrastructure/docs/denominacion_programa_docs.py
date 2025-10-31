from drf_yasg import openapi
from ..serializers import PresentacionDocumentoSerializer

etiquetas_dinamicas_example = {
    "variables": {
        "nombre_de_programa": "Especialización en Producción Láctea",
        "Num_creditos": 40,
        "Modalidad_programa": "Presencial",
        "Regional_programa": "Bogotá D.C.",
      
    }
}

crear_programa_doc = {
    "operation_summary": "Crear un nuevo programa de especialización",
    "operation_description": (
        "Este endpoint permite registrar un nuevo programa de especialización. "
        "Utiliza todas las validaciones del serializer, incluyendo verificaciones de créditos, "
        "admitidos y coherencia entre modalidad, duración y periodicidad."
    ),
    "tags": ["Presentacion Documento"],
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
            schema=PresentacionDocumentoSerializer,
        ),
        400: openapi.Response(description="Error de validación en los datos enviados"),
    },
}
