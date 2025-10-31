from rest_framework import serializers


class DataFieldSerializer(serializers.Serializer):
    """Serializer para cada campo individual en 'data'"""
    value = serializers.JSONField()
    name = serializers.CharField()


class FormularioPosgradoSerializer(serializers.Serializer):
    """Serializer principal para el formulario de posgrados especialización"""

    form_title = serializers.CharField(max_length=255)
    form_slug = serializers.CharField(max_length=255)
    data = serializers.DictField(
        child=DataFieldSerializer(),
        required=True
    )

    def validate_data(self, value):
        # Lista de campos requeridos (igual que antes)
        required_field_ids = [
            '6b63f530-fe21-43be-832a-8be7cdfaba44',
            '96c39513-5d58-4979-8e16-3bf78c523c45',
            '4434fb70-2094-4bae-8314-41008a8ebab7',
            'bbf86bf9-d17f-4371-81b2-159de62557db',
            '62938ce0-a586-4c81-9770-9fcfd82c4e8b',
            'bc15299c-b749-4d46-ae83-6532e817047d',
            '6ccc8d23-6e2d-4d2e-b992-c23a946c8728',
            '36a2ae22-2d8a-47e1-bee1-2a45e076f5b8',
            '85b056d2-9615-4a0f-85ac-dbed244323cc',
            '231d56b0-15c6-49bf-9e56-ead5c4e9ae9b',
            '5fd9aeab-37b2-4912-a6eb-b9d87e9fc9d1',
            '3ec69789-767c-46ba-ad64-5dde43bbe176',
            '2bd970b5-ff5f-4607-b074-da8abece915e',
            '7a188ea4-35c8-42fb-ac91-a460e1bc4a0f',
            'd9429034-212d-4cd1-9db5-8de85a5a4a1e',
            '9d442c2e-9954-4d96-b939-eaa3526b54c8',
            '6b31f7af-3038-4410-b685-5157f4fe9cfd',
            'c621eb85-74c3-46ef-b232-3a20cf29ccf4',
            'a6e711ec-4ff0-4b4a-b883-a480dddd3df4',
            '9a230edc-5ea6-4536-a008-dbd997b64369',
            'b57cd6a5-3ac7-4d2a-b97a-5096f53d79ed',
            '49d5a80c-2e65-47d8-b3a7-3fa13d06b41c',
            '88d8286e-7a4d-4a04-aa63-084457b3c2c3',
        ]
        missing_fields = [fid for fid in required_field_ids if fid not in value]
        if missing_fields:
            raise serializers.ValidationError(f"Faltan campos requeridos: {missing_fields}")
        return value

    def validate(self, data):
        # Validación de slug
        if data.get('form_title') == 'Formulario Posgrados Especialización':
            if not data.get('form_slug', '').startswith('formulario-posgrados-especializacion'):
                raise serializers.ValidationError({
                    'form_slug': 'El form_slug no corresponde con el form_title'
                })
        return data

    def to_representation(self, instance):
        """Crea una salida JSON limpia y semántica"""
        data = instance.get("data", {})
        clean_output = {}

        # Mapeo de nombres originales a etiquetas de salida más legibles
        field_mapping = {
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

        # Recorremos los campos y aplicamos el mapeo
        for field in data.values():
            name = field.get("name")
            value = field.get("value")
            key = field_mapping.get(name)
            if key:
                clean_output[key] = value

        return {"variables": clean_output}
