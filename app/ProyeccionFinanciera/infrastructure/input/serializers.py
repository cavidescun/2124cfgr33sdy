from rest_framework import serializers
from django.core.validators import validate_email
from datetime import datetime

from app.shared.validators.fields import LlaveMaestraField

class EtiquetasDinamicasSerializer(serializers.Serializer):
    etiquetas_dinamicas = serializers.DictField()
    llave_maestra = LlaveMaestraField()

    def validate(self, data):
        etiquetas = data.get("etiquetas_dinamicas", {})
        if "variables" not in etiquetas:
            raise serializers.ValidationError({"etiquetas_dinamicas": "Debe contener la clave variables."})
        
        variables = etiquetas.get("variables", {})
        if not isinstance(variables, dict):
            raise serializers.ValidationError({"variables": "El valor de varibales debe ser un objeto"})
        
        errores = {}
        for nombre, valor in variables.items():
            error = self._validar_variable(nombre, valor)
            if error:
                errores[nombre] = error

            if errores:
                raise serializers.ValidationError({"variables": errores})
            
            return data
    
    def _validar_variable(sef, nombre, valor):
        if valor is None or valor == "":
            return "El Campo no puede estar vacio"
        
        # hacer validador para los campos que lo requieran
        return None
    
class ProyeccionFinancieraQuerySerializer(serializers.Serializer):
    llave_id = serializers.CharField(
        required=True,
        help_text="ID del llave_id que desea obtener"
    )