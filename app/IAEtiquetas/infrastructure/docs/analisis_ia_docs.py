from drf_yasg import openapi

analizar_ia_doc = {
    "operation_summary": "Analizar datos con IA",
    "operation_description": """
    Analiza datos utilizando inteligencia artificial (OpenAI).
    
    Puedes proporcionar:
    1. **nombre_etiqueta**: Busca un template de prompt predefinido en la base de datos
    2. **datos**: Los datos a analizar (formato JSON)
    3. **prompt_custom** (opcional): Si no existe template, usa este prompt personalizado
    
    El sistema buscará un template asociado a la etiqueta. Si no existe y no proporcionas
    un prompt_custom, retornará un error.
    """,
    "tags": ["Análisis IA"],
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "nombre_etiqueta": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Nombre de la etiqueta para buscar el template",
                example="analisis_programa_academico"
            ),
            "datos": openapi.Schema(
                type=openapi.TYPE_OBJECT,
                description="Datos a analizar",
                example={
                    "nombre_programa": "Especialización en Gestión de Proyectos",
                    "modalidad": "Virtual",
                    "creditos": 30,
                    "duracion": "2 semestres"
                }
            ),
            "prompt_custom": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Prompt personalizado (opcional)",
                example="Analiza el siguiente programa académico y genera recomendaciones: {datos}"
            )
        },
        required=["nombre_etiqueta", "datos"]
    ),
    "responses": {
        200: openapi.Response(
            description="Análisis completado exitosamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                    "nombre_etiqueta": openapi.Schema(type=openapi.TYPE_STRING),
                    "resultado": openapi.Schema(type=openapi.TYPE_STRING),
                    "prompt_usado": openapi.Schema(type=openapi.TYPE_STRING),
                    "datos_entrada": openapi.Schema(type=openapi.TYPE_OBJECT),
                    "creado_en": openapi.Schema(type=openapi.TYPE_STRING, format="date-time")
                }
            )
        ),
        400: openapi.Response(description="Datos inválidos"),
        404: openapi.Response(description="Template no encontrado"),
        500: openapi.Response(description="Error al procesar con IA")
    }
}

listar_templates_doc = {
    "operation_summary": "Listar templates de prompts",
    "operation_description": "Obtiene la lista de todos los templates de prompts activos disponibles",
    "tags": ["Templates IA"],
    "responses": {
        200: openapi.Response(
            description="Lista de templates",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "nombre_etiqueta": openapi.Schema(type=openapi.TYPE_STRING),
                        "prompt_template": openapi.Schema(type=openapi.TYPE_STRING),
                        "descripcion": openapi.Schema(type=openapi.TYPE_STRING)
                    }
                )
            )
        )
    }
}

crear_template_doc = {
    "operation_summary": "Crear o actualizar template de prompt",
    "operation_description": """
    Crea un nuevo template de prompt o actualiza uno existente.
    
    El **nombre_etiqueta** debe ser único y no contener espacios (usa guiones bajos o guiones).
    
    El **prompt_template** puede usar placeholders:
    - `{datos}`: Inserta todos los datos como JSON
    - `{campo}`: Inserta el valor de un campo específico
    
    Ejemplo de prompt_template:
```
    Analiza el siguiente programa académico:
    
    {datos}
    
    Proporciona recomendaciones sobre:
    - Nombre: {nombre_programa}
    - Modalidad: {modalidad}
```
    """,
    "tags": ["Templates IA"],
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "nombre_etiqueta": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Identificador único (sin espacios, minúsculas recomendadas)",
                example="analisis_programa_academico"
            ),
            "prompt_template": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Contenido del prompt con placeholders {variable}",
                example="Analiza el siguiente programa: {datos}\n\nProporciona un informe detallado."
            ),
            "descripcion": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Descripción del propósito del template (opcional)",
                example="Análisis completo de programas académicos"
            )
        },
        required=["nombre_etiqueta", "prompt_template"]
    ),
    "responses": {
        201: openapi.Response(
            description="Template creado exitosamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "message": openapi.Schema(type=openapi.TYPE_STRING),
                    "data": openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "nombre_etiqueta": openapi.Schema(type=openapi.TYPE_STRING),
                            "prompt_template": openapi.Schema(type=openapi.TYPE_STRING),
                            "descripcion": openapi.Schema(type=openapi.TYPE_STRING)
                        }
                    )
                }
            )
        ),
        400: openapi.Response(description="Datos inválidos")
    }
}

obtener_template_doc = {
    "operation_summary": "Obtener template específico",
    "operation_description": "Obtiene los detalles de un template por su nombre de etiqueta",
    "tags": ["Templates IA"],
    "manual_parameters": [
        openapi.Parameter(
            'nombre_etiqueta',
            openapi.IN_PATH,
            description="Nombre de la etiqueta del template",
            type=openapi.TYPE_STRING,
            required=True
        )
    ],
    "responses": {
        200: openapi.Response(
            description="Template encontrado",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "nombre_etiqueta": openapi.Schema(type=openapi.TYPE_STRING),
                    "prompt_template": openapi.Schema(type=openapi.TYPE_STRING),
                    "descripcion": openapi.Schema(type=openapi.TYPE_STRING)
                }
            )
        ),
        404: openapi.Response(description="Template no encontrado")
    }
}

eliminar_template_doc = {
    "operation_summary": "Eliminar (desactivar) template",
    "operation_description": "Desactiva un template de prompt. No se elimina físicamente de la base de datos.",
    "tags": ["Templates IA"],
    "manual_parameters": [
        openapi.Parameter(
            'nombre_etiqueta',
            openapi.IN_PATH,
            description="Nombre de la etiqueta del template a eliminar",
            type=openapi.TYPE_STRING,
            required=True
        )
    ],
    "responses": {
        200: openapi.Response(
            description="Template eliminado exitosamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "message": openapi.Schema(type=openapi.TYPE_STRING)
                }
            )
        ),
        404: openapi.Response(description="Template no encontrado")
    }
}

crear_multiples_templates_doc = {
    "operation_summary": "Crear múltiples templates a la vez",
    "operation_description": """
    Crea o actualiza múltiples templates de prompts en una sola operación.
    
    Útil para inicializar o actualizar varios templates simultáneamente.
    """,
    "tags": ["Templates IA"],
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "templates": openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "nombre_etiqueta": openapi.Schema(type=openapi.TYPE_STRING),
                        "prompt_template": openapi.Schema(type=openapi.TYPE_STRING),
                        "descripcion": openapi.Schema(type=openapi.TYPE_STRING)
                    },
                    required=["nombre_etiqueta", "prompt_template"]
                )
            )
        },
        required=["templates"],
        example={
            "templates": [
                {
                    "nombre_etiqueta": "analisis_creditos",
                    "prompt_template": "Analiza los créditos: {datos}",
                    "descripcion": "Validación de créditos académicos"
                },
                {
                    "nombre_etiqueta": "revision_contenido",
                    "prompt_template": "Revisa el contenido: {datos}",
                    "descripcion": "Revisión de contenidos programáticos"
                }
            ]
        }
    ),
    "responses": {
        201: openapi.Response(
            description="Templates creados exitosamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "message": openapi.Schema(type=openapi.TYPE_STRING),
                    "created": openapi.Schema(type=openapi.TYPE_INTEGER),
                    "templates": openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Schema(type=openapi.TYPE_OBJECT)
                    )
                }
            )
        ),
        400: openapi.Response(description="Datos inválidos")
    }
}