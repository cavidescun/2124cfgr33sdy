from drf_yasg import openapi
from ..serializers import AspectosCurricularesSerializer

etiquetas_dinamicas_example ={
  "variables": {
    "modalidad_programa": "presencial",
    "nombre_de_programa": "Especialización en Gestión de Proyectos",
    "total_materias": "12 materias",
    "créditos_academicos": "30 créditos académicos",
    "total_horas": "1440 horas",
    "duración_programa": "2 semestres",
    "minymax_espaciosacademicos": "5 a 7",
    "maxymin_espaciosacademicos": "14 a 16",
    "creditos_diciplinares": "24 créditos académicos",
    "créditos_electivos": "6",
    "materias_primersemestre": "MATERIAS PRIMER SEMESTRE",
    "listadomaterias_primersemestre": "Fundamentos de Gestión de Proyectos, Planeación Estratégica, Gestión del Alcance, Gestión del Tiempo, Gestión de Costos, Gestión de la Calidad",
    "materias_segundosemestre": "MATERIAS SEGUNDO SEMESTRE",
    "listadomaterias_segundosemestre": "Gestión de Recursos Humanos, Gestión de Comunicaciones, Gestión de Riesgos, Gestión de Adquisiciones, Electiva I, Trabajo de Grado",
    "perfil_ingreso": "Profesionales de diferentes áreas del conocimiento con interés en desarrollar competencias en dirección y gestión de proyectos. Se requiere título profesional de pregrado en cualquier disciplina, experiencia laboral mínima de un año, y capacidad de análisis, liderazgo y trabajo en equipo.",
    "perfil_egreso": "El egresado de la Especialización en Gestión de Proyectos estará en capacidad de planificar, ejecutar, controlar y cerrar proyectos de diversa índole aplicando metodologías reconocidas internacionalmente. Podrá liderar equipos de trabajo, gestionar recursos eficientemente y tomar decisiones estratégicas que garanticen el éxito de los proyectos bajo su responsabilidad.",
    "perfil_ocupacional": "El especialista podrá desempeñarse como: Director de Proyectos, Coordinador de PMO (Project Management Office), Consultor en Gestión de Proyectos, Analista de Proyectos, Gerente de Portafolio de Proyectos, tanto en el sector público como privado, en organizaciones nacionales e internacionales de diversos sectores económicos.",
    "elemento_TyE": "La conceptualización teórica y epistemológica del programa se fundamenta en las mejores prácticas internacionales de gestión de proyectos, particularmente en el PMBOK Guide del Project Management Institute (PMI) y metodologías ágiles como SCRUM. El programa integra enfoques tradicionales y contemporáneos de la administración de proyectos, considerando aspectos técnicos, humanos y organizacionales. Se sustenta en teorías de gestión estratégica, liderazgo transformacional, toma de decisiones y optimización de recursos, con un enfoque sistémico que reconoce la complejidad de los proyectos en contextos dinámicos y globalizados.",
    "estudiosrepresentados": [
      {
        "semestre": "I",
        "numero_orden": "1",
        "asignatura": "Fundamentos de Gestión de Proyectos",
        "tipologia": "Teórico-Práctica",
        "creditosmateria": "3",
        "horas_trabajo": "144"
      },
      {
        "semestre": "I",
        "numero_orden": "2",
        "asignatura": "Planeación Estratégica",
        "tipologia": "Teórico-Práctica",
        "creditosmateria": "2",
        "horas_trabajo": "96"
      },
      {
        "semestre": "I",
        "numero_orden": "3",
        "asignatura": "Gestión del Alcance",
        "tipologia": "Teórico-Práctica",
        "creditosmateria": "3",
        "horas_trabajo": "144"
      },
      {
        "semestre": "I",
        "numero_orden": "4",
        "asignatura": "Gestión del Tiempo",
        "tipologia": "Teórico-Práctica",
        "creditosmateria": "2",
        "horas_trabajo": "96"
      },
      {
        "semestre": "I",
        "numero_orden": "5",
        "asignatura": "Gestión de Costos",
        "tipologia": "Teórico-Práctica",
        "creditosmateria": "3",
        "horas_trabajo": "144"
      },
      {
        "semestre": "I",
        "numero_orden": "6",
        "asignatura": "Gestión de la Calidad",
        "tipologia": "Teórico-Práctica",
        "creditosmateria": "2",
        "horas_trabajo": "96"
      },
      {
        "semestre": "II",
        "numero_orden": "7",
        "asignatura": "Gestión de Recursos Humanos",
        "tipologia": "Teórico-Práctica",
        "creditosmateria": "3",
        "horas_trabajo": "144"
      },
      {
        "semestre": "II",
        "numero_orden": "8",
        "asignatura": "Gestión de Comunicaciones",
        "tipologia": "Teórico-Práctica",
        "creditosmateria": "2",
        "horas_trabajo": "96"
      },
      {
        "semestre": "II",
        "numero_orden": "9",
        "asignatura": "Gestión de Riesgos",
        "tipologia": "Teórico-Práctica",
        "creditosmateria": "3",
        "horas_trabajo": "144"
      },
      {
        "semestre": "II",
        "numero_orden": "10",
        "asignatura": "Gestión de Adquisiciones",
        "tipologia": "Teórico-Práctica",
        "creditosmateria": "2",
        "horas_trabajo": "96"
      },
      {
        "semestre": "II",
        "numero_orden": "11",
        "asignatura": "Electiva I",
        "tipologia": "Electiva",
        "creditosmateria": "2",
        "horas_trabajo": "96"
      },
      {
        "semestre": "II",
        "numero_orden": "12",
        "asignatura": "Trabajo de Grado",
        "tipologia": "Práctica",
        "creditosmateria": "3",
        "horas_trabajo": "144"
      }
    ],
    "tablarae": [
      {
        "dominio_competencia": "Cognitivo",
        "nivel_taxonomico_competencia": "Analizar",
        "competencia_objetivocondiciónfinalidad": "Analizar la viabilidad de proyectos considerando variables técnicas, económicas y sociales para determinar su factibilidad",
        "espaciosacadémico": "Fundamentos de Gestión de Proyectos",
        "nivel_taxonomico_resultados": "Evaluar",
        "resultados_objetivocondiciónfinalidad": "Evaluar propuestas de proyectos mediante el análisis de estudios de factibilidad para recomendar su aprobación o rechazo"
      },
      {
        "dominio_competencia": "Praxiológico",
        "nivel_taxonomico_competencia": "Aplicar",
        "competencia_objetivocondiciónfinalidad": "Aplicar metodologías de planificación de proyectos utilizando herramientas especializadas para garantizar el cumplimiento de objetivos",
        "espaciosacadémico": "Planeación Estratégica",
        "nivel_taxonomico_resultados": "Crear",
        "resultados_objetivocondiciónfinalidad": "Crear planes de proyecto integrales que incluyan alcance, tiempo, costo y calidad para asegurar una ejecución exitosa"
      },
      {
        "dominio_competencia": "Praxiológico",
        "nivel_taxonomico_competencia": "Aplicar",
        "competencia_objetivocondiciónfinalidad": "Aplicar técnicas de gestión del alcance para definir y controlar el trabajo del proyecto",
        "espaciosacadémico": "Gestión del Alcance",
        "nivel_taxonomico_resultados": "Aplicar",
        "resultados_objetivocondiciónfinalidad": "Aplicar herramientas de definición de alcance como EDT/WBS para estructurar el trabajo del proyecto de manera jerárquica"
      },
      {
        "dominio_competencia": "Cognitivo",
        "nivel_taxonomico_competencia": "Comprender",
        "competencia_objetivocondiciónfinalidad": "Comprender los principios de gestión del tiempo para optimizar el cronograma del proyecto",
        "espaciosacadémico": "Gestión del Tiempo",
        "nivel_taxonomico_resultados": "Aplicar",
        "resultados_objetivocondiciónfinalidad": "Aplicar técnicas de programación como ruta crítica y nivelación de recursos para desarrollar cronogramas realistas"
      },
      {
        "dominio_competencia": "Praxiológico",
        "nivel_taxonomico_competencia": "Analizar",
        "competencia_objetivocondiciónfinalidad": "Analizar la estructura de costos del proyecto para mantener el presupuesto bajo control",
        "espaciosacadémico": "Gestión de Costos",
        "nivel_taxonomico_resultados": "Evaluar",
        "resultados_objetivocondiciónfinalidad": "Evaluar el desempeño financiero del proyecto mediante técnicas de valor ganado para tomar decisiones correctivas"
      },
      {
        "dominio_competencia": "Actitudinal",
        "nivel_taxonomico_competencia": "Valorar",
        "competencia_objetivocondiciónfinalidad": "Valorar la importancia del liderazgo y la comunicación efectiva para dirigir equipos de proyecto",
        "espaciosacadémico": "Gestión de Recursos Humanos",
        "nivel_taxonomico_resultados": "Organizar",
        "resultados_objetivocondiciónfinalidad": "Organizar equipos de trabajo considerando competencias y habilidades para maximizar el rendimiento del proyecto"
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
    "tags": ["Aspectos Curriculares"],
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
            description="Aspectos Curriculares creada exitosamente",
            schema=AspectosCurricularesSerializer,
        ),
        400: openapi.Response(
            description="Error de ingreso/validacion de los datos enviados"
        ),
    },
}
