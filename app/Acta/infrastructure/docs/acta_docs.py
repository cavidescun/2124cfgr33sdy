from drf_yasg import openapi

# Ejemplo actualizado con el JSON que enviaste
etiquetas_dinamicas_example = {
    "etiquetas_dinamicas": {
        "variables": {
            "proceso": "a",
            "busqueda_snies": 2123,
            "nivel": "Posgrado",
            "ciclo": "Especialización",
            "nombre_de_programa": "11",
            "tipo_registro": "Registro Calificado",
            "modalidad_programa": "Presencial",
            "regional_programa": "a",
            "título_especialista": "1212",
            "perfil_especialista": "wkjfdf",
            "duracion_programa": 12233,
            "periodicidad_programa": "Semestral",
            "admitidos_programa": 22,
            "viabilidad_financiera": True,
            "fecha": "2025-10-17",
            "escuela_datos": "Ingeniería",
            "correo_director": "dfjdsf@prueba.com",
            "campo_amplio": "Ingeniería, Industria y Construcción",
            "campo_especifico": "Arquitectura y Construcción",
            "campo_detallado": "Construcción e Ingeniería Civil",
            "área_de_conocimiento": "Bellas Artes",
            "nucleo_basico": "Diseño",
            "programas_similares": [
                "Administración",
                "Administración en Salud"
            ]
        }
    }
}

# Documentación Swagger actualizada

crear_acta_doc = {
    "operation_summary": "Crear un programa de posgrado",
    "operation_description": "Registrar un programa de posgrado usando el esquema dinámico de etiquetas.",
    "tags": ["Actas"],
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        example=etiquetas_dinamicas_example
    ),
    "responses": {
        201: openapi.Response(
            description="Programa creado exitosamente",
        ),
        400: openapi.Response(description="Error de validación")
    }
}

obtener_acta_doc = {
    "operation_summary": "Obtener un programa de posgrado",
    "operation_description": "Devuelve un programa de posgrado con la estructura completa de etiquetas dinámicas.",
    "tags": ["Actas"],
    "manual_parameters": [
        openapi.Parameter(
            name="llave_id",
            in_=openapi.IN_QUERY,
            description="Identificador único del programa (por ejemplo: LLAVE-5BE573CF)",
            type=openapi.TYPE_STRING,
            required=True,
            example="LLAVE-5BE573CF"
        )
    ],
    "responses": {
        200: openapi.Response(
            description="Programa obtenido exitosamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example=etiquetas_dinamicas_example
            )
        ),
        404: openapi.Response(
            description="Programa no encontrado",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={"error": "Programa no encontrado"}
            )
        )
    }
}


actualizar_acta_doc = {
    "operation_summary": "Actualizar parcialmente un programa de posgrado",
    "operation_description": "Permite actualizar uno o varios campos de un programa de posgrado existente. Solo es necesario enviar los campos que se desean modificar.",
    "tags": ["Actas"],
    "manual_parameters": [
        openapi.Parameter(
            name="llave_id",
            in_=openapi.IN_QUERY,
            description="Identificador único del programa (por ejemplo: LLAVE-5BE573CF)",
            type=openapi.TYPE_STRING,
            required=True,
            example="LLAVE-5BE573CF"
        )
    ],
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description="Enviar solo los campos que se desean actualizar dentro de 'etiquetas_dinamicas.variables'",
        example={
            "etiquetas_dinamicas": {
                "variables": {
                    "nivel": "Posgrado",
                    "ciclo": "Maestría",
                    "duracion_programa": 24,
                    "admitidos_programa": 30
                }
            }
        }
    ),
    "responses": {
        200: openapi.Response(
            description="Programa actualizado exitosamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={
                    "message": "Programa actualizado exitosamente",
                    "llave_id": "LLAVE-5BE573CF",
                    "campos_actualizados": ["nivel", "ciclo", "duracion_programa", "admitidos_programa"]
                }
            )
        ),
        400: openapi.Response(
            description="Error de validación",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={"error": "Datos inválidos"}
            )
        ),
        404: openapi.Response(
            description="Programa no encontrado",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={"error": "Programa no encontrado"}
            )
        )
    }
}

acta_aprobacion_doc = {
    "operation_summary": "Aprobar o rechazar un acta",
    "operation_description": (
        "Permite aprobar o rechazar un acta existente. "
        "El identificador del acta se envía por query params y "
        "el estado de aprobación se envía en el body."
    ),
    "tags": ["Actas"],
    "manual_parameters": [
        openapi.Parameter(
            name="llave_id",
            in_=openapi.IN_QUERY,
            description="Identificador único del acta",
            type=openapi.TYPE_STRING,
            required=False,  # ⬅️ no obligatorio
            example="123e4567-e89b-12d3-a456-426614174000",
        )
    ],
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description="Body libre. Se puede enviar cualquier estructura.",
        additionalProperties=True,  # ⬅️ permite cualquier cosa
        example={
            "flag": True
        }
    ),
    "responses": {
        200: openapi.Response(
            description="Estado del acta actualizado",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                additionalProperties=True,
                example={
                    "message": "Estado del acta actualizado correctamente",
                    "data": {
                        "llave_id": "123e4567-e89b-12d3-a456-426614174000",
                        "aprobado": True
                    }
                },
            ),
        ),
        400: openapi.Response(
            description="Error",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                additionalProperties=True,
                example={"error": "Error en la solicitud"},
            ),
        ),
    },
}
