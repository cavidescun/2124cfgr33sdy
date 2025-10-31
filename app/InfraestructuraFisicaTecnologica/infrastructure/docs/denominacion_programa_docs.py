from drf_yasg import openapi

crear_programa_doc = {
    "operation_description": "Crea una nueva infraestructura física tecnológica con etiquetas dinámicas y configuración de gráficos.",
    "tags": ["Infraestructura Fisica Tecnologica"],
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
                        "llave_maestra": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Llave maestra numérica para identificar el programa.",
                example="12345",
            ),
            "etiquetas_dinamicas": openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "tablas": openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "caracteristicas": openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                items=openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        "caracteristica": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Nombre de la característica",
                                        ),
                                        "total": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Total de la característica",
                                        ),
                                    },
                                ),
                                description="Lista de características",
                            ),
                            "items": openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                items=openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        "item": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Nombre del item",
                                        ),
                                        "t_2024": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Valor actual",
                                        ),
                                        "t_2025": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Proyección 2025",
                                        ),
                                        "t_2026": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Proyección 2026",
                                        ),
                                        "t_2027": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Proyección 2027",
                                        ),
                                        "t_2028": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Proyección 2028",
                                        ),
                                        "t_2029": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Proyección 2029",
                                        ),
                                        "t_2030": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Proyección 2030",
                                        ),
                                    },
                                ),
                                description="Lista de items con proyecciones",
                            ),
                            "formatos": openapi.Schema(
                                type=openapi.TYPE_ARRAY,
                                items=openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        "formato": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Nombre del formato",
                                        ),
                                        "t_2024": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Proyección 2024",
                                        ),
                                        "t_2025": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Proyección 2025",
                                        ),
                                        "t_2026": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Proyección 2026",
                                        ),
                                        "t_2027": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Proyección 2027",
                                        ),
                                        "t_2028": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Proyección 2028",
                                        ),
                                        "t_2029": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Proyección 2029",
                                        ),
                                        "t_2030": openapi.Schema(
                                            type=openapi.TYPE_STRING,
                                            description="Proyección 2030",
                                        ),
                                    },
                                ),
                                description="Lista de formatos con proyecciones anuales",
                            ),
                        },
                        description="Tablas con datos de características, items y formatos",
                    ),
                    "_graficos_config": openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "formatos": openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    "tipo": openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                        description="Tipo de gráfico",
                                        enum=[
                                            "barras",
                                            "barras_agrupadas",
                                            "lineas",
                                            "pastel",
                                        ],
                                    ),
                                    "titulo": openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                        description="Título del gráfico",
                                    ),
                                    "filename": openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                        description="Nombre del archivo de salida",
                                    ),
                                    "categorias_campo": openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                        description="Campo que contiene las categorías",
                                    ),
                                    "valores_campos": openapi.Schema(
                                        type=openapi.TYPE_ARRAY,
                                        items=openapi.Schema(type=openapi.TYPE_STRING),
                                        description="Lista de campos con valores (para gráficos agrupados)",
                                    ),
                                    "valores_campo": openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                        description="Campo con valores (para gráficos simples)",
                                    ),
                                    "color": openapi.Schema(
                                        type=openapi.TYPE_STRING,
                                        description="Color del gráfico",
                                    ),
                                },
                                description="Configuración del gráfico de formatos",
                            )
                        },
                        description="Configuración de gráficos",
                    ),
                    "variables": openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "Modalidad_programa": openapi.Schema(
                                type=openapi.TYPE_STRING,
                                description="Modalidad del programa",
                            ),
                            "Regional_programa": openapi.Schema(
                                type=openapi.TYPE_STRING,
                                description="Regional del programa",
                            ),
                        },
                        description="Variables adicionales del programa",
                    ),
                },
                description="Etiquetas dinámicas con tablas y configuración",
            ),

        },
        required=["etiquetas_dinamicas", "llave_maestra"],
        example={
            "llave_maestra": 111,
            "etiquetas_dinamicas": {
                "tablas": {
                    "caracteristicas": [
                        {"caracteristica": "Queso", "total": "$5,000"},
                        {"caracteristica": "Leche", "total": "$3,000"},
                        {"caracteristica": "Mantequilla", "total": "$7,000"},
                    ],
                    "items": [
                        {
                            "item": "Queso",
                            "t_2024": "$5",
                            "t_2025": "1",
                            "t_2026": "21",
                            "t_2027": "1213",
                            "t_2028": "12323",
                            "t_2029": "1212",
                            "t_2030": "213",
                        },
                        {
                            "item": "Leche",
                            "t_2024": "$5",
                            "t_2025": "1",
                            "t_2026": "21",
                            "t_2027": "1213",
                            "t_2028": "12323",
                            "t_2029": "1212",
                            "t_2030": "213",
                        },
                        {
                            "item": "Mantequilla",
                            "t_2024": "$5",
                            "t_2025": "1",
                            "t_2026": "21",
                            "t_2027": "1213",
                            "t_2028": "12323",
                            "t_2029": "1212",
                            "t_2030": "213",
                        },
                    ],
                    "formatos": [
                        {
                            "formato": "Queso",
                            "t_2024": "1",
                            "t_2025": "1",
                            "t_2026": "1",
                            "t_2027": "1",
                            "t_2028": "1",
                            "t_2029": "1",
                            "t_2030": "1",
                        },
                        {
                            "formato": "Leche",
                            "t_2024": "1",
                            "t_2025": "1",
                            "t_2026": "1",
                            "t_2027": "1",
                            "t_2028": "1",
                            "t_2029": "1",
                            "t_2030": "1",
                        },
                        {
                            "formato": "PRUEBA",
                            "t_2024": "1",
                            "t_2025": "1",
                            "t_2026": "1",
                            "t_2027": "1",
                            "t_2028": "1",
                            "t_2029": "1",
                            "t_2030": "1",
                        },
                        {
                            "formato": "Mantequilla",
                            "t_2024": "1",
                            "t_2025": "1",
                            "t_2026": "1",
                            "t_2027": "1",
                            "t_2028": "1",
                            "t_2029": "1",
                            "t_2030": "1",
                        },
                    ],
                },
                "_graficos_config": {
                    "formatos": {
                        "tipo": "barras_agrupadas",
                        "titulo": "grafico_proyeccion_financiera_presencial",
                        "filename": "grafico_proyeccion_financiera_presencial.png",
                        "categorias_campo": "formato",
                        "valores_campos": [
                            "t_2024",
                            "t_2025",
                            "t_2026",
                            "t_2027",
                            "t_2028",
                            "t_2029",
                            "t_2030",
                        ],
                        "color": "steelblue",
                    }
                },
                "variables": {
                    "Modalidad_programa": "Presencial",
                    "Regional_programa": "Bogotá D.C.",
                },
            },
       
        },
    ),
    "responses": {
        201: openapi.Response(
            description="Programa creado exitosamente",
            examples={
                "application/json": {"message": "Programa creado exitosamente", "id": 1}
            },
        ),
        400: openapi.Response(
            description="Error de validación",
            examples={
                "application/json": {
                    "etiquetas_dinamicas": [
                        "El campo 'etiquetas_dinamicas' no puede estar vacío."
                    ],
                    "llave_maestra": ["Este campo es requerido."],
                }
            },
        ),
        500: openapi.Response(
            description="Error interno del servidor",
            examples={"application/json": {"error": "Error al procesar la solicitud"}},
        ),
    },
}
