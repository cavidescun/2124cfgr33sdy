from drf_yasg import openapi
from ..serializers import JustificacionProgramaSerializer

etiquetas_dinamicas_example = {
    "tablas": {
        "GC_inscritos": [
            {"años": 2020, "inscritos": 320},
            {"años": 2021, "inscritos": 365},
            {"años": 2022, "inscritos": 420}
        ],
        "GC_admitidos": [
            {"años": 2020, "admitidos": 280},
            {"años": 2021, "admitidos": 310},
            {"años": 2022, "admitidos": 350}
        ],
        "GC_matriculados": [
            {"años": 2020, "matriculados": 270},
            {"años": 2021, "matriculados": 300},
            {"años": 2022, "matriculados": 335}
        ],
        "GC_graduados": [
            {"años": 2020, "graduados": 235},
            {"años": 2021, "graduados": 260},
            {"años": 2022, "graduados": 293}
        ],
        "GC_tasadesercion": [
            {
                "IES": "Universidad Nacional",
                "añouno": 12.5,
                "añodos": 11.8,
                "añotres": 10.2,
                "añocuatro": 13.5,
                "añocinco": 9.8,
                "añosesis": 8.5
            },
            {
                "IES": "Universidad de los Andes",
                "añouno": 8.3,
                "añodos": 7.9,
                "añotres": 7.2,
                "añocuatro": 9.1,
                "añocinco": 6.5,
                "añoseis": 5.8
            },
            {
                "IES": "Universidad Externado",
                "añouno": 14.2,
                "añodos": 13.5,
                "añotres": 12.8,
                "añocuatro": 15.3,
                "añocinco": 11.2,
                "añoseis": 10.5
            }
        ],
        "GC_vinculacion_laboral": [
            {"año": 2017, "nacional": 65.3, "cun": 75.8},
            {"año": 2018, "nacional": 67.1, "cun": 78.2},
            {"año": 2019, "nacional": 68.5, "cun": 80.1},
            {"año": 2020, "nacional": 63.2, "cun": 74.5},
            {"año": 2021, "nacional": 71.8, "cun": 83.2},
            {"año": 2022, "nacional": 74.5, "cun": 87.0}
        ],
        "tablareferentes": [
            {
                "Institucion": "Universidad Nacional de Colombia",
                "programa": "Especialización en Marketing Político",
                "modalidad": "Presencial",
                "credito": 24,
                "periodos": 2,
                "periodicidad": "Semestral",
                "municipio": "Bogotá"
            },
            {
                "Institucion": "Universidad de los Andes",
                "programa": "Especialización en Comunicación Política",
                "modalidad": "Virtual",
                "credito": 30,
                "periodos": 3,
                "periodicidad": "Trimestral",
                "municipio": "Bogotá"
            },
            {
                "Institucion": "Universidad Externado de Colombia",
                "programa": "Especialización en Marketing Político y Electoral",
                "modalidad": "Presencial",
                "credito": 28,
                "periodos": 2,
                "periodicidad": "Semestral",
                "municipio": "Bogotá"
            }
        ],
        "programasint": [
            {
                "pais": "España",
                "universidad": "Universidad Complutense de Madrid",
                "denominacion": "Máster en Marketing Político",
                "duracion_estimada": "12 meses",
                "modalidad": "Presencial",
                "perfil": "Profesionales en comunicación, ciencias políticas y marketing"
            },
            {
                "pais": "México",
                "universidad": "Universidad Iberoamericana",
                "denominacion": "Maestría en Comunicación Política",
                "duracion_estimada": "18 meses",
                "modalidad": "Híbrida",
                "perfil": "Graduados en áreas sociales y comunicación"
            },
            {
                "pais": "Argentina",
                "universidad": "Universidad de Buenos Aires",
                "denominacion": "Posgrado en Marketing Electoral",
                "duracion_estimada": "10 meses",
                "modalidad": "Virtual",
                "perfil": "Profesionales del área política y comunicacional"
            }
        ],
        "estadisticasestudiantes": [
            {
                "institucion_educacion_superior": "Universidad Nacional de Colombia",
                "programa_academico": "Especialización en Marketing Político",
                "años": 2022,
                "inscritos": 145,
                "Admitidos": 120,
                "Matriculados": 115,
                "graduados": 98
            },
            {
                "institucion_educacion_superior": "Universidad de los Andes",
                "programa_academico": "Especialización en Comunicación Política",
                "años": 2022,
                "inscritos": 180,
                "Admitidos": 150,
                "Matriculados": 145,
                "graduados": 130
            },
            {
                "institucion_educacion_superior": "Universidad Externado de Colombia",
                "programa_academico": "Especialización en Marketing Político",
                "años": 2022,
                "inscritos": 95,
                "Admitidos": 80,
                "Matriculados": 75,
                "graduados": 65
            }
        ]
    },
    "_graficos_config": {
        "GC_inscritos": {
            "tipo": "barras",
            "titulo": "Evolución de Estudiantes Inscritos",
            "filename": "grafico_columnas_inscritos.png",
            "categorias_campo": "años",
            "valores_campo": "inscritos"
        },
        "GC_admitidos": {
            "tipo": "barras",
            "titulo": "Evolución de Estudiantes Admitidos",
            "filename": "grafico_columnas_admitidos.png",
            "categorias_campo": "años",
            "valores_campo": "admitidos"
        },
        "GC_matriculados": {
            "tipo": "barras",
            "titulo": "Evolución de Estudiantes Matriculados",
            "filename": "grafico_columnas_matriculados.png",
            "categorias_campo": "años",
            "valores_campo": "matriculados"
        },
        "GC_graduados": {
            "tipo": "barras",
            "titulo": "Evolución de Estudiantes Graduados",
            "filename": "grafico_columnas_graduados.png",
            "categorias_campo": "años",
            "valores_campo": "graduados"
        },
        "GC_tasadesercion": {
            "tipo": "lineas",
            "titulo": "Tasas de Deserción por Institución",
            "filename": "grafico_lineas_desercion.png",
            "categorias_campo": "IES",
            "series": ["añouno", "añodos", "añotres", "añocuatro", "añocinco", "añoseis"]
        },
        "GC_vinculacion_laboral": {
            "tipo": "lineas",
            "titulo": "Vinculación Laboral de Recién Graduados: Nacional vs CUN",
            "filename": "grafico_lineas_vinculacion_laboral.png",
            "categorias_campo": "año",
            "series": ["nacional", "cun"]
        }
    },
    "variables": {
        "nombre_de_programa": "Marketing Político",
        "tipo_registro": "Registro Calificado",
        "modalidad_programa": "Virtual",
        "análisis_referentes": "El análisis comparativo muestra que los programas nacionales tienen una duración promedio de 2 semestres con 24-30 créditos académicos. La mayoría se ofrecen en modalidad presencial en las principales ciudades del país. Los perfiles de egreso están orientados hacia la gestión de campañas políticas y estrategias de comunicación gubernamental.",
        "análisis_programasint": "A nivel internacional, se observa una tendencia hacia programas de maestría con duración entre 10 y 18 meses. Las universidades europeas lideran la oferta con enfoques en comunicación política digital, mientras que en Latinoamérica predominan los programas enfocados en marketing electoral y gestión de campañas.",
        "análisis_estadisticasestudiantes": "Las estadísticas muestran un crecimiento sostenido en la matrícula de programas afines, con tasas de admisión promedio del 85% y tasas de graduación cercanas al 80%. La Universidad de los Andes presenta los mejores indicadores de captación y retención estudiantil.",
        "análisis_desercion": "Los datos evidencian una disminución progresiva en las tasas de deserción en el período 2017-2022, pasando de promedios del 11.7% al 8.3%. El año 2020 presenta un incremento atípico relacionado con la pandemia. Las estrategias de acompañamiento estudiantil han mostrado efectividad en la reducción de este indicador.",
        "análisis_tasa_vinculacion": "La tasa de vinculación laboral de egresados de la CUN se mantiene consistentemente 8-12 puntos porcentuales por encima del promedio nacional, alcanzando el 87% en los últimos períodos medidos.",
        "Expectativas_laborales": "especialización en Marketing Político ofrece amplias oportunidades en consultoría política, gestión de campañas electorales, comunicación gubernamental, análisis de opinión pública y estrategia digital para organizaciones políticas y sociales, con una demanda creciente en el sector público y privado",
        "nombre_regional1": "Cundinamarca",
        "plan_departamental_1": "El Plan de Desarrollo Departamental 2020-2024 'Cundinamarca, Región que Progresa' establece como ejes estratégicos la transformación digital, la educación de calidad y el fortalecimiento institucional. Promueve la formación posgradual en áreas relacionadas con la gestión pública, la comunicación y el liderazgo político territorial.",
        "nombre_regional2": "Antioquia",
        "plan_departamental_2": "El Plan de Desarrollo 'Unidos por la Vida' 2020-2023 prioriza la educación superior como motor de desarrollo regional, incentivando programas de especialización en gobernanza, participación ciudadana y comunicación política para fortalecer las capacidades de los líderes regionales.",
        "nombre_regional3": "Valle del Cauca",
        "plan_departamental_3": "El Plan de Desarrollo 'Valle Invencible' contempla estrategias de formación avanzada en gestión pública y comunicación estratégica para mejorar la capacidad institucional y la participación democrática en el departamento.",
        "nombre_regional4": "Atlántico",
        "plan_departamental_4": "El departamento prioriza la formación en competencias políticas y comunicacionales para fortalecer el liderazgo regional y la transparencia en la gestión pública, alineándose con los objetivos de modernización institucional.",
        "nombre_regional5": "Santander",
        "plan_departamental_5": "El Plan Departamental impulsa programas de educación posgradual que contribuyan al fortalecimiento democrático, la innovación en gestión pública y el desarrollo de capacidades en comunicación política y social.",
        "nombre_regional6": "Bolívar",
        "plan_departamental_6": "Bolívar incluye en su plan de desarrollo la necesidad de formar profesionales especializados en marketing político y comunicación estratégica para mejorar la gestión territorial y fortalecer los procesos democráticos locales.",
        "nombre_regional7": "Tolima",
        "plan_departamental_7": "El departamento reconoce la importancia de la formación especializada en comunicación política y gestión electoral como elementos clave para la consolidación de procesos democráticos y la modernización institucional.",
        "nombre_regional8": "Huila",
        "plan_departamental_8": "El Plan de Desarrollo del Huila enfatiza la formación posgradual en áreas de gobernanza, comunicación pública y participación ciudadana como estrategias para el desarrollo regional sostenible.",
        "justificacion_modalidades": "La modalidad virtual del programa de Especialización en Marketing Político responde a las necesidades actuales del mercado educativo colombiano y a las tendencias globales de educación superior. Esta modalidad permite ampliar la cobertura geográfica, facilitar el acceso a profesionales en ejercicio, reducir costos de desplazamiento y promover la flexibilidad en los procesos de aprendizaje.",
        "explicación_modalidades": "El programa virtual se desarrolla mediante una plataforma LMS (Learning Management System) que integra recursos sincrónicos y asincrónicos. Los estudiantes acceden a contenidos multimedia, participan en foros de discusión, desarrollan trabajos colaborativos y asisten a sesiones en vivo con expertos nacionales e internacionales. La metodología incluye estudios de caso, simulaciones de campañas políticas y análisis de contextos electorales reales.",
        "diferenciadores_programa": "El programa se diferencia por: 1) Enfoque práctico con simulaciones de campañas reales, 2) Uso de herramientas de analítica digital y Big Data aplicadas al marketing político, 3) Módulos especializados en comunicación digital y redes sociales, 4) Alianzas con organizaciones políticas para prácticas profesionales, 5) Enfoque en ética y transparencia electoral, 6) Análisis de contextos políticos latinoamericanos, 7) Metodología de aprendizaje basado en proyectos con casos colombianos."
    }
}

crear_programa_doc = {
    "operation_summary": "Crear una nueva justificacion de programa",
    "operation_description": (
        "Este endpoint permite registrar la justificacion del programa."
        "Utiliza validaciones de serializer"
        "bla bla bla"
    ),
    "tags": ["Justificacion Programa"],
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
            description="Justificacion creada exitosamente",
            schema=JustificacionProgramaSerializer,
        ),
        400: openapi.Response(
            description="Error de ingreso/validacion de los datos enviados"
        ),
    },
}
