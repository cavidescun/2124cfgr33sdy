from rest_framework import serializers


class UnificarResponseSerializer(serializers.Serializer):
    llave_maestra = serializers.CharField()


from rest_framework import serializers
from app.Core.infrastructure.models.models_snies import ProgramaAcademico


class ProgramaAcademicoSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField(read_only=True)

    class Meta:
        model = ProgramaAcademico
        fields = [
            "codigo_snies_del_programa",
            "nombre_del_programa",
            "nombre_institucion",
            "nivel_academico",
            "modalidad",
            "score",
        ]
