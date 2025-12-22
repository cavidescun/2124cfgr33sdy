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



class ProyeccionFinancieraUpdateSerializer(serializers.Serializer):
    llave_id = serializers.CharField(required=True)
    etiquetas_dinamicas = serializers.DictField(child=serializers.DictField())

    def validate(self, data):
        container = self.context["container"]
        obtener_uc = container.proyeccion_financiera().obtener_proyeccionFinanciera()
        acuerdo = obtener_uc.ejecutar(llave_id=data["llave_id"])

        if not acuerdo:
            raise serializers.ValidationError({"error": "Programa no encontrado"})

        data["acuerdo"] = acuerdo

        etiquetas_raw = acuerdo.etiquetas_dinamicas

        if "variables" in etiquetas_raw:
  
            actuales = etiquetas_raw["variables"]
        else:
            # Estructura anidada (lo que TIENES actualmente)
            actuales = etiquetas_raw.get("etiquetas_dinamicas", {}).get("variables", {})

        # Nuevos datos enviados por el usuario
        nuevas = data["etiquetas_dinamicas"].get("variables", {})

        # Validar tipos
        if not isinstance(nuevas, dict):
            raise serializers.ValidationError(
                {"error": "El campo 'variables' debe ser un objeto."}
            )

        # Buscar campos no válidos
        campos_invalidos = set(nuevas.keys()) - set(actuales.keys())
        if campos_invalidos:
            raise serializers.ValidationError(
                {
                    "error": [
                        "No se pueden actualizar campos no existentes.",
                        f"Campos inválidos: {list(campos_invalidos)}"
                    ]
                }
            )

        # Guardar validaciones
        data["campos_actualizados"] = list(nuevas.keys())

        # Fusionar los datos
        actuales_actualizados = {**actuales, **nuevas}

        # Mantener la misma estructura del ACTA
        if "variables" in etiquetas_raw:
            # Estructura simple
            data["etiquetas_finales"] = {
                "variables": actuales_actualizados
            }
        else:
            # Estructura anidada
            data["etiquetas_finales"] = {
                "etiquetas_dinamicas": {
                    "variables": actuales_actualizados
                }
            }

        return data