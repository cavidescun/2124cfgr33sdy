from rest_framework import serializers


from app.shared.validators.fields import LlaveMaestraField


class UnificacionInformacionSerializer(serializers.Serializer):
    llave_maestra = LlaveMaestraField()

class GenerarDocumentoSerializer(serializers.Serializer):
    llave_maestra = LlaveMaestraField()



class PuntoControlQuerySerializer(serializers.Serializer):
    llave_maestra = serializers.CharField(
        required=True,
        help_text="Identificador único del proceso",
        error_messages={
            "required": "El parámetro llave_maestra es obligatorio"
        }
    )

class BuscarProgramasSimilaresQuerySerializer(serializers.Serializer):
    campo_amplio = serializers.CharField(required=False, allow_blank=True)
    campo_especifico = serializers.CharField(required=False, allow_blank=True)
    campo_detallado = serializers.CharField(required=False, allow_blank=True)
    area_conocimiento = serializers.CharField(required=False, allow_blank=True)
    nucleo_basico = serializers.CharField(required=False, allow_blank=True)

    def validate(self, data):
        if not any(data.values()):
            raise serializers.ValidationError(
                "Debe enviar al menos un parámetro de búsqueda."
            )
        return data