from rest_framework import serializers


class AnalizarIARequestSerializer(serializers.Serializer):
    nombre_etiqueta = serializers.CharField(
        required=True,
        max_length=100,
        help_text="Nombre de la etiqueta para buscar el template de prompt"
    )
    datos = serializers.JSONField(
        required=True,
        help_text="Datos a analizar en formato JSON"
    )
    prompt_custom = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True,
        help_text="Prompt personalizado (opcional). Si no se proporciona, se usa el template de la etiqueta"
    )
    
    def validate_datos(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("Los datos deben ser un objeto JSON válido")
        if not value:
            raise serializers.ValidationError("Los datos no pueden estar vacíos")
        return value


class AnalizarIAResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre_etiqueta = serializers.CharField()
    resultado = serializers.CharField()
    prompt_usado = serializers.CharField()
    datos_entrada = serializers.JSONField()
    creado_en = serializers.DateTimeField(read_only=True)


class PromptTemplateSerializer(serializers.Serializer):
    nombre_etiqueta = serializers.CharField(
        max_length=100,
        help_text="Identificador único del template (sin espacios, usar guiones bajos)"
    )
    prompt_template = serializers.CharField(
        help_text="Contenido del prompt. Usa {datos} para el JSON completo o {campo} para campos específicos"
    )
    descripcion = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
        help_text="Descripción del propósito del template"
    )
    
    def validate_nombre_etiqueta(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("El nombre de etiqueta no puede estar vacío")
        
        # Validar que no tenga espacios
        if ' ' in value:
            raise serializers.ValidationError(
                "El nombre de etiqueta no puede contener espacios. Usa guiones bajos (_) o guiones (-)"
            )
        
        return value.strip().lower()
    
    def validate_prompt_template(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("El prompt_template no puede estar vacío")
        return value


class PromptTemplateDetailSerializer(PromptTemplateSerializer):
    creado_en = serializers.DateTimeField(read_only=True)
    actualizado_en = serializers.DateTimeField(read_only=True)
    activo = serializers.BooleanField(read_only=True)


class PromptTemplateCreateRequestSerializer(serializers.Serializer):
    templates = PromptTemplateSerializer(many=True)
    
    def validate_templates(self, value):
        if not value:
            raise serializers.ValidationError("Debe proporcionar al menos un template")
        
        # Validar nombres duplicados
        nombres = [t['nombre_etiqueta'] for t in value]
        if len(nombres) != len(set(nombres)):
            raise serializers.ValidationError("Hay nombres de etiqueta duplicados")
        
        return value