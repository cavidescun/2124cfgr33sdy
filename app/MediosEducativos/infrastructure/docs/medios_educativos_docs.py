from drf_yasg import openapi
from ..serializers import MediosEducativosSerializer

etiquetas_dinamicas_example = {
  "variables": {
    "nombre_de_programa": "Especialización en Gestión de Proyectos",
    "listadolibros": [
      {
        "item": "1",
        "nombre_libro": "Guía de los Fundamentos para la Dirección de Proyectos (Guía del PMBOK)",
        "nombre_autor": "Project Management Institute",
        "año_libro": "2021",
        "formato_libro": "Físico"
      },
      {
        "item": "2",
        "nombre_libro": "Gestión de Proyectos con Microsoft Project",
        "nombre_autor": "García Martínez, Juan",
        "año_libro": "2022",
        "formato_libro": "Digital"
      },
      {
        "item": "3",
        "nombre_libro": "Dirección y Gestión de Proyectos",
        "nombre_autor": "Perea Rojas-Marcos, Manuel",
        "año_libro": "2020",
        "formato_libro": "Físico"
      },
      {
        "item": "4",
        "nombre_libro": "Gestión Ágil de Proyectos: SCRUM",
        "nombre_autor": "Palacio, Juan",
        "año_libro": "2023",
        "formato_libro": "Digital"
      },
      {
        "item": "5",
        "nombre_libro": "Gestión de Riesgos en Proyectos",
        "nombre_autor": "Chapman, Chris & Ward, Stephen",
        "año_libro": "2021",
        "formato_libro": "Físico"
      }
    ],
    "inventario_software": [
      {
        "asignatura_software": "Fundamentos de Gestión de Proyectos",
        "nombre_medioseducativossoft": "Microsoft Project Professional",
        "descr_educativosoft": "Software especializado para la planificación, seguimiento y control de proyectos. Permite crear cronogramas, asignar recursos, gestionar presupuestos y generar informes detallados del avance de proyectos."
      },
      {
        "asignatura_software": "Gestión del Tiempo",
        "nombre_medioseducativossoft": "Primavera P6",
        "descr_educativosoft": "Herramienta robusta de gestión de proyectos empresariales que permite programar, organizar y controlar proyectos complejos con múltiples recursos y dependencias."
      },
      {
        "asignatura_software": "Gestión de Costos",
        "nombre_medioseducativossoft": "SAP Project System",
        "descr_educativosoft": "Módulo de SAP para la gestión integrada de proyectos que incluye planificación de costos, control presupuestario y análisis financiero de proyectos."
      },
      {
        "asignatura_software": "Gestión de Comunicaciones",
        "nombre_medioseducativossoft": "Trello",
        "descr_educativosoft": "Plataforma colaborativa basada en tableros Kanban para organizar tareas, proyectos y flujos de trabajo de manera visual y en equipo."
      },
      {
        "asignatura_software": "Gestión de Riesgos",
        "nombre_medioseducativossoft": "@Risk",
        "descr_educativosoft": "Software de análisis de riesgos mediante simulación Monte Carlo que permite evaluar la incertidumbre en proyectos y tomar decisiones basadas en probabilidades."
      }
    ],
    "inventario_laboratorio": [
      {
        "asignatura_laboratorio": "Planeación Estratégica",
        "nombre_medioseducativoslabora": "Laboratorio de Simulación Empresarial",
        "descr_educativolabora": "Espacio equipado con simuladores de negocios (Company Game) que permite a los estudiantes experimentar con la toma de decisiones estratégicas en entornos empresariales controlados."
      },
      {
        "asignatura_laboratorio": "Gestión de la Calidad",
        "nombre_medioseducativoslabora": "Laboratorio de Análisis de Datos",
        "descr_educativolabora": "Laboratorio con software estadístico (Minitab, SPSS) para realizar análisis de control de calidad, Six Sigma y gestión de procesos de mejora continua."
      },
      {
        "asignatura_laboratorio": "Trabajo de Grado",
        "nombre_medioseducativoslabora": "Sala de Proyectos",
        "descr_educativolabora": "Espacio colaborativo equipado con herramientas tecnológicas, pantallas interactivas y zonas de trabajo para el desarrollo de proyectos aplicados y trabajo en equipo."
      }
    ],
    "recursos_bibliograficos": [
      {
        "descr_formatobibli": "Libros físicos",
        "periodo_1": "15",
        "periodo_2": "20",
        "periodo_3": "25",
        "periodo_4": "30",
        "periodo_5": "35",
        "periodo_6": "40",
        "periodo_7": "45",
        "enlace_bibliografico": "https://biblioteca.cun.edu.co/libros-fisicos"
      },
      {
        "descr_formatobibli": "Libros digitales",
        "periodo_1": "50",
        "periodo_2": "75",
        "periodo_3": "100",
        "periodo_4": "125",
        "periodo_5": "150",
        "periodo_6": "175",
        "periodo_7": "200",
        "enlace_bibliografico": "https://biblioteca.cun.edu.co/libros-digitales"
      },
      {
        "descr_formatobibli": "Bases de datos especializadas",
        "periodo_1": "3",
        "periodo_2": "4",
        "periodo_3": "5",
        "periodo_4": "6",
        "periodo_5": "7",
        "periodo_6": "8",
        "periodo_7": "9",
        "enlace_bibliografico": "https://biblioteca.cun.edu.co/bases-datos"
      },
      {
        "descr_formatobibli": "Revistas académicas",
        "periodo_1": "10",
        "periodo_2": "12",
        "periodo_3": "15",
        "periodo_4": "18",
        "periodo_5": "20",
        "periodo_6": "22",
        "periodo_7": "25",
        "enlace_bibliografico": "https://biblioteca.cun.edu.co/revistas"
      },
      {
        "descr_formatobibli": "Software especializado",
        "periodo_1": "5",
        "periodo_2": "6",
        "periodo_3": "7",
        "periodo_4": "8",
        "periodo_5": "9",
        "periodo_6": "10",
        "periodo_7": "11",
        "enlace_bibliografico": "https://software.cun.edu.co/licencias"
      }
    ],
    "proyección_financiera": [
      {
        "Formato_proyeccionfinan": "Libros físicos",
        "periodo_1finan": "$3.000.000",
        "periodo_2finan": "$3.500.000",
        "periodo_3finan": "$4.000.000",
        "periodo_4finan": "$4.500.000",
        "periodo_5finan": "$5.000.000",
        "periodo_6finan": "$5.500.000",
        "periodo_7finan": "$6.000.000"
      },
      {
        "Formato_proyeccionfinan": "Libros digitales",
        "periodo_1finan": "$8.000.000",
        "periodo_2finan": "$9.000.000",
        "periodo_3finan": "$10.000.000",
        "periodo_4finan": "$11.000.000",
        "periodo_5finan": "$12.000.000",
        "periodo_6finan": "$13.000.000",
        "periodo_7finan": "$14.000.000"
      },
      {
        "Formato_proyeccionfinan": "Bases de datos especializadas",
        "periodo_1finan": "$15.000.000",
        "periodo_2finan": "$16.500.000",
        "periodo_3finan": "$18.000.000",
        "periodo_4finan": "$19.500.000",
        "periodo_5finan": "$21.000.000",
        "periodo_6finan": "$22.500.000",
        "periodo_7finan": "$24.000.000"
      },
      {
        "Formato_proyeccionfinan": "Revistas académicas",
        "periodo_1finan": "$5.000.000",
        "periodo_2finan": "$5.500.000",
        "periodo_3finan": "$6.000.000",
        "periodo_4finan": "$6.500.000",
        "periodo_5finan": "$7.000.000",
        "periodo_6finan": "$7.500.000",
        "periodo_7finan": "$8.000.000"
      },
      {
        "Formato_proyeccionfinan": "Software especializado",
        "periodo_1finan": "$25.000.000",
        "periodo_2finan": "$27.000.000",
        "periodo_3finan": "$29.000.000",
        "periodo_4finan": "$31.000.000",
        "periodo_5finan": "$33.000.000",
        "periodo_6finan": "$35.000.000",
        "periodo_7finan": "$37.000.000"
      },
      {
        "Formato_proyeccionfinan": "Equipos y tecnología",
        "periodo_1finan": "$20.000.000",
        "periodo_2finan": "$22.000.000",
        "periodo_3finan": "$24.000.000",
        "periodo_4finan": "$26.000.000",
        "periodo_5finan": "$28.000.000",
        "periodo_6finan": "$30.000.000",
        "periodo_7finan": "$32.000.000"
      },
      {
        "Formato_proyeccionfinan": "Total inversión",
        "periodo_1finan": "$76.000.000",
        "periodo_2finan": "$83.500.000",
        "periodo_3finan": "$91.000.000",
        "periodo_4finan": "$98.500.000",
        "periodo_5finan": "$106.000.000",
        "periodo_6finan": "$114.000.000",
        "periodo_7finan": "$121.000.000"
      }
    ]
  }
}

crear_programa_doc = {
    "operation_summary": "Crear una nueva justificacion de programa",
    "operation_description": (
        "Este endpoint permite registrar la justificacion del programa."
        "Utiliza validaciones de serializer"
        "bla bla bla"
    ),
    "tags": ["Medios Educativos"],
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "llave_maestra": openapi.Schema(type=openapi.TYPE_STRING, example="2025001"),
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
            description="Medios Educativos creados exitosamente",
            schema=MediosEducativosSerializer,
        ),
        400: openapi.Response(
            description="Error de ingreso/validacion de los datos enviados"
        ),
    },
}
