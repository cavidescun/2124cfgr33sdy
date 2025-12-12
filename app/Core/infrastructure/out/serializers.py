from rest_framework import serializers


class UnificarResponseSerializer(serializers.Serializer):
    llave_maestra = serializers.CharField()


