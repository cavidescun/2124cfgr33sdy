from rest_framework import serializers
from django.core.validators import validate_email
from datetime import datetime

from app.shared.validators.fields import LlaveMaestraField


class UnificacionInformacionSerializer(serializers.Serializer):
    llave_maestra = LlaveMaestraField()

class GenerarDocumentoSerializer(serializers.Serializer):
    llave_maestra = LlaveMaestraField()

