from rest_framework import serializers

class AcuerdoResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    llave_maestra = serializers.CharField()
    creado_en = serializers.DateTimeField()

class AcuerdoDetailResponseSerializer(AcuerdoResponseSerializer):
    actualizado_en = serializers.DateTimeField(required=False)
    creado_por_id = serializers.IntegerField(required=False)
    etiquetas_dinamicas = serializers.DictField(required=False)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        etiquetas = data.get("etiquetas_dinamicas")
        if etiquetas:
            if "etiquetas_dinamicas" in etiquetas:
                data["etiquetas_dinamicas"] = etiquetas["etiquetas_dinamicas"]
        return data
    