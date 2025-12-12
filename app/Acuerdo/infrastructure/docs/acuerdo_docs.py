from drf_yasg import openapi

formulario_posgrado_example = {
  "llave_maestra": "LLAVE-5BE573CF",
  "etiquetas_dinamicas": {
    "variables": {
      "busqueda_snies": 2123,
      "fecha": "21/11/2025",
      "dia": "21",
      "mes": "11",
      "año": "2025",
      "proceso": "nuevo",
      "numero_acta": "20245896",
      "snies": "20245896",
      "numero_acuerdo": "20245896",
      "modalidad_programa": "Presencial",
      "Ciudades": "bogota",
      "ciclo": "Especialización",
      "nombre_de_programa_tp": ",Arquitectura",
      "título_especialista": "Especialista en Arquitectura",
      "num_creditos": "90",
      "duracion_programa": 12233,
      "periodicidad_programa": "Semestral",
      "admitidos_programa": 22,
      "componente_procedeutico": 22,
      "nombre_de_programa_tg": ",Arquitectura",
      "título_especialista": "Especialista en Arquitectura",
      "num_creditos": "90",
      "duracion_programa": 12233,
      "periodicidad_programa": "Semestral",
      "admitidos_programa": 22,
      "componente_procedeutico": 22,
      "nombre_de_programa_pro": ",Arquitectura",
      "título_especialista": "Especialista en Arquitectura",
      "num_creditos": "90",
      "duracion_programa": 12233,
      "periodicidad_programa": "Semestral",
      "admitidos_programa": 22,
      "componente_procedeutico": 22,
      "nombre_de_programa": ",Arquitectura",
      "título_especialista": "Especialista en Arquitectura",
      "num_creditos": "90",
      "duracion_programa": 12233,
      "periodicidad_programa": "Semestral",
      "admitidos_programa": 22,
      "componente_procedeutico": 22
    }
  }
}

crear_acuerdo_doc = {
    "operation_summary": "crear un acuerdo de programa",
    "operation_description": " crea un acuerdo en la estructura JSON.",
    "tags": ["Acuerdo"],
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        example=formulario_posgrado_example
    ),
    "responses": {
        200: openapi.Response(
            description="Acuerdo creado exitosamente",
        ),
        400: openapi.Response(
            description="Error de validacion"
        )
    }
}

obtener_acuerdo_doc = {
    "operation_summary": "Obtener un acuerdo de programa",
    "operation_description": " Obtener un acuerdo en la estructura JSON.",
    "tags": ["Acuerdo"],
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
            description="Acuerdo creado exitosamente",
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

actualizar_acuerdo_doc = {
    "operation_summary": "Actualizar parcialmente un acuerdo de programa",
    "operation_description": "Permite actualizar uno o varios campos de un acuerdo existente. Solo es necesario enviar los campos que se desean modificar dentro de 'etiquetas_dinamicas.variables'.",
    "tags": ["Acuerdo"],
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
        description="Enviar solo los campos que se desean actualizar. Se puede actualizar 'llave_maestra' o cualquier campo dentro de 'etiquetas_dinamicas.variables'",
        example={
            "etiquetas_dinamicas": {
                "variables": {
                    "proceso": "modificacion",
                    "numero_acta": "20245900",
                    "modalidad_programa": "Virtual",
                    "Ciudades": "medellin",
                    "num_creditos": "100",
                    "duracion_programa": 15000,
                    "admitidos_programa": 30
                }
            }
        }
    ),
    "responses": {
        200: openapi.Response(
            description="Acuerdo actualizado exitosamente",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={
                    "message": "Acuerdo actualizado exitosamente",
                    "llave_id": "LLAVE-5BE573CF",
                    "campos_actualizados": [
                        "proceso",
                        "numero_acta",
                        "modalidad_programa",
                        "Ciudades",
                        "num_creditos",
                        "duracion_programa",
                        "admitidos_programa"
                    ]
                }
            )
        ),
        400: openapi.Response(
            description="Error de validación",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={"error": "Datos inválidos", "detalles": "El campo 'num_creditos' debe ser numérico"}
            )
        ),
        404: openapi.Response(
            description="Acuerdo no encontrado",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={"error": "Acuerdo no encontrado con el llave_id proporcionado"}
            )
        )
    }
}