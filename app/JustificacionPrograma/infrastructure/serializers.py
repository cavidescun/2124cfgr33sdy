from rest_framework import serializers

from app.shared.validators.fields import LlaveMaestraField
from .models import JustificacionPrograma


class JustificacionProgramaSerializer(serializers.ModelSerializer):
    llave_maestra = LlaveMaestraField()

    class Meta:
        model = JustificacionPrograma
        fields = "__all__"

        def validate_etiquetas_dinamicas(self, value):
            if value is None:
                raise serializers.ValidationError(
                    "El campo etiquetas dinamicas no puede ser nulo"
                )
            if not isinstance(value, dict):
                raise serializers.ValidationError(
                    "El campo debe ser un JSON (clave: valor)"
                )
            if not value:
                raise serializers.ValidationError(
                    "Las claves del JSON no pueden estar vacias."
                )
            for k, v in value.items():
                if not k.strip():
                    raise serializers.ValidationError(
                        "Las claves del JSON no puedes estar vacias."
                    )
                if v in [None, ""]:
                    raise serializers.ValidationError(
                        f"El valor de la clave '{k}' no puede estar vacio"
                    )
            return value
