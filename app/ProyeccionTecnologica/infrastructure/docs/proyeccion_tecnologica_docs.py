from drf_yasg import openapi

# Ejemplo actualizado para proyección tecnológica
formulario_tecnologia_example = {
    "llave_maestra": "LLAVE-5BE573CF",
    "etiquetas_dinamicas": {
        "variables": {
            "busqueda_snies": 2123,
            "snies": "20245896",
            "nivel": "Posgrado",
            "ciclo": "Especialización",
            "nombre_de_programa_tp": "Arquitectura",
            "nombre_de_programa_tg": "Arquitectura",
            "nombre_de_programa_pro": "Arquitectura",
            "nombre_de_programa": "Arquitectura",
            "año_inicial": "2025",
            "año_final": "2030",
            "tabla_tecnologica": {
                "columnas": [
                    "año 1", "año 2", "año 3", "año 4", "año 5", "año 6", "año 7"
                ],
                "filas": [
                    {
                        "categoria": "Equipos de Cómputo",
                        "año_1": "50",
                        "año_2": "60",
                        "año_3": "70",
                        "año_4": "80",
                        "año_5": "90",
                        "año_6": "100",
                        "año_7": "110"
                    },
                    {
                        "categoria": "Servidores",
                        "año_1": "2",
                        "año_2": "3",
                        "año_3": "4",
                        "año_4": "5",
                        "año_5": "6",
                        "año_6": "7",
                        "año_7": "8"
                    },
                    {
                        "categoria": "Licencias de Software",
                        "año_1": "50",
                        "año_2": "60",
                        "año_3": "70",
                        "año_4": "80",
                        "año_5": "90",
                        "año_6": "100",
                        "año_7": "110"
                    },
                    {
                        "categoria": "Equipos Audiovisuales",
                        "año_1": "15",
                        "año_2": "18",
                        "año_3": "20",
                        "año_4": "22",
                        "año_5": "25",
                        "año_6": "28",
                        "año_7": "30"
                    },
                    {
                        "categoria": "Impresoras y Escáneres",
                        "año_1": "10",
                        "año_2": "12",
                        "año_3": "14",
                        "año_4": "16",
                        "año_5": "18",
                        "año_6": "20",
                        "año_7": "22"
                    },
                    {
                        "categoria": "Equipos de Red",
                        "año_1": "8",
                        "año_2": "10",
                        "año_3": "12",
                        "año_4": "14",
                        "año_5": "16",
                        "año_6": "18",
                        "año_7": "20"
                    },
                    {
                        "categoria": "Tablets",
                        "año_1": "20",
                        "año_2": "25",
                        "año_3": "30",
                        "año_4": "35",
                        "año_5": "40",
                        "año_6": "45",
                        "año_7": "50"
                    },
                    {
                        "categoria": "Plataformas E-Learning",
                        "año_1": "1",
                        "año_2": "1",
                        "año_3": "2",
                        "año_4": "2",
                        "año_5": "2",
                        "año_6": "3",
                        "año_7": "3"
                    },
                    {
                        "categoria": "Almacenamiento en la Nube (GB)",
                        "año_1": "1000",
                        "año_2": "1500",
                        "año_3": "2000",
                        "año_4": "2500",
                        "año_5": "3000",
                        "año_6": "3500",
                        "año_7": "4000"
                    },
                    {
                        "categoria": "Software Especializado",
                        "año_1": "5",
                        "año_2": "6",
                        "año_3": "7",
                        "año_4": "8",
                        "año_5": "9",
                        "año_6": "10",
                        "año_7": "11"
                    }
                ]
            }
        }
    }
}

# Documentación para CREAR proyección tecnológica
crear_proyeccion_tecnologia_doc = {
    "operation_summary": "Crear una proyección de tecnología",
    "operation_description": "Crea una nueva proyección de recursos tecnológicos en la estructura JSON. Permite definir la evolución de equipos, software y recursos tecnológicos a lo largo de los años del programa.",
    "tags": ["Proyección Tecnológica"],
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description="Estructura completa de la proyección tecnológica con categorías y valores por año",
        example=formulario_tecnologia_example
    ),
    "responses": {
        200: openapi.Response(
            description="Proyección tecnológica creada exitosamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={
                    "message": "Proyección tecnológica creada exitosamente",
                    "llave_id": "LLAVE-5BE573CF",
                    "categorias_creadas": 10,
                    "años_proyectados": 7
                }
            )
        ),
        400: openapi.Response(
            description="Error de validación",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={
                    "error": "Datos inválidos",
                    "detalles": "El campo 'tabla_tecnologica' es requerido"
                }
            )
        )
    }
}

# Documentación para OBTENER proyección tecnológica
obtener_proyeccion_tecnologia_doc = {
    "operation_summary": "Obtener una proyección de tecnología",
    "operation_description": "Recupera una proyección tecnológica existente mediante su identificador único (llave_id).",
    "tags": ["Proyección Tecnológica"],
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
            description="Proyección tecnológica obtenida exitosamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example=formulario_tecnologia_example
            )
        ),
        404: openapi.Response(
            description="Proyección no encontrada",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={"error": "Proyección tecnológica no encontrada"}
            )
        )
    }
}

# Documentación para ACTUALIZAR proyección tecnológica
actualizar_proyeccion_tecnologia_doc = {
    "operation_summary": "Actualizar parcialmente una proyección de tecnología",
    "operation_description": "Permite actualizar uno o varios campos de una proyección tecnológica existente. Se pueden actualizar campos individuales, años específicos, o categorías completas de recursos tecnológicos.",
    "tags": ["Proyección Tecnológica"],
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
        description="Enviar solo los campos que se desean actualizar. Se puede actualizar información general, años, o datos específicos de las categorías tecnológicas.",
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
            "actualizar_equipos_computo": {
                "summary": "Actualizar proyección de equipos de cómputo",
                "value": {
                    "etiquetas_dinamicas": {
                        "variables": {
                            "tabla_tecnologica": {
                                "filas": [
                                    {
                                        "categoria": "Equipos de Cómputo",
                                        "año_1": "60",
                                        "año_2": "75",
                                        "año_3": "90",
                                        "año_4": "105",
                                        "año_5": "120",
                                        "año_6": "135",
                                        "año_7": "150"
                                    }
                                ]
                            }
                        }
                    }
                }
            },
            "actualizar_multiples_categorias": {
                "summary": "Actualizar múltiples categorías tecnológicas",
                "value": {
                    "etiquetas_dinamicas": {
                        "variables": {
                            "tabla_tecnologica": {
                                "filas": [
                                    {
                                        "categoria": "Equipos de Cómputo",
                                        "año_1": "60",
                                        "año_2": "75"
                                    },
                                    {
                                        "categoria": "Licencias de Software",
                                        "año_1": "60",
                                        "año_2": "75"
                                    },
                                    {
                                        "categoria": "Servidores",
                                        "año_3": "5",
                                        "año_4": "6"
                                    },
                                    {
                                        "categoria": "Almacenamiento en la Nube (GB)",
                                        "año_1": "2000",
                                        "año_2": "2500",
                                        "año_3": "3000"
                                    }
                                ]
                            }
                        }
                    }
                }
            },
            "actualizar_infraestructura_año_especifico": {
                "summary": "Actualizar toda la infraestructura tecnológica de un año",
                "value": {
                    "etiquetas_dinamicas": {
                        "variables": {
                            "tabla_tecnologica": {
                                "filas": [
                                    {"categoria": "Equipos de Cómputo", "año_3": "80"},
                                    {"categoria": "Servidores", "año_3": "5"},
                                    {"categoria": "Licencias de Software", "año_3": "80"},
                                    {"categoria": "Equipos Audiovisuales", "año_3": "22"},
                                    {"categoria": "Impresoras y Escáneres", "año_3": "16"},
                                    {"categoria": "Equipos de Red", "año_3": "14"},
                                    {"categoria": "Tablets", "año_3": "35"},
                                    {"categoria": "Plataformas E-Learning", "año_3": "2"},
                                    {"categoria": "Almacenamiento en la Nube (GB)", "año_3": "2500"},
                                    {"categoria": "Software Especializado", "año_3": "8"}
                                ]
                            }
                        }
                    }
                }
            },
            "actualizar_software_y_plataformas": {
                "summary": "Actualizar solo software y plataformas digitales",
                "value": {
                    "etiquetas_dinamicas": {
                        "variables": {
                            "tabla_tecnologica": {
                                "filas": [
                                    {
                                        "categoria": "Licencias de Software",
                                        "año_1": "75",
                                        "año_2": "90",
                                        "año_3": "105"
                                    },
                                    {
                                        "categoria": "Plataformas E-Learning",
                                        "año_1": "2",
                                        "año_2": "2",
                                        "año_3": "3"
                                    },
                                    {
                                        "categoria": "Software Especializado",
                                        "año_1": "8",
                                        "año_2": "10",
                                        "año_3": "12"
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
            description="Proyección tecnológica actualizada exitosamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={
                    "message": "Proyección tecnológica actualizada exitosamente",
                    "llave_id": "LLAVE-5BE573CF",
                    "campos_actualizados": [
                        "tabla_tecnologica.filas"
                    ],
                    "categorias_actualizadas": [
                        "Equipos de Cómputo",
                        "Licencias de Software",
                        "Servidores",
                        "Almacenamiento en la Nube (GB)"
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
                    "detalles": "La categoría 'Equipos de Cómputo' requiere valores numéricos"
                }
            )
        ),
        404: openapi.Response(
            description="Proyección no encontrada",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={
                    "error": "Proyección tecnológica no encontrada con el llave_id proporcionado"
                }
            )
        )
    }
}