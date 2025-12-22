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