from rest_framework import serializers
class CampoFormSerializer(serializers.Serializer):
    name = serializers.CharField()
    label = serializers.CharField()
    type = serializers.CharField()
    options = serializers.ListField(
        child=serializers.CharField(), required=False, allow_empty=True
    )
    value = serializers.JSONField(required=False, allow_null=True)

    def validate(self, data):
        if data.get("type") in ["text", "textarea", "email"]:
            if not data.get("value"):
                raise serializers.ValidationError(
                    {data["name"]: f"El campo '{data['label']}' no puede estar vacío."}
                )
        if data.get("type") in ["select", "multiselect"]:
            opciones = data.get("options", [])
            valor = data.get("value")
            if opciones:
                if data["type"] == "select" and valor not in opciones:
                    raise serializers.ValidationError(
                        {data["name"]: f"El valor '{valor}' no es una opción válida."}
                    )
                elif data["type"] == "multiselect":
                    if not all(v in opciones for v in valor):
                        raise serializers.ValidationError(
                            {data["name"]: f"Una o más opciones seleccionadas no son válidas."}
                        )

        if data.get("type") == "email":
            from django.core.validators import validate_email
            try:
                validate_email(data.get("value", ""))
            except Exception:
                raise serializers.ValidationError(
                    {data["name"]: f"El campo '{data['label']}' debe ser un correo válido."}
                )

        return data


class FormularioSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.CharField()
    fields = CampoFormSerializer(many=True)

    def validate_fields(self, value):
        """
        Validar que la lista de campos no esté vacía.
        """
        if not value:
            raise serializers.ValidationError("El formulario debe tener al menos un campo.")
        return value


class FormularioPosgradoSerializer(serializers.Serializer):
    form = FormularioSerializer()

    def validate(self, data):
        """
        Validaciones generales del formulario.
        """
        form = data.get("form", {})
        if not form.get("title"):
            raise serializers.ValidationError("El título del formulario no puede estar vacío.")
        return data
class ActaQuerySerializer(serializers.Serializer):
    acta_id = serializers.IntegerField(
        required=True,
        help_text="ID del acta que se desea obtener"
    )