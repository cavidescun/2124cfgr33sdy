from drf_yasg import openapi

crear_programa_doc = {
    "operation_description": "Genera un documento maestro completo a partir de una llave maestra numérica.",
    "tags": ["Documento Maestro Programa"],
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "llave_maestra": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Llave maestra numérica para identificar el programa.",
                example="12345",
            ),
        },
        required=["llave_maestra"],
    ),
    "responses": {
        201: openapi.Response(
            description="Documento maestro generado exitosamente.",
            examples={
                "application/json": {
                    "message": "Justificación de programa creada exitosamente",
                    "id": "documento_12345.pdf",
                }
            },
        ),
        400: openapi.Response(
            description="Error de validación.",
            examples={
                "application/json": {
                    "llave_maestra": ["La llave maestra debe ser un número válido."]
                }
            },
        ),
        500: openapi.Response(
            description="Error interno del servidor.",
            examples={"application/json": {"error": "Error al procesar la solicitud."}},
        ),
    },
}
