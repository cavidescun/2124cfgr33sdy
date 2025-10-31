from drf_yasg import openapi
from ..serializers import ProfesoresSerializer

etiquetas_dinamicas_example = {
    "variables": {
        "nombre_de_programa": "Especialización en Gerencia de Proyectos",
        "modalidad_programa": "virtual",
        "total_profesores": 12,
        "total_profesores_tiempo_completo": 8,
        "total_profesores_medio_tiempo": 4,
        "estudiantes_por_profesor": 25,
        "profesores": [
            {
                "profesor": "Dr. Juan Carlos Martínez",
                "vinculacion": "Tiempo Completo",
                "formacion_academica": "Doctorado en Administración",
                "formacion_pedagogica": "Diplomado en Pedagogía Universitaria",
                "formacion_virtual": "Certificación en Educación Virtual",
                "porc_dedicacion": "100%",
                "porc_docencia": "60%",
                "porc_investigacion": "25%",
                "porc_proyeccion_social": "10%",
                "porc_otros": "5%",
                "max_formacion": "Doctor",
                "cvlac": "https://scienti.minciencias.gov.co/cvlac/visualizador/12345",
                "tipo_contrato": "Término Indefinido",
                "asignacion_horaria": "40 horas semanales",
            },
            {
                "profesor": "Mg. María Fernanda López",
                "vinculacion": "Tiempo Completo",
                "formacion_academica": "Maestría en Gerencia de Proyectos",
                "formacion_pedagogica": "Especialización en Docencia Universitaria",
                "formacion_virtual": "Curso en Herramientas Digitales",
                "porc_dedicacion": "100%",
                "porc_docencia": "70%",
                "porc_investigacion": "20%",
                "porc_proyeccion_social": "5%",
                "porc_otros": "5%",
                "max_formacion": "Magister",
                "cvlac": "https://scienti.minciencias.gov.co/cvlac/visualizador/67890",
                "tipo_contrato": "Término Indefinido",
                "asignacion_horaria": "40 horas semanales",
            },
            {
                "profesor": "Esp. Carlos Andrés Rodríguez",
                "vinculacion": "Medio Tiempo",
                "formacion_academica": "Especialización en Gerencia Estratégica",
                "formacion_pedagogica": "Diplomado en Estrategias Didácticas",
                "formacion_virtual": "Certificación Moodle",
                "porc_dedicacion": "50%",
                "porc_docencia": "80%",
                "porc_investigacion": "10%",
                "porc_proyeccion_social": "5%",
                "porc_otros": "5%",
                "max_formacion": "Especialista",
                "cvlac": "https://scienti.minciencias.gov.co/cvlac/visualizador/11223",
                "tipo_contrato": "Por Periodo Académico",
                "asignacion_horaria": "20 horas semanales",
            },
        ],
        "tipo_vinculacion": [
            {
                "vinculacion": "Tiempo Completo",
                "max_nivel_formacion": "Doctorado",
                "area_conocimiento": "Administración y Gerencia",
                "formacion_adicional": "Certificación en Gestión de Proyectos PMI",
                "profesor": "Dr. Juan Carlos Martínez",
            },
            {
                "vinculacion": "Tiempo Completo",
                "max_nivel_formacion": "Maestría",
                "area_conocimiento": "Ingeniería Industrial",
                "formacion_adicional": "Diplomado en Metodologías Ágiles",
                "profesor": "Mg. María Fernanda López",
            },
            {
                "vinculacion": "Medio Tiempo",
                "max_nivel_formacion": "Especialización",
                "area_conocimiento": "Gerencia Estratégica",
                "formacion_adicional": "Certificación SCRUM Master",
                "profesor": "Esp. Carlos Andrés Rodríguez",
            },
            {
                "vinculacion": "Cátedra",
                "max_nivel_formacion": "Maestría",
                "area_conocimiento": "Finanzas Corporativas",
                "formacion_adicional": "Certificación en Evaluación Financiera de Proyectos",
                "profesor": "Mg. Laura Patricia Gómez",
            },
        ],
    }
}
crear_programa_doc = {
    "operation_summary": "Crear una nueva justificacion de programa",
    "operation_description": (
        "Este endpoint permite registrar la justificacion del programa."
        "Utiliza validaciones de serializer"
        "bla bla bla"
    ),
    "tags": ["Profesores"],
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
             "llave_maestra": openapi.Schema(
                type=openapi.TYPE_STRING,
                example="E121244",
            ),
            "etiquetas_dinamicas": openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example=etiquetas_dinamicas_example,
            ),
        },
        required=[
            "llave_maestra"
            "etiquetas_dinamicas",
        ],
    ),
    "responses": {
        201: openapi.Response(
            description="Profesores creado exitosamente",
            schema=ProfesoresSerializer,
        ),
        400: openapi.Response(
            description="Error de ingreso/validacion de los datos enviados"
        ),
    },
}
