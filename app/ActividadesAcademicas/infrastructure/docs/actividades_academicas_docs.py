from drf_yasg import openapi
from ..serializers import ActividadesAcademicasSerializer

etiquetas_dinamicas_example = {
    "tablas": {
      "graficodetorta_distribucion_creditos": [
        {"caracteristica": "Disciplinar", "total": "70"},
        {"caracteristica": "Electivo", "total": "15"},
        {"caracteristica": "Transversal Institucional", "total": "15"}
      ],
      "graficodetorta_distribucion_componente": [
        {"caracteristica": "Área Fundamental", "total": "45"},
        {"caracteristica": "Área Profesional", "total": "35"},
        {"caracteristica": "Área de Profundización", "total": "20"}
      ],
    },
    "_graficos_config": {
      "graficodetorta_distribucion_creditos": {
        "tipo": "torta",
        "titulo": "graficodetorta_distribucion_creditos",
        "filename": "graficodetorta_distribucion_creditos.png",
        "categorias_campo": "caracteristica",
        "valores_campo": "total"
      },
      "graficodetorta_distribucion_componente": {
        "tipo": "torta",
        "titulo": "graficodetorta_distribucion_componente",
        "filename": "graficodetorta_distribucion_componente.png",
        "categorias_campo": "caracteristica",
        "valores_campo": "total"
      },
  },
    "variables":{
  "nombre_de_programa": "Especialización en Gerencia de Proyectos",
  "modalidad_programa": "virtual",
  "componentes": [
    {
      "componente": "Disciplinar",
      "porcentaje_distribucion_creditos": "70%"
    },
    {
      "componente": "Electivo",
      "porcentaje_distribucion_creditos": "15%"
    },
    {
      "componente": "Transversal Institucional",
      "porcentaje_distribucion_creditos": "15%"
    }
  ],
  
  "componentes_creditos": [
    {
      "componente": "Área Fundamental",
      "porcentaje_distribucion_componente": "45%"
    },
    {
      "componente": "Área Profesional",
      "porcentaje_distribucion_componente": "35%"
    },
    {
      "componente": "Área de Profundización",
      "porcentaje_distribucion_componente": "20%"
    }
  ],
  
  "componentes_area": [
    {
      "componente": "Disciplinar",
      "area": "Gestión de Proyectos",
      "asignatura": "Fundamentos de Gerencia de Proyectos",
      "creditos": 3,
      "porcentaje_area": "25%",
      "total_creditos": 12,
      "porcentaje_distribucion_componente": "40%"
    },
    {
      "componente": "Disciplinar",
      "area": "Gestión de Proyectos",
      "asignatura": "Planificación Estratégica de Proyectos",
      "creditos": 3,
      "porcentaje_area": "25%",
      "total_creditos": 12,
      "porcentaje_distribucion_componente": "40%"
    },
    {
      "componente": "Disciplinar",
      "area": "Gestión Financiera",
      "asignatura": "Gestión Financiera de Proyectos",
      "creditos": 3,
      "porcentaje_area": "20%",
      "total_creditos": 15,
      "porcentaje_distribucion_componente": "50%"
    },
    {
      "componente": "Electivo",
      "area": "Electivas Profesionales",
      "asignatura": "Innovación y Emprendimiento",
      "creditos": 2,
      "porcentaje_area": "40%",
      "total_creditos": 5,
      "porcentaje_distribucion_componente": "100%"
    },
    {
      "componente": "Transversal Institucional",
      "area": "Investigación",
      "asignatura": "Proyecto Integrado de Aula I",
      "creditos": 3,
      "porcentaje_area": "60%",
      "total_creditos": 5,
      "porcentaje_distribucion_componente": "100%"
    }
  ],
  
   "Componente_uniestructural": "El nivel uniestructural se caracteriza por la adquisición de conocimientos básicos y fundamentales. En este nivel, el estudiante identifica conceptos aislados y desarrolla habilidades elementales relacionadas con la gerencia de proyectos, tales como la identificación de las fases de un proyecto y el reconocimiento de metodologías básicas de gestión.",
        "Componente_multiestructural": "El nivel multiestructural implica la integración de varios conocimientos y habilidades de manera coordinada. El estudiante es capaz de relacionar diferentes conceptos de la gerencia de proyectos, aplicando herramientas y técnicas en contextos específicos, permitiendo una comprensión más amplia de la disciplina.",
        "Componente_integrador": "En el nivel integrador, el estudiante logra una comprensión holística del campo de estudio, integrando conocimientos teóricos y prácticos para resolver problemas complejos. Se espera que articule diferentes áreas del conocimiento para proponer soluciones innovadoras en la gestión de proyectos.",
        "Componente_relacional": "El nivel relacional o ampliado representa el más alto grado de aprendizaje, donde el estudiante no solo integra conocimientos, sino que los extiende y generaliza a nuevos contextos. Es capaz de realizar análisis críticos, proponer nuevas metodologías y contribuir al avance del conocimiento en gerencia de proyectos.",
        "Componente_investigacion": "El componente de investigación se desarrolla transversalmente a través de los Proyectos Integrados de Aula y los Núcleos Integradores Problémicos, donde los estudiantes aplican la metodología de Aprendizaje Basado en Problemas (ABP) para articular los saberes adquiridos y dar respuesta a situaciones problemáticas reales del contexto profesional.",
        "Componente_accion": "El componente de acción enfatiza la aplicación práctica del conocimiento en contextos reales. A través de ejercicios prácticos, estudios de caso y proyectos aplicados, los estudiantes desarrollan competencias procedimentales que les permiten desempeñarse eficientemente como especialistas en gerencia de proyectos.",
  
  "proporciones": [
    {
      "proporcion": "1:5",
      "cantidad_semanas": 16,
      "creditos": 1,
      "had": 8,
      "hti": 40,
      "ht": 48
    },
    {
      "proporcion": "1:5",
      "cantidad_semanas": 16,
      "creditos": 2,
      "had": 16,
      "hti": 80,
      "ht": 96
    },
    {
      "proporcion": "1:5",
      "cantidad_semanas": 16,
      "creditos": 3,
      "had": 24,
      "hti": 120,
      "ht": 144
    },
    {
      "proporcion": "1:5",
      "cantidad_semanas": 16,
      "creditos": 4,
      "had": 32,
      "hti": 160,
      "ht": 192
    }
  ],
  
  "asignaturas": [
    {
      "asignatura": "Fundamentos de Gerencia de Proyectos",
      "creditos_academicos": 3,
      "had": 24,
      "hti": 120,
      "ht": 144,
      "semestre": 1,
      "tipologia": "Teórica"
    },
    {
      "asignatura": "Planificación Estratégica de Proyectos",
      "creditos_academicos": 3,
      "had": 24,
      "hti": 120,
      "ht": 144,
      "semestre": 1,
      "tipologia": "Teórico-Práctica"
    },
    {
      "asignatura": "Gestión Financiera de Proyectos",
      "creditos_academicos": 3,
      "had": 24,
      "hti": 120,
      "ht": 144,
      "semestre": 2,
      "tipologia": "Teórico-Práctica"
    },
    {
      "asignatura": "Proyecto Integrado de Aula I",
      "creditos_academicos": 3,
      "had": 24,
      "hti": 120,
      "ht": 144,
      "semestre": 2,
      "tipologia": "Práctica"
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
    "tags": ["Actividades Academicas"],
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "llave_maestra": openapi.Schema(type=openapi.TYPE_STRING, example="LLAVE-B16182F2"),
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
            description="Actividades Academicas creada exitosamente",
            schema=ActividadesAcademicasSerializer,
        ),
        400: openapi.Response(
            description="Error de ingreso/validacion de los datos enviados"
        ),
    },
}
