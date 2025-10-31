from rest_framework import serializers
import re


class LlaveMaestraSerializer(serializers.Serializer):
    llave_maestra = serializers.CharField(required=True, allow_blank=False)

    def validate_llave_maestra(self, value):
      
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "La llave maestra no puede estar vacía ni contener solo espacios en blanco."
            )



        return value
