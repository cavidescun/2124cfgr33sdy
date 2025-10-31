from drf_yasg import openapi
from ..serializers import SectorExternoSerializer

etiquetas_dinamicas_example ={
  "variables": {
    "modalidad_programa": "virtual",
    "nombre_de_programa": "Gerencia de Proyectos",
    "numero_docentes_proyeccion_social": 3,
    
    "conveniosestablecidos": [
    {
      "eje_convenios": "Emprendimiento y desarrollo económico",
      "objetivo_convenios": "Fortalecer competencias empresariales en estudiantes",
      "actividad_convenios": "Talleres de emprendimiento con empresas del sector",
      "resultado_esperado_convenios": "100 estudiantes capacitados en emprendimiento",
      "t2020_convenios": "X",
      "t2021_convenios": "X",
      "t2022_convenios": "X",
      "t2023_convenios": "X",
      "t2024_convenios": "X",
      "t2025_convenios": "X",
      "responsable_actividad_convenios": "Coordinador de Proyección Social",
      "recursos_convenios": "Plataforma virtual, docentes, material didáctico",
      "presupuesto_convenios": "$15.000.000"
    },
    {
      "eje_convenios": "Innovación y TIC",
      "objetivo_convenios": "Desarrollar proyectos de innovación tecnológica",
      "actividad_convenios": "Proyectos integrados con empresas tecnológicas",
      "resultado_esperado_convenios": "5 proyectos de innovación implementados",
      "t2020_convenios": "",
      "t2021_convenios": "X",
      "t2022_convenios": "X",
      "t2023_convenios": "X",
      "t2024_convenios": "X",
      "t2025_convenios": "X",
      "responsable_actividad_convenios": "Director de Programa",
      "recursos_convenios": "Laboratorios, software especializado, mentores",
      "presupuesto_convenios": "$25.000.000"
    },
    {
      "eje_convenios": "Medio ambiente y sostenibilidad",
      "objetivo_convenios": "Promover prácticas sostenibles en gestión de proyectos",
      "actividad_convenios": "Certificaciones en gestión ambiental de proyectos",
      "resultado_esperado_convenios": "50 estudiantes certificados en sostenibilidad",
      "t2020_convenios": "",
      "t2021_convenios": "",
      "t2022_convenios": "X",
      "t2023_convenios": "X",
      "t2024_convenios": "X",
      "t2025_convenios": "X",
      "responsable_actividad_convenios": "Docente de Proyección Social",
      "recursos_convenios": "Material educativo, plataforma e-learning",
      "presupuesto_convenios": "$10.000.000"
    }
  ],
  
  "docentesdelprograma": [
    {
      "nombre_docente": "Carlos Andrés Martínez López",
      "formacion_docente": "Magíster en Gestión de Proyectos",
      "docentes_vinculacion": "Tiempo Completo",
      "asignacion_horaria": "8 horas semanales proyección social"
    },
    {
      "nombre_docente": "María Fernanda Rojas Gutiérrez",
      "formacion_docente": "Doctora en Administración",
      "docentes_vinculacion": "Medio Tiempo",
      "asignacion_horaria": "4 horas semanales proyección social"
    },
    {
      "nombre_docente": "Juan Pablo Vargas Sánchez",
      "formacion_docente": "Magíster en Ingeniería Industrial",
      "docentes_vinculacion": "Cátedra",
      "asignacion_horaria": "3 horas semanales proyección social"
    }
  ],
  
  "conveniocooperacion": [
    {
      "vigencia_convenio": "2023-2028",
      "numero_convenio": "CONV-001-2023",
      "objetivo_convenio": "Cooperación académica e investigativa para el fortalecimiento de competencias en gerencia de proyectos"
    },
    {
      "vigencia_convenio": "2024-2027",
      "numero_convenio": "CONV-045-2024",
      "objetivo_convenio": "Intercambio de conocimientos y desarrollo de proyectos conjuntos en innovación empresarial"
    },
    {
      "vigencia_convenio": "2022-2025",
      "numero_convenio": "CONV-112-2022",
      "objetivo_convenio": "Capacitación y certificación de estudiantes en metodologías ágiles de gestión de proyectos"
    },
    {
      "vigencia_convenio": "2024-2029",
      "numero_convenio": "CONV-078-2024",
      "objetivo_convenio": "Desarrollo de proyectos de transformación digital con acompañamiento empresarial"
    }
  ],
  
  "conveniopracticas": [
    {
      "codigo_convenio": "PRAC-2023-001",
      "aliado_convenio": "Constructora Andina S.A.S.",
      "inicio_vigencia_convenio": "01/03/2023",
      "fin_vigencia_convenio": "01/03/2026",
      "prorroga_convenio": "Sí"
    },
    {
      "codigo_convenio": "PRAC-2023-015",
      "aliado_convenio": "Consultoría Empresarial PMI Colombia",
      "inicio_vigencia_convenio": "15/06/2023",
      "fin_vigencia_convenio": "15/06/2028",
      "prorroga_convenio": "Sí"
    },
    {
      "codigo_convenio": "PRAC-2024-022",
      "aliado_convenio": "Tech Solutions International",
      "inicio_vigencia_convenio": "01/02/2024",
      "fin_vigencia_convenio": "01/02/2027",
      "prorroga_convenio": "No"
    },
    {
      "codigo_convenio": "PRAC-2024-033",
      "aliado_convenio": "Fundación para el Desarrollo Empresarial",
      "inicio_vigencia_convenio": "20/05/2024",
      "fin_vigencia_convenio": "20/05/2029",
      "prorroga_convenio": "Sí"
    },
    {
      "codigo_convenio": "PRAC-2022-008",
      "aliado_convenio": "Banco de Proyectos Territoriales",
      "inicio_vigencia_convenio": "10/09/2022",
      "fin_vigencia_convenio": "10/09/2025",
      "prorroga_convenio": "Sí"
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
    "tags": ["Relacion Sector Externo"],
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
            description="Relacion con sector externo creada exitosamente",
            schema=SectorExternoSerializer,
        ),
        400: openapi.Response(
            description="Error de ingreso/validacion de los datos enviados"
        ),
    },
}
