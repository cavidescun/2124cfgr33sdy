from drf_yasg import openapi

formulario_posgrado_example = {
  "llave_maestra": "LLAVE-5BE573CF",
  "etiquetas_dinamicas": {
    "variables": {
      "busqueda_snies": 2123,
      "snies": "20245896",
      "nivel": "Posgrado",
      "ciclo": "Especialización",
      "nombre_de_programa_tp": ",Arquitectura",
      "nombre_de_programa_tg": ",Arquitectura",
      "nombre_de_programa_pro": ",Arquitectura",
      "nombre_de_programa": ",Arquitectura",
      "año_inicial": "2025",
      "año_final": "2030",

  "tabla_financiera": {
    "columnas": [
      "año 1 A",
      "año 1 B",
      "año 2 A",
      "año 2 B",
      "año 3 A",
      "año 3 B",
      "año 4 A",
      "año 4 B",
      "año 5 A",
      "año 5 B",
      "año 6 A",
      "año 6 B",
      "año 7 A",
      "año 7 B"
    ],
    "filas": [
      {
        "categoria": "Bienestar",
        "año_1_A": "",
        "año_1_B": "",
        "año_2_A": "",
        "año_2_B": "",
        "año_3_A": "",
        "año_3_B": "",
        "año_4_A": "",
        "año_4_B": "",
        "año_5_A": "",
        "año_5_B": "",
        "año_6_A": "",
        "año_6_B": "",
        "año_7_A": "",
        "año_7_B": ""
        
      },
      {
        "categoria": "Infraestructura",
        "año_1_A": "",
        "año_1_B": "",
        "año_2_A": "",
        "año_2_B": "",
        "año_3_A": "",
        "año_3_B": "",
        "año_4_A": "",
        "año_4_B": "",
        "año_5_A": "",
        "año_5_B": "",
        "año_6_A": "",
        "año_6_B": "",
        "año_7_A": "",
        "año_7_B": ""
      },
      {
        "categoria": "Investigación",
        "año_1_A": "",
        "año_1_B": "",
        "año_2_A": "",
        "año_2_B": "",
        "año_3_A": "",
        "año_3_B": "",
        "año_4_A": "",
        "año_4_B": "",
        "año_5_A": "",
        "año_5_B": "",
        "año_6_A": "",
        "año_6_B": "",
        "año_7_A": "",
        "año_7_B": ""
      },
      {
        "categoria": "Medios Educativos",
        "año_1_A": "",
        "año_1_B": "",
        "año_2_A": "",
        "año_2_B": "",
        "año_3_A": "",
        "año_3_B": "",
        "año_4_A": "",
        "año_4_B": "",
        "año_5_A": "",
        "año_5_B": "",
        "año_6_A": "",
        "año_6_B": "",
        "año_7_A": "",
        "año_7_B": ""
      },
      {
        "categoria": "Proyección Social",
        "año_1_A": "",
        "año_1_B": "",
        "año_2_A": "",
        "año_2_B": "",
        "año_3_A": "",
        "año_3_B": "",
        "año_4_A": "",
        "año_4_B": "",
        "año_5_A": "",
        "año_5_B": "",
        "año_6_A": "",
        "año_6_B": "",
        "año_7_A": "",
        "año_7_B": ""
      },
      {
        "categoria": "Proyección Estudiantes",
        "año_1_A": "",
        "año_1_B": "",
        "año_2_A": "",
        "año_2_B": "",
        "año_3_A": "",
        "año_3_B": "",
        "año_4_A": "",
        "año_4_B": "",
        "año_5_A": "",
        "año_5_B": "",
        "año_6_A": "",
        "año_6_B": "",
        "año_7_A": "",
        "año_7_B": ""
      }
    ]
  }   
    }
  }
}

crear_proyeccionFinanciera_doc = {
    "operation_summary": "crear una proyección financiera",
    "operation_description": " crea una proyección financiera en la estructura JSON.",
    "tags": ["Proyeccion Financiera"],
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        example=formulario_posgrado_example
    ),
    "responses": {
        200: openapi.Response(
            description="Proyección financiera creada exitosamente",
        ),
        400: openapi.Response(
            description="Error de validacion"
        )
    }
}

obtener_proyeccionFinanciera_doc = {
    "operation_summary": "Obtener una proyección financiera",
    "operation_description": " Obtener una proyección financiera en la estructura JSON.",
    "tags": ["Proyeccion Financiera"],
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
            description="Proyección financiera obtenida exitosamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example=formulario_posgrado_example
            )
        ),
        404: openapi.Response(
            description="Error de validacion",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={"error": "Acuerdo no encontrado"}
            )
        )
    }
}


actualizar_proyeccionFinanciera_doc = {
    "operation_summary": "Actualizar parcialmente una proyección financiera",
    "operation_description": "Permite actualizar uno o varios campos de una proyección financiera existente. Se pueden actualizar campos individuales, años específicos, o filas completas de la tabla financiera.",
    "tags": ["Proyeccion Financiera"],
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
        description="Enviar solo los campos que se desean actualizar. Se puede actualizar información general, años, o datos específicos de la tabla financiera.",
        examples={
            "actualizar_años": {
                "summary": "Actualizar años del programa",
                "value": {
                    "etiquetas_dinamicas": {
                        "variables": {
                            "año_inicial": "2026",
                            "año_final": "2032"
                        }
                    }
                }
            },
            "actualizar_fila_completa": {
                "summary": "Actualizar una fila completa de la tabla",
                "value": {
                    "etiquetas_dinamicas": {
                        "variables": {
                            "tabla_financiera": {
                                "filas": [
                                    {
                                        "categoria": "Bienestar",
                                        "año_1_A": "5000000",
                                        "año_1_B": "5200000",
                                        "año_2_A": "5500000",
                                        "año_2_B": "5800000",
                                        "año_3_A": "6000000",
                                        "año_3_B": "6300000",
                                        "año_4_A": "6500000",
                                        "año_4_B": "6800000",
                                        "año_5_A": "7000000",
                                        "año_5_B": "7300000",
                                        "año_6_A": "7500000",
                                        "año_6_B": "7800000",
                                        "año_7_A": "8000000",
                                        "año_7_B": "8300000"
                                    }
                                ]
                            }
                        }
                    }
                }
            },
            "actualizar_valores_especificos": {
                "summary": "Actualizar valores específicos de categorías",
                "value": {
                    "etiquetas_dinamicas": {
                        "variables": {
                            "tabla_financiera": {
                                "filas": [
                                    {
                                        "categoria": "Investigación",
                                        "año_1_A": "3000000",
                                        "año_1_B": "3200000"
                                    },
                                    {
                                        "categoria": "Infraestructura",
                                        "año_2_A": "8000000",
                                        "año_2_B": "8500000"
                                    }
                                ]
                            }
                        }
                    }
                }
            }
        }
    ),
    "responses": {
        200: openapi.Response(
            description="Proyección financiera actualizada exitosamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={
                    "message": "Proyección financiera actualizada exitosamente",
                    "llave_id": "LLAVE-5BE573CF",
                    "campos_actualizados": [
                        "año_inicial",
                        "año_final",
                        "tabla_financiera.filas"
                    ],
                    "categorias_actualizadas": ["Bienestar", "Investigación"]
                }
            )
        ),
        400: openapi.Response(
            description="Error de validación",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={
                    "error": "Datos inválidos",
                    "detalles": "La categoría 'Bienestar' no existe en la tabla financiera"
                }
            )
        ),
        404: openapi.Response(
            description="Proyección financiera no encontrada",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={"error": "Proyección financiera no encontrada con el llave_id proporcionado"}
            )
        )
    }
}