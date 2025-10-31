class FormularioPosgradoMapper:
    """Convierte datos del formulario en etiquetas dinámicas limpias."""

    FIELD_MAPPING = {
        "Nombre de la Especialización": "nombre_de_programa",
        "Título de la Especialización a otorgar": "título_especialista",
        "Perfil de la Especialización": "perfil_especialista",
        "Duración de la Especialización (meses)": "Duracion_programa",
        "Regional(es)": "Regional_programa",
        "Periodicidad Admisión": "Periodicidad_programa",
        "Cantidad Estudiantes 1er Semestre": "Admitidos_programa",
        "Modalidad": "Modalidad_programa",
        "Campo Amplio": "campo_amplio",
        "Campo Específico": "campo_especifico",
        "Campo Detallado": "campo_detallado",
        "Área del Conocimiento": "área_de_conocimiento",
        "Núcleo Básico del Conocimiento": "núcleo_básico_conocimiento",
        "Programas Similares": "programas_similares",
    }

    @classmethod
    def to_etiquetas(cls, data_fields: dict) -> dict:
        """Devuelve un diccionario limpio con la estructura {'variables': {...}}"""
        etiquetas = {
            cls.FIELD_MAPPING[name]: field["value"]
            for field in data_fields.values()
            if (name := field.get("name")) in cls.FIELD_MAPPING
        }
        return {"variables": etiquetas}
