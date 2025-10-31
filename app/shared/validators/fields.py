# app/shared/fields.py
from rest_framework import serializers
from app.shared.validators.validators import validar_llave_maestra


class LlaveMaestraField(serializers.CharField):
    def to_internal_value(self, data):
        # Convierte directamente a instancia de RegistroCalificado
        return validar_llave_maestra(data)
