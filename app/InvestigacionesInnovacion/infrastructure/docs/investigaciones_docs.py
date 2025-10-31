from drf_yasg import openapi
from ..serializers import InvestigacionesInnovacionSerializer

etiquetas_dinamicas_example ={
"variables": {
    "nombre_de_programa": "Gerencia de Proyectos",
    "escuela_datos": "Transformación Empresarial",
    "grupos_investigacion": "Gidecer",
    "grupos_interinstitucionales": "Sigcienty y Armos",
    "lineas_investigacion": "Gestión organizacional, emprendimiento e innovación empresarial",
    
    "lineasescuela": [
      {
        "lineas_escuela": "Gestión Organizacional y Empresarial"
      },
      {
        "lineas_escuela": "Emprendimiento e Innovación"
      },
      {
        "lineas_escuela": "Transformación Digital y Tecnologías Emergentes"
      },
      {
        "lineas_escuela": "Responsabilidad Social Empresarial"
      }
    ],
    
    "lineasdelprograma": [
      {
        "lineas_programas": "Gestión Estratégica de Proyectos",
        "programas_academico": "Especialización en Gerencia de Proyectos"
      },
      {
        "lineas_programas": "Innovación y Transformación en Proyectos",
        "programas_academico": "Especialización en Gerencia de Proyectos"
      },
      {
        "lineas_programas": "Gestión Financiera y de Riesgos en Proyectos",
        "programas_academico": "Especialización en Gerencia de Proyectos"
      }
    ],
    
    "plan_desarrollo_investigativo": [
      {
        "objetivo": "Fortalecer los aspectos institucionales de investigación en el programa académico",
        "estrategia": "Generar las líneas de investigación de carácter disciplinar y multidisciplinar. Incorporar en la reflexión elementos tecnológicos de importancia institucional como la IA, las Industrias 5.0 y otras tecnologías emergentes",
        "tactica": "Realizar una exploración de las líneas de investigación institucionales que permita definir por lo menos dos áreas temáticas de investigación del programa de manera articulada con las orientaciones institucionales",
        "periodo": "2025-2032",
        "resultado": "Por lo menos dos líneas de investigación o áreas temáticas de interés investigativo para el programa académico en sintonía con las temáticas institucionales",
        "indicador": "Documento escrito",
        "responsable": "Programa Académico - Dirección Nacional de Investigación - Investigadores"
      },
      {
        "objetivo": "Fortalecer los aspectos institucionales de investigación en el programa académico",
        "estrategia": "Implementar el plan de capacitación desde la DNI para investigadores y personal administrativo",
        "tactica": "Construir el plan de capacitación del desarrollo humano de los investigadores de la Dirección Nacional de Investigación",
        "periodo": "2025-2032",
        "resultado": "Ejecución de las actividades contempladas en el plan de trabajo y capacitación del desarrollo humano anual del Investigador",
        "indicador": "Sesiones grabadas de capacitación",
        "responsable": "Programa Académico - Dirección Nacional de Investigación - Investigadores"
      },
      {
        "objetivo": "Fortalecer los aspectos institucionales de investigación en el programa académico",
        "estrategia": "Fortalecer los grupos de investigación existentes que impactan al programa académico",
        "tactica": "Adelantar las actividades necesarias para mantener y mejorar los resultados de categorización de los grupos",
        "periodo": "2025-2032",
        "resultado": "Cumplimiento de actividades previstas en el plan de Categorización de Grupos de Investigación",
        "indicador": "Resultados de convocatoria de medición de grupos Minciencias",
        "responsable": "Programa Académico - Dirección Nacional de Investigación - Investigadores"
      },
      {
        "objetivo": "Fortalecer los aspectos institucionales de investigación en el programa académico",
        "estrategia": "Mantener activa la investigación institucional",
        "tactica": "Liderar el proceso interno de Convocatorias para proyectos de investigación que impacten al programa académico",
        "periodo": "2025-2032",
        "resultado": "Realización de Convocatorias de periodicidad anual o en los tiempos que la DNI considere",
        "indicador": "Actas de Inicio de los Proyectos de Investigación",
        "responsable": "Programa Académico - Dirección Nacional de Investigación - Investigadores"
      },
      {
        "objetivo": "Fortalecer los aspectos institucionales de investigación en el programa académico",
        "estrategia": "Contribuir al fortalecimiento de las actividades de interacción entre las funciones sustantivas",
        "tactica": "Adelantar actividades con la participación conjunta de otras áreas de la institución",
        "periodo": "2025-2032",
        "resultado": "Generación de actividades de interacción con la participación de las áreas correspondientes",
        "indicador": "No. de participantes",
        "responsable": "Programa Académico - Dirección Nacional de Investigación - Otras áreas - Investigadores"
      },
      {
        "objetivo": "Promover los escenarios de investigación formativa",
        "estrategia": "Contribuir al fortalecimiento de los Semilleros de investigación con estudiantes pertenecientes al Programa",
        "tactica": "Generar escenarios de capacitación sobre la importancia y las actividades de los Semilleros. Realizar convocatorias periódicas para la conformación de Semilleros de Investigación",
        "periodo": "2025-2032",
        "resultado": "Por lo menos un (1) semilleros de investigación para cada programa académico",
        "indicador": "Acta de Constitución de los Semilleros",
        "responsable": "Programa Académico - Dirección Nacional de Investigación - Investigadores"
      },
      {
        "objetivo": "Promover los escenarios de investigación formativa",
        "estrategia": "Mantener actualizada la información relacionada con los Semilleros de Investigación",
        "tactica": "Implementar una estrategia que permita visibilizar la ruta de inscripción, oficialización y seguimiento de los semilleros de investigación de acuerdo con los lineamientos establecido por la DNI y la Política General de investigación y Creación Artística y Cultural (2017)",
        "periodo": "2025-2032",
        "resultado": "Una (1) estrategia que permita visibilizar la ruta de inscripción, oficialización y seguimiento de los semilleros de investigación",
        "indicador": "Documento Excel",
        "responsable": "Programa Académico - Dirección Nacional de Investigación - Investigadores"
      },
      {
        "objetivo": "Promover los escenarios de investigación formativa",
        "estrategia": "Promover la participación en eventos regionales o nacionales en los cuales se evidencien productos de investigación del semillero",
        "tactica": "Propiciar espacios de socialización institucional de los Semilleros de Investigación. Acompañar la realización de actividades realizadas por los Semilleros de Investigación",
        "periodo": "2025-2032",
        "resultado": "Por lo menos dos (2) eventos regionales o nacionales en los cuales participen los semilleros de programa",
        "indicador": "Registro de participación y asistencia",
        "responsable": "Programa Académico - Dirección Nacional de Investigación - Investigadores"
      },
      {
        "objetivo": "Mejorar la visualización de las prácticas investigativas del programa",
        "estrategia": "Fortalecer las relaciones interinstitucionales que aumenten los niveles de cooperación y cohesión de los grupos y semilleros de investigación",
        "tactica": "Adelantar trabajo colaborativo con el área de Internacionalización. Invitar a los docentes de investigación a participar de redes académicas",
        "periodo": "2025-2032",
        "resultado": "Establecer Relaciones interinstitucionales que aumenten los niveles de cooperación y cohesión de los grupos y semilleros de investigación",
        "indicador": "Actas de reunión - Certificación de vinculación a redes académicas e interinstitucionales",
        "responsable": "Programa Académico - Dirección Nacional de Investigación - Investigadores"
      },
      {
        "objetivo": "Mejorar la visualización de las prácticas investigativas del programa",
        "estrategia": "Apoyar la organización de eventos académicos en los cuales se presenten resultados parciales y finales de investigación",
        "tactica": "Organizar la realización de eventos institucionales (v. gr. Semana de la Investigación, Semana Cunista, etc.)",
        "periodo": "2025-2032",
        "resultado": "Un (1) evento académico anual en los cuales se presenten resultados parciales y finales de investigación",
        "indicador": "Certificación de la participación",
        "responsable": "Programa Académico - Dirección Nacional de Investigación - Investigadores"
      },
      {
        "objetivo": "Mejorar la visualización de las prácticas investigativas del programa",
        "estrategia": "Apoyar la participación de docentes como ponentes en eventos académicos nacionales e internacionales",
        "tactica": "Gestionar la participación de los docentes en eventos académicos",
        "periodo": "2025-2032",
        "resultado": "Apoyar la participación de tres (3) docentes como ponentes en eventos académicos nacionales e internacionales",
        "indicador": "Certificación de participación",
        "responsable": "Programa Académico - Dirección Nacional de Investigación - Investigadores"
      },
      {
        "objetivo": "Mejorar la visualización de las prácticas investigativas del programa",
        "estrategia": "Apoyar el desarrollo de convenios interinstitucionales para la concreción de redes académicas y de conocimiento",
        "tactica": "Adelantar trabajo colaborativo con el área de Internacionalización. Invitar a los docentes de investigación a participar de redes académicas",
        "periodo": "2025-2032",
        "resultado": "Apoyar el desarrollo de dos (2) convenios interinstitucionales para la concreción de redes académicas y de conocimiento",
        "indicador": "Actas de reunión - Certificación de vinculación a redes académicas e interinstitucionales - Generar productos de investigación pertenecientes a las tipologías establecidas por Minciencias - Generar espacios de capacitación sobre la importancia y el contenido del Modelo de Medición de Minciencias - Establecer un plan de trabajo de periodicidad anual - Establecer actividades de seguimiento y control que garanticen el cumplimiento del plan de trabajo",
        "responsable": "Programa Académico - Dirección Nacional de Investigación - Investigadores"
      },
      {
        "objetivo": "Mejorar la visualización de las prácticas investigativas del programa",
        "estrategia": "Generar productos de investigación pertenecientes a las tipologías establecidas por Minciencias. Generar espacios de capacitación sobre la importancia y el contenido del Modelo de Medición de Minciencias. Establecer un plan de trabajo de periodicidad anual. Establecer actividades de seguimiento y control que garanticen el cumplimiento del plan de trabajo",
        "tactica": "Generar productos de investigación pertenecientes a las tipologías establecidas por Minciencias. Generar espacios de capacitación sobre la importancia y el contenido del Modelo de Medición de Minciencias. Establecer un plan de trabajo de periodicidad anual. Establecer actividades de seguimiento y control que garanticen el cumplimiento del plan de trabajo",
        "periodo": "2025-2032",
        "resultado": "Generar al menos cinco (5) productos de investigación pertenecientes a las tipologías establecidas por Minciencias",
        "indicador": "Certificación de producto",
        "responsable": "Programa Académico - Dirección Nacional de Investigación - Investigadores"
      },
      {
        "objetivo": "Mejorar la visualización de las prácticas investigativas del programa",
        "estrategia": "Implementar una estrategia de seguimiento según los lineamientos de la DNI de actualización de los CvLAC y GrupLAC de investigadores y grupos de investigación",
        "tactica": "Elaborar informes semestrales de producción en investigación de cada grupo e investigador. Establecer actividades de seguimiento y control que garanticen el cumplimiento del plan de trabajo",
        "periodo": "2025-2032",
        "resultado": "Una (1) estrategia de seguimiento según los lineamientos de la DNI de actualización de los CvLAC y GrupLAC de investigadores y grupos de investigación",
        "indicador": "Informes de gestión y/o de resultados según plataforma institucional de seguimiento",
        "responsable": "Programa Académico - Dirección Nacional de Investigación - Investigadores"
      },
      {
        "objetivo": "Mejorar la visualización de las prácticas investigativas del programa",
        "estrategia": "Implementar actividades de mejoramiento continuo desde el factor de Investigación",
        "tactica": "Adelantar las actividades de autoevaluación por área. Organizar y sistematizar la información obtenida",
        "periodo": "2025-2032",
        "resultado": "Por lo menos dos (2) autoevaluaciones del factor o condición de investigación en el programa, con su respectivo plan de mejoramiento realizadas",
        "indicador": "Documento de resultados de la autoevaluación - Plan de mejora",
        "responsable": "Programa Académico - Dirección Nacional de Investigación - Investigadores"
      }
    ],
    
    "fomentoinvestigacion": [
      {
        "nombre_fomento": "Carlos Andrés Martínez López",
        "formacion_fomento": "Doctor en Administración de Empresas",
        "cylac_fomento": "https://scienti.minciencias.gov.co/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0001234567"
      },
      {
        "nombre_fomento": "María Fernanda Rojas Gutiérrez",
        "formacion_fomento": "Doctora en Gestión de Proyectos",
        "cylac_fomento": "https://scienti.minciencias.gov.co/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0001234568"
      },
      {
        "nombre_fomento": "Juan Pablo Vargas Sánchez",
        "formacion_fomento": "Magíster en Ingeniería Industrial",
        "cylac_fomento": "https://scienti.minciencias.gov.co/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0001234569"
      },
      {
        "nombre_fomento": "Ana Carolina Pérez Molina",
        "formacion_fomento": "Magíster en Gestión de Proyectos",
        "cylac_fomento": "https://scienti.minciencias.gov.co/cvlac/visualizador/generarCurriculoCv.do?cod_rh=0001234570"
      }
    ],
   "grupos_investigacion_institucionales": [
      {"escuela": "Ingeniería", "grupo": "Axon", "categoria_minciencias": "A"},
      {"escuela": "Ingeniería", "grupo": "Idecun", "categoria_minciencias": "C"},
      {"escuela": "Ingeniería", "grupo": "Sigcienty (Interinstitucionales)", "categoria_minciencias": "A"},
      {"escuela": "Ingeniería", "grupo": "Armos (Interinstitucionales)", "categoria_minciencias": "C"},
      {"escuela": "Diseño y Comunicación", "grupo": "Codim", "categoria_minciencias": "B"},
      {"escuela": "Transformación Empresarial", "grupo": "Gidecer", "categoria_minciencias": "B"},
      {"escuela": "Transformación Empresarial", "grupo": "Responsabilidad Social Cunista", "categoria_minciencias": "C"},
      {"escuela": "Transformación Empresarial", "grupo": "GirasCUN", "categoria_minciencias": "C"},
      {"escuela": "Transformación Empresarial", "grupo": "Escala", "categoria_minciencias": "C"},
      {"escuela": "Escuela de Ciencias Sociales, Jurídicas y Gobierno", "grupo": "Paz, Desarrollo Territorial e Innovación Educativa", "categoria_minciencias": "C"}
    ],
    "lineas_institucionales_investigacion": [
      {
        "linea": "Gestión y Tecnologías",
        "sublinea_1": "Mejoramiento de procesos organizacionales",
        "sublinea_2": "Adaptación y apropiación de Tecnologías",
        "sublinea_3": "Desarrollo de soluciones técnicas aplicadas"
      },
      {
        "linea": "Innovación Pedagógica",
        "sublinea_1": "Innovación en procesos pedagógicos",
        "sublinea_2": "Desarrollo de pensamiento lógico matemático",
        "sublinea_3": "Aplicación y apropiación de TIC"
      },
      {
        "linea": "Responsabilidad Social",
        "sublinea_1": "Desarrollo sostenible y responsabilidad ambiental",
        "sublinea_2": "Mujer y Sociedad",
        "sublinea_3": "Bienestar institucional y organizacional"
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
    "tags": ["Investigaciones e Innovacion"],
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
            description="Investigaciones creada exitosamente",
            schema=InvestigacionesInnovacionSerializer,
        ),
        400: openapi.Response(
            description="Error de ingreso/validacion de los datos enviados"
        ),
    },
}
