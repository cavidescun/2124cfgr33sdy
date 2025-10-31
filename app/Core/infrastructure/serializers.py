from rest_framework import serializers


class GenerarDocumentoSerializer(serializers.Serializer):
    snies = serializers.CharField(max_length=255)
