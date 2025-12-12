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
      "año 1",
      "año 2",
      "año 3",
      "año 4",
      "año 5",
      "año 6",
      "año 7"
    ],
    "filas": [
      {
        "categoria": "Proyección Alumnos",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
        
      },
      {
        "categoria": "Proyección # Alumnos",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Capacidad General por Jornada",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Salones",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Capacidad Salones",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Salas De Sistemas",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Capacidad Salas De Sistemas",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Talleres O Laboratorios",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Capacidad Talleres O Laboratorios",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Zonas De Bienestar",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Capacidad Zonas De Bienestar",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Sala De Profesores",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Capacidad Sala De Profesores",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
            {
        "categoria": "Biblioteca",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Capacidad Biblioteca",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Auditorio",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Capacidad Auditorio",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Oficinas",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Capacidad Oficinas",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Baños",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      },
      {
        "categoria": "Capacidad Baños",
        "año_1": "",
        "año_2": "",
        "año_3": "",
        "año_4": "",
        "año_5": "",
        "año_6": "",
        "año_7": ""
      }
    ]
  }   
    }
  }
}

crear_proyeccion_infrac_tecnol_doc = {
    "operation_summary": "crear una proyección de infraestructura tecnológica",
    "operation_description": " crea una proyección en la estructura JSON.",
    "tags": ["Proyección Infraestructura y Tecnológica"],
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        example=formulario_posgrado_example
    ),
    "responses": {
        200: openapi.Response(
            description="Proyección creada exitosamente",
        ),
        400: openapi.Response(
            description="Error de validacion"
        )
    }
}

obtener_proyeccion_infrac_tecnol_doc = {
    "operation_summary": "Obtener una proyección de infraestructura tecnológica",
    "operation_description": " Obtener una proyección en la estructura JSON.",
    "tags": ["Proyección Infraestructura y Tecnológica"],
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
            description="Proyección obtenida exitosamente",
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


actualizar_proyeccion_infrac_tecnol_doc = {
    "operation_summary": "Actualizar parcialmente una proyección de infraestructura y tecnológica",
    "operation_description": "Permite actualizar uno o varios campos de una proyección de infraestructura existente. Se pueden actualizar campos individuales, años específicos, o categorías completas de la tabla.",
    "tags": ["Proyección Infraestructura y Tecnológica"],
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
        description="Enviar solo los campos que se desean actualizar. Se puede actualizar información general, años, o datos específicos de las categorías de infraestructura.",
        examples={
            "actualizar_años": {
                "summary": "Actualizar período del programa",
                "value": {
                    "etiquetas_dinamicas": {
                        "variables": {
                            "año_inicial": "2026",
                            "año_final": "2032"
                        }
                    }
                }
            },
            "actualizar_categoria_completa": {
                "summary": "Actualizar una categoría completa",
                "value": {
                    "etiquetas_dinamicas": {
                        "variables": {
                            "tabla_financiera": {
                                "filas": [
                                    {
                                        "categoria": "Salones",
                                        "año_1": "15",
                                        "año_2": "18",
                                        "año_3": "20",
                                        "año_4": "22",
                                        "año_5": "25",
                                        "año_6": "28",
                                        "año_7": "30"
                                    },
                                    {
                                        "categoria": "Capacidad Salones",
                                        "año_1": "450",
                                        "año_2": "540",
                                        "año_3": "600",
                                        "año_4": "660",
                                        "año_5": "750",
                                        "año_6": "840",
                                        "año_7": "900"
                                    }
                                ]
                            }
                        }
                    }
                }
            },
            "actualizar_multiples_categorias": {
                "summary": "Actualizar múltiples categorías específicas",
                "value": {
                    "etiquetas_dinamicas": {
                        "variables": {
                            "tabla_financiera": {
                                "filas": [
                                    {
                                        "categoria": "Proyección Alumnos",
                                        "año_1": "100",
                                        "año_2": "150"
                                    },
                                    {
                                        "categoria": "Biblioteca",
                                        "año_1": "2",
                                        "año_2": "2"
                                    },
                                    {
                                        "categoria": "Capacidad Biblioteca",
                                        "año_1": "200",
                                        "año_2": "200"
                                    },
                                    {
                                        "categoria": "Salas De Sistemas",
                                        "año_3": "5",
                                        "año_4": "6"
                                    }
                                ]
                            }
                        }
                    }
                }
            },
            "actualizar_infraestructura_completa": {
                "summary": "Actualizar toda la infraestructura de un año específico",
                "value": {
                    "etiquetas_dinamicas": {
                        "variables": {
                            "tabla_financiera": {
                                "filas": [
                                    {
                                        "categoria": "Salones",
                                        "año_1": "20"
                                    },
                                    {
                                        "categoria": "Capacidad Salones",
                                        "año_1": "600"
                                    },
                                    {
                                        "categoria": "Salas De Sistemas",
                                        "año_1": "4"
                                    },
                                    {
                                        "categoria": "Capacidad Salas De Sistemas",
                                        "año_1": "120"
                                    },
                                    {
                                        "categoria": "Talleres O Laboratorios",
                                        "año_1": "8"
                                    },
                                    {
                                        "categoria": "Capacidad Talleres O Laboratorios",
                                        "año_1": "240"
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
            description="Proyección de infraestructura actualizada exitosamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={
                    "message": "Proyección de infraestructura actualizada exitosamente",
                    "llave_id": "LLAVE-5BE573CF",
                    "campos_actualizados": [
                        "año_inicial",
                        "tabla_financiera.filas"
                    ],
                    "categorias_actualizadas": [
                        "Salones",
                        "Capacidad Salones",
                        "Biblioteca",
                        "Salas De Sistemas"
                    ],
                    "años_modificados": ["año_1", "año_2", "año_3"]
                }
            )
        ),
        400: openapi.Response(
            description="Error de validación",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={
                    "error": "Datos inválidos",
                    "detalles": "La categoría 'Salones' requiere valores numéricos"
                }
            )
        ),
        404: openapi.Response(
            description="Proyección no encontrada",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={"error": "Proyección de infraestructura no encontrada con el llave_id proporcionado"}
            )
        )
    }
}