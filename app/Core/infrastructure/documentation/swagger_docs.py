from drf_yasg import openapi
from rest_framework.response import Response
from django.http import FileResponse
from django.urls import reverse
from django.conf import settings
import os

# ================================
#  EJEMPLO DE RESPUESTA GET
# ================================
listar_ejemplo = {
    "count": 4,
    "page": 1,
    "page_size": 10,
    "results": [
        {
            "llave_maestra": "LLAVE-123",
            "filename": "especializacion.docx",
            "size": 248832,
            "modified": "2025-12-09T17:28:54",
            "download_url": "http://localhost:8000/api/descargar-informe?llave_maestra=LLAVE-123&file=especializacion.docx"
        },
        {
            "llave_maestra": "LLAVE-123",
            "filename": "resumen.pdf",
            "size": 50291,
            "modified": "2025-12-09T16:21:10",
            "download_url": "http://localhost:8000/api/descargar-informe?llave_maestra=LLAVE-123&file=resumen.pdf"
        },
        {
            "llave_maestra": "LLAVE-456",
            "filename": "informe.docx",
            "size": 189420,
            "modified": "2025-12-09T15:10:30",
            "download_url": "http://localhost:8000/api/descargar-informe?llave_maestra=LLAVE-456&file=informe.docx"
        }
    ]
}

# ================================
#  DOCUMENTACIÓN GET – LISTAR
# ================================
listar_archivos_doc = {
    "operation_summary": "Listar archivos disponibles",
    "operation_description": (
        "Retorna la lista de archivos generados con paginación incluida.\n\n"
        "**Comportamiento:**\n"
        "- **Sin llave_maestra**: Lista todos los archivos de todas las carpetas en `/app/output`\n"
        "- **Con llave_maestra**: Lista solo los archivos de esa carpeta específica"
    ),
    "tags": ["Procesos"],

    "manual_parameters": [
        openapi.Parameter(
            name="llave_maestra",
            in_=openapi.IN_QUERY,
            description="Llave maestra del proceso (opcional). Si no se envía, lista todos los archivos de todas las carpetas.",
            type=openapi.TYPE_STRING,
            required=False,
            example="LLAVE-123"
        ),
        openapi.Parameter(
            name="page",
            in_=openapi.IN_QUERY,
            description="Número de página",
            type=openapi.TYPE_INTEGER,
            required=False,
            default=1,
            example=1
        ),
        openapi.Parameter(
            name="page_size",
            in_=openapi.IN_QUERY,
            description="Cantidad de elementos por página",
            type=openapi.TYPE_INTEGER,
            required=False,
            default=10,
            example=10
        ),
    ],

    "responses": {
        200: openapi.Response(
            description="Listado de archivos",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "count": openapi.Schema(
                        type=openapi.TYPE_INTEGER,
                        description="Total de archivos encontrados"
                    ),
                    "page": openapi.Schema(
                        type=openapi.TYPE_INTEGER,
                        description="Página actual"
                    ),
                    "page_size": openapi.Schema(
                        type=openapi.TYPE_INTEGER,
                        description="Elementos por página"
                    ),
                    "results": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                "llave_maestra": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    description="Llave maestra del archivo"
                                ),
                                "filename": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    description="Nombre del archivo"
                                ),
                                "size": openapi.Schema(
                                    type=openapi.TYPE_INTEGER,
                                    description="Tamaño en bytes"
                                ),
                                "modified": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    description="Fecha de modificación (ISO 8601)"
                                ),
                                "download_url": openapi.Schema(
                                    type=openapi.TYPE_STRING,
                                    description="URL de descarga directa"
                                ),
                            }
                        )
                    ),
                },
                example=listar_ejemplo
            )
        ),
        404: openapi.Response(
            description="La carpeta no existe o no hay archivos",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        example="La carpeta output no existe"
                    )
                }
            )
        ),
    }
}

# ================================
#  DOCUMENTACIÓN POST – DESCARGAR
# ================================
descargar_archivo_doc = {
    "operation_summary": "Descargar archivo",
    "operation_description": "Descarga un archivo específico ubicado dentro de `/app/output/<llave_maestra>/`",
    "tags": ["Documentos"],

    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["llave_maestra", "file"],
        properties={
            "llave_maestra": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Llave maestra que identifica la carpeta",
                example="LLAVE-123"
            ),
            "file": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Nombre del archivo a descargar (incluyendo extensión)",
                example="especializacion.docx"
            ),
        }
    ),

    "responses": {
        200: openapi.Response(
            description="Archivo devuelto en binario para descarga",
            schema=openapi.Schema(
                type=openapi.TYPE_FILE,
                description="Archivo binario (stream)",
            )
        ),
        400: openapi.Response(
            description="Datos incompletos",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        example="Debe enviar llave_maestra y file"
                    )
                }
            )
        ),
        404: openapi.Response(
            description="Archivo no encontrado",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "error": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        example="No existe archivo"
                    )
                }
            )
        ),
    }
}


# ================================
#  EJEMPLO DE RESPUESTA
# ================================
email_token_ejemplo_success = {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MDg2NjQwMCwiaWF0IjoxNjcwNzgwMDAwLCJqdGkiOiJhYmMxMjM0NTYiLCJ1c2VyX2lkIjoxfQ.xyz789",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwNzgzNjAwLCJpYXQiOjE2NzA3ODAwMDAsImp0aSI6ImRlZjc4OTAxMiIsInVzZXJfaWQiOjF9.abc456"
}

email_token_ejemplo_error = {
    "email": ["Este campo es requerido."]
}

email_token_ejemplo_not_found = {
    "detail": "Usuario no encontrado con este email."
}

# ================================
#  DOCUMENTACIÓN EMAIL TOKEN
# ================================
email_token_doc = {
    "operation_summary": "Obtener tokens JWT por email",
    "operation_description": (
        "Genera tokens de acceso y refresh para un usuario autenticado mediante su email.\n\n"
        "**Flujo:**\n"
        "1. El usuario proporciona su email\n"
        "2. El sistema valida que el email existe en la base de datos\n"
        "3. Se generan tokens JWT (access y refresh)\n"
        "4. Los tokens se devuelven para autenticación en requests posteriores\n\n"
        "**Uso de tokens:**\n"
        "- **access**: Token de corta duración para autenticar requests (enviar en header: `Authorization: Bearer <access_token>`)\n"
        "- **refresh**: Token de larga duración para obtener nuevos access tokens cuando expiren\n\n"
        "**Nota:** Este endpoint no requiere autenticación previa (AllowAny)."
    ),
    "tags": ["Autenticación"],

    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["email"],
        properties={
            "email": openapi.Schema(
                type=openapi.TYPE_STRING,
                format=openapi.FORMAT_EMAIL,
                description="Email del usuario registrado en el sistema",
                example="admin@example.com"
            ),
        }
    ),

    "responses": {
        200: openapi.Response(
            description="Tokens generados exitosamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "refresh": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Token refresh JWT (larga duración)",
                    ),
                    "access": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Token access JWT (corta duración)",
                    ),
                },
                example=email_token_ejemplo_success
            )
        ),
        400: openapi.Response(
            description="Datos inválidos o incompletos",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "email": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                        description="Errores de validación del campo email"
                    ),
                },
                example=email_token_ejemplo_error
            )
        ),
        404: openapi.Response(
            description="Usuario no encontrado",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "detail": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Mensaje de error"
                    ),
                },
                example=email_token_ejemplo_not_found
            )
        ),
    }
}




# ================================
#  EJEMPLOS DE RESPUESTA
# ================================
unificacion_ejemplo_error = {
    "llave_maestra": [
        "Este campo es requerido."
    ]
}

unificacion_ejemplo_error_formato = {
    "llave_maestra": [
        "Formato de llave maestra inválido."
    ]
}

# ================================
#  DOCUMENTACIÓN UNIFICACIÓN
# ================================
unificacion_informacion_doc = {
    "operation_summary": "Unificar información del proceso",
    "operation_description": (
        "Ejecuta el proceso de unificación de información asociada a una llave maestra.\n\n"
        "**Flujo del proceso:**\n"
        "1. Valida que la llave maestra tenga el formato correcto\n"
        "2. Ejecuta el caso de uso de unificación de información\n"
        "3. Consolida y procesa todos los datos relacionados con la llave maestra\n"
        "4. Retorna un código 204 (No Content) cuando finaliza exitosamente\n\n"
        "**Nota:** Este proceso puede tomar varios segundos dependiendo de la cantidad de información a unificar."
    ),
    "tags": ["Procesos"],

    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["llave_maestra"],
        properties={
            "llave_maestra": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Identificador único del proceso a unificar",
                example="LLAVE-E26E95BF",
                pattern="^LLAVE-[A-Z0-9]+$"
            ),
        }
    ),

    "responses": {
        204: openapi.Response(
            description="Unificación ejecutada exitosamente (sin contenido en respuesta)",
        ),
        400: openapi.Response(
            description="Datos inválidos o llave maestra con formato incorrecto",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "llave_maestra": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                        description="Errores de validación del campo llave_maestra"
                    ),
                },
                examples={
                    "campo_requerido": {
                        "value": unificacion_ejemplo_error
                    },
                    "formato_invalido": {
                        "value": unificacion_ejemplo_error_formato
                    }
                }
            )
        ),
        500: openapi.Response(
            description="Error interno durante el proceso de unificación",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "detail": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Mensaje de error"
                    ),
                },
                example={"detail": "Error al procesar la unificación"}
            )
        ),
    }
}

# ================================
#  DOCUMENTACIÓN GENERAR DOCUMENTO
# ================================
generar_documento_doc = {
    "operation_summary": "Generar documento del proceso",
    "operation_description": (
        "Genera el documento final asociado a una llave maestra.\n\n"
        "**Flujo del proceso:**\n"
        "1. Valida que la llave maestra tenga el formato correcto\n"
        "2. Ejecuta el caso de uso de generación de documento\n"
        "3. Crea el documento con toda la información consolidada\n"
        "4. Guarda el archivo en `/app/output/<llave_maestra>/`\n"
        "5. Retorna un código 204 (No Content) cuando finaliza exitosamente\n\n"
        "**Nota:** Después de ejecutar este endpoint, puedes listar y descargar el documento generado usando el endpoint de descarga."
    ),
    "tags": ["Procesos"],

    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["llave_maestra"],
        properties={
            "llave_maestra": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Identificador único del proceso para generar documento",
                example="LLAVE-E26E95BF",
                pattern="^LLAVE-[A-Z0-9]+$"
            ),
        }
    ),

    "responses": {
        204: openapi.Response(
            description="Documento generado exitosamente (sin contenido en respuesta)",
        ),
        400: openapi.Response(
            description="Datos inválidos o llave maestra con formato incorrecto",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "llave_maestra": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_STRING),
                        description="Errores de validación del campo llave_maestra"
                    ),
                },
                examples={
                    "campo_requerido": {
                        "value": {"llave_maestra": ["Este campo es requerido."]}
                    },
                    "formato_invalido": {
                        "value": {"llave_maestra": ["Formato de llave maestra inválido."]}
                    }
                }
            )
        ),
        404: openapi.Response(
            description="No se encontró información para la llave maestra especificada",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "detail": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Mensaje de error"
                    ),
                },
                example={"detail": "No existe información para esta llave maestra"}
            )
        ),
        500: openapi.Response(
            description="Error interno durante la generación del documento",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "detail": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="Mensaje de error"
                    ),
                },
                example={"detail": "Error al generar el documento"}
            )
        ),
    }
}



punto_de_control = {
    "operation_summary": "Verificar estado de información para unificación",
    "operation_description": (
        "Verifica si la información asociada a una llave maestra está completa y lista "
        "para ejecutar el proceso de unificación.\n\n"
        "**Propósito del endpoint:**\n"
        "- Permite al frontend determinar si el botón de 'Unificar' debe habilitarse.\n"
        "- No ejecuta el proceso de unificación, solo valida el estado actual.\n\n"
        "**Flujo del proceso:**\n"
        "1. Valida que la llave maestra tenga el formato correcto.\n"
        "2. Consulta si ya existe toda la información requerida.\n"
        "3. Retorna un estado indicando si está lista o no.\n\n"
        "**Tiempo de respuesta:** Rápido, ya que solo consulta el estado."
    ),
    "tags": ["Procesos"],

    # ❗ Se elimina request_body y se usa manual_parameters para query params
    "manual_parameters": [
        openapi.Parameter(
            name="llave_maestra",
            in_=openapi.IN_QUERY,
            description="Identificador único del proceso",
            required=True,
            type=openapi.TYPE_STRING,
            pattern="^LLAVE-[A-Z0-9]+$",
            example="LLAVE-E26E95BF",
        )
    ],

    "responses": {
        200: openapi.Response(
            description="Estado consultado correctamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "message": openapi.Schema(type=openapi.TYPE_STRING),
                    "data": openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "acta": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                            "biblioteca": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                            "acuerdo": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                            "proyeccion_financiera": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                            "proyeccion_infra_tecnologica": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        }
                    )
                },
                example={
                    "message": "Estados obtenidos exitosamente",
                    "data": {
                        "acta": True,
                        "biblioteca": True,
                        "acuerdo": False,
                        "proyeccion_financiera": True,
                        "proyeccion_infra_tecnologica": True
                    }
                }
            )
        ),

        400: openapi.Response(
            description="Datos inválidos o llave maestra con formato incorrecto",
        ),

        500: openapi.Response(
            description="Error interno al revisar el estado",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "detail": openapi.Schema(type=openapi.TYPE_STRING)
                },
                example={"detail": "Error al verificar el estado de la llave maestra"}
            )
        ),
    }
}