from drf_yasg import openapi

formulario_biblioteca_example = {
    "llave_maestra": "LLAVE-5BE573CF",
    "etiquetas_dinamicas": {
        "variables": {
            "listadolibros": [
                {
                    "item": "1",
                    "año_libro": "2021",
                    "nombre_autor": "Project Management Institute",
                    "nombre_libro": "Guía de los Fundamentos para la Dirección de Proyectos (Guía del PMBOK)",
                    "formato_libro": "Físico"
                },
                {
                    "item": "2",
                    "año_libro": "2022",
                    "nombre_autor": "García Martínez, Juan",
                    "nombre_libro": "Gestión de Proyectos con Microsoft Project",
                    "formato_libro": "Digital"
                },
                {
                    "item": "3",
                    "año_libro": "2020",
                    "nombre_autor": "Perea Rojas-Marcos, Manuel",
                    "nombre_libro": "Dirección y Gestión de Proyectos",
                    "formato_libro": "Físico"
                },
                {
                    "item": "4",
                    "año_libro": "2023",
                    "nombre_autor": "Palacio, Juan",
                    "nombre_libro": "Gestión Ágil de Proyectos: SCRUM",
                    "formato_libro": "Digital"
                },
                {
                    "item": "5",
                    "año_libro": "2021",
                    "nombre_autor": "Chapman, Chris & Ward, Stephen",
                    "nombre_libro": "Gestión de Riesgos en Proyectos",
                    "formato_libro": "Físico"
                }
            ],
            "nombre_de_programa": "Especialización en Gestión de Proyectos",
            "inventario_software": [
                {
                    "asignatura_software": "Fundamentos de Gestión de Proyectos",
                    "descr_educativosoft": "Software especializado para la planificación, seguimiento y control de proyectos...",
                    "nombre_medioseducativossoft": "Microsoft Project Professional"
                },
                {
                    "asignatura_software": "Gestión del Tiempo",
                    "descr_educativosoft": "Herramienta robusta de gestión de proyectos empresariales...",
                    "nombre_medioseducativossoft": "Primavera P6"
                },
                {
                    "asignatura_software": "Gestión de Costos",
                    "descr_educativosoft": "Módulo de SAP para la gestión integrada de proyectos...",
                    "nombre_medioseducativossoft": "SAP Project System"
                },
                {
                    "asignatura_software": "Gestión de Comunicaciones",
                    "descr_educativosoft": "Plataforma colaborativa basada en tableros Kanban...",
                    "nombre_medioseducativossoft": "Trello"
                },
                {
                    "asignatura_software": "Gestión de Riesgos",
                    "descr_educativosoft": "Software de análisis de riesgos mediante simulación Monte Carlo...",
                    "nombre_medioseducativossoft": "@Risk"
                }
            ],
            "inventario_laboratorio": [
                {
                    "descr_educativolabora": "Espacio equipado con simuladores de negocios...",
                    "asignatura_laboratorio": "Planeación Estratégica",
                    "nombre_medioseducativoslabora": "Laboratorio de Simulación Empresarial"
                },
                {
                    "descr_educativolabora": "Laboratorio con software estadístico (Minitab, SPSS)...",
                    "asignatura_laboratorio": "Gestión de la Calidad",
                    "nombre_medioseducativoslabora": "Laboratorio de Análisis de Datos"
                },
                {
                    "descr_educativolabora": "Espacio colaborativo equipado con herramientas tecnológicas...",
                    "asignatura_laboratorio": "Trabajo de Grado",
                    "nombre_medioseducativoslabora": "Sala de Proyectos"
                }
            ],
            "proyección_financiera": [
                {
                    "periodo_1finan": "$3.000.000",
                    "periodo_2finan": "$3.500.000",
                    "periodo_3finan": "$4.000.000",
                    "periodo_4finan": "$4.500.000",
                    "periodo_5finan": "$5.000.000",
                    "periodo_6finan": "$5.500.000",
                    "periodo_7finan": "$6.000.000",
                    "Formato_proyeccionfinan": "Libros físicos"
                },
                {
                    "periodo_1finan": "$8.000.000",
                    "periodo_2finan": "$9.000.000",
                    "periodo_3finan": "$10.000.000",
                    "periodo_4finan": "$11.000.000",
                    "periodo_5finan": "$12.000.000",
                    "periodo_6finan": "$13.000.000",
                    "periodo_7finan": "$14.000.000",
                    "Formato_proyeccionfinan": "Libros digitales"
                },
                {
                    "periodo_1finan": "$15.000.000",
                    "periodo_2finan": "$16.500.000",
                    "periodo_3finan": "$18.000.000",
                    "periodo_4finan": "$19.500.000",
                    "periodo_5finan": "$21.000.000",
                    "periodo_6finan": "$22.500.000",
                    "periodo_7finan": "$24.000.000",
                    "Formato_proyeccionfinan": "Bases de datos especializadas"
                },
                {
                    "periodo_1finan": "$5.000.000",
                    "periodo_2finan": "$5.500.000",
                    "periodo_3finan": "$6.000.000",
                    "periodo_4finan": "$6.500.000",
                    "periodo_5finan": "$7.000.000",
                    "periodo_6finan": "$7.500.000",
                    "periodo_7finan": "$8.000.000",
                    "Formato_proyeccionfinan": "Revistas académicas"
                },
                {
                    "periodo_1finan": "$25.000.000",
                    "periodo_2finan": "$27.000.000",
                    "periodo_3finan": "$29.000.000",
                    "periodo_4finan": "$31.000.000",
                    "periodo_5finan": "$33.000.000",
                    "periodo_6finan": "$35.000.000",
                    "periodo_7finan": "$37.000.000",
                    "Formato_proyeccionfinan": "Software especializado"
                },
                {
                    "periodo_1finan": "$20.000.000",
                    "periodo_2finan": "$22.000.000",
                    "periodo_3finan": "$24.000.000",
                    "periodo_4finan": "$26.000.000",
                    "periodo_5finan": "$28.000.000",
                    "periodo_6finan": "$30.000.000",
                    "periodo_7finan": "$32.000.000",
                    "Formato_proyeccionfinan": "Equipos y tecnología"
                },
                {
                    "periodo_1finan": "$76.000.000",
                    "periodo_2finan": "$83.500.000",
                    "periodo_3finan": "$91.000.000",
                    "periodo_4finan": "$98.500.000",
                    "periodo_5finan": "$106.000.000",
                    "periodo_6finan": "$114.000.000",
                    "periodo_7finan": "$121.000.000",
                    "Formato_proyeccionfinan": "Total inversión"
                }
            ],
            "recursos_bibliograficos": [
                {
                    "periodo_1": "15",
                    "periodo_2": "20",
                    "periodo_3": "25",
                    "periodo_4": "30",
                    "periodo_5": "35",
                    "periodo_6": "40",
                    "periodo_7": "45",
                    "descr_formatobibli": "Libros físicos",
                    "enlace_bibliografico": "https://biblioteca.cun.edu.co/libros-fisicos"
                },
                {
                    "periodo_1": "50",
                    "periodo_2": "75",
                    "periodo_3": "100",
                    "periodo_4": "125",
                    "periodo_5": "150",
                    "periodo_6": "175",
                    "periodo_7": "200",
                    "descr_formatobibli": "Libros digitales",
                    "enlace_bibliografico": "https://biblioteca.cun.edu.co/libros-digitales"
                },
                {
                    "periodo_1": "3",
                    "periodo_2": "4",
                    "periodo_3": "5",
                    "periodo_4": "6",
                    "periodo_5": "7",
                    "periodo_6": "8",
                    "periodo_7": "9",
                    "descr_formatobibli": "Bases de datos especializadas",
                    "enlace_bibliografico": "https://biblioteca.cun.edu.co/bases-datos"
                },
                {
                    "periodo_1": "10",
                    "periodo_2": "12",
                    "periodo_3": "15",
                    "periodo_4": "18",
                    "periodo_5": "20",
                    "periodo_6": "22",
                    "periodo_7": "25",
                    "descr_formatobibli": "Revistas académicas",
                    "enlace_bibliografico": "https://biblioteca.cun.edu.co/revistas"
                },
                {
                    "periodo_1": "5",
                    "periodo_2": "6",
                    "periodo_3": "7",
                    "periodo_4": "8",
                    "periodo_5": "9",
                    "periodo_6": "10",
                    "periodo_7": "11",
                    "descr_formatobibli": "Software especializado",
                    "enlace_bibliografico": "https://software.cun.edu.co/licencias"
                }
            ]
        }
    }
}

crear_biblioteca_doc = {
    "operation_summary": "Crear recursos bibliográficos del programa",
    "operation_description": "Registrar los recursos bibliográficos, medios educativos y proyecciones financieras de biblioteca para un programa de posgrado.",
    "tags": ["Biblioteca"],
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        example=formulario_biblioteca_example
    ),
    "responses": {
        201: openapi.Response(
            description="Recursos bibliográficos creados exitosamente"
        ),
        400: openapi.Response(
            description="Error de validación"
        )
    }
}

obtener_biblioteca_doc = {
    "operation_summary": "Obtener recursos bibliográficos del programa",
    "operation_description": "Devuelve los recursos bibliográficos completos de un programa de posgrado incluyendo listado de libros, software, laboratorios y proyecciones.",
    "tags": ["Biblioteca"],
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
            description="Recursos bibliográficos obtenidos exitosamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example=formulario_biblioteca_example
            )
        ),
        404: openapi.Response(
            description="Recursos bibliográficos no encontrados",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={"error": "Recursos bibliográficos no encontrados"}
            )
        )
    }
}

actualizar_biblioteca_doc = {
    "operation_summary": "Actualizar parcialmente recursos bibliográficos",
    "operation_description": "Permite actualizar uno o varios elementos de los recursos bibliográficos del programa. Se pueden actualizar libros específicos, software, laboratorios, proyecciones financieras o recursos bibliográficos.",
    "tags": ["Biblioteca"],
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
        description="Enviar solo los elementos que se desean actualizar. Se pueden modificar listados completos o elementos individuales.",
        examples={
            "actualizar_libros": {
                "summary": "Agregar o actualizar libros del listado",
                "value": {
                    "etiquetas_dinamicas": {
                        "variables": {
                            "listadolibros": [
                                {
                                    "item": "1",
                                    "año_libro": "2024",
                                    "nombre_autor": "Kerzner, Harold",
                                    "nombre_libro": "Project Management: A Systems Approach to Planning",
                                    "formato_libro": "Digital"
                                },
                                {
                                    "item": "6",
                                    "año_libro": "2023",
                                    "nombre_autor": "Mulcahy, Rita",
                                    "nombre_libro": "PMP Exam Prep",
                                    "formato_libro": "Físico"
                                }
                            ]
                        }
                    }
                }
            },
            "actualizar_software": {
                "summary": "Actualizar inventario de software",
                "value": {
                    "etiquetas_dinamicas": {
                        "variables": {
                            "inventario_software": [
                                {
                                    "asignatura_software": "Gestión Ágil",
                                    "descr_educativosoft": "Plataforma para gestión ágil de proyectos con metodología Scrum",
                                    "nombre_medioseducativossoft": "Jira Software"
                                },
                                {
                                    "asignatura_software": "Colaboración en Proyectos",
                                    "descr_educativosoft": "Herramienta de colaboración y gestión de tareas en equipo",
                                    "nombre_medioseducativossoft": "Asana"
                                }
                            ]
                        }
                    }
                }
            },
            "actualizar_proyeccion_financiera": {
                "summary": "Actualizar proyección financiera específica",
                "value": {
                    "etiquetas_dinamicas": {
                        "variables": {
                            "proyección_financiera": [
                                {
                                    "periodo_1finan": "$10.000.000",
                                    "periodo_2finan": "$11.000.000",
                                    "periodo_3finan": "$12.000.000",
                                    "periodo_4finan": "$13.000.000",
                                    "periodo_5finan": "$14.000.000",
                                    "periodo_6finan": "$15.000.000",
                                    "periodo_7finan": "$16.000.000",
                                    "Formato_proyeccionfinan": "Libros digitales"
                                }
                            ]
                        }
                    }
                }
            },
            "actualizar_recursos_bibliograficos": {
                "summary": "Actualizar recursos bibliográficos",
                "value": {
                    "etiquetas_dinamicas": {
                        "variables": {
                            "recursos_bibliograficos": [
                                {
                                    "periodo_1": "20",
                                    "periodo_2": "25",
                                    "periodo_3": "30",
                                    "periodo_4": "35",
                                    "periodo_5": "40",
                                    "periodo_6": "45",
                                    "periodo_7": "50",
                                    "descr_formatobibli": "Libros físicos",
                                    "enlace_bibliografico": "https://biblioteca.cun.edu.co/libros-fisicos"
                                },
                                {
                                    "periodo_1": "5",
                                    "periodo_2": "6",
                                    "periodo_3": "7",
                                    "periodo_4": "8",
                                    "periodo_5": "10",
                                    "periodo_6": "12",
                                    "periodo_7": "15",
                                    "descr_formatobibli": "Bases de datos especializadas",
                                    "enlace_bibliografico": "https://biblioteca.cun.edu.co/bases-datos"
                                }
                            ]
                        }
                    }
                }
            },
            "actualizar_multiple": {
                "summary": "Actualizar múltiples secciones simultáneamente",
                "value": {
                    "etiquetas_dinamicas": {
                        "variables": {
                            "nombre_de_programa": "Especialización en Gestión Avanzada de Proyectos",
                            "listadolibros": [
                                {
                                    "item": "1",
                                    "año_libro": "2024",
                                    "nombre_autor": "Nuevo Autor",
                                    "nombre_libro": "Nuevo Libro",
                                    "formato_libro": "Digital"
                                }
                            ],
                            "inventario_laboratorio": [
                                {
                                    "descr_educativolabora": "Nuevo laboratorio equipado con tecnología de punta",
                                    "asignatura_laboratorio": "Innovación en Proyectos",
                                    "nombre_medioseducativoslabora": "Laboratorio de Innovación"
                                }
                            ]
                        }
                    }
                }
            }
        }
    ),
    "responses": {
        200: openapi.Response(
            description="Recursos bibliográficos actualizados exitosamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={
                    "message": "Recursos bibliográficos actualizados exitosamente",
                    "llave_id": "LLAVE-5BE573CF",
                    "secciones_actualizadas": [
                        "listadolibros",
                        "inventario_software",
                        "proyección_financiera"
                    ],
                    "elementos_modificados": {
                        "libros": 2,
                        "software": 2,
                        "proyecciones": 1
                    }
                }
            )
        ),
        400: openapi.Response(
            description="Error de validación",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={
                    "error": "Datos inválidos",
                    "detalles": "El formato del libro debe ser 'Físico' o 'Digital'"
                }
            )
        ),
        404: openapi.Response(
            description="Recursos bibliográficos no encontrados",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={"error": "Recursos bibliográficos no encontrados con el llave_id proporcionado"}
            )
        )
    }
}