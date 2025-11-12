from django.db import models


class PromptTemplateModel(models.Model):
    """Modelo para almacenar templates de prompts"""
    nombre_etiqueta = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nombre de la etiqueta",
        help_text="Identificador único para el template"
    )
    prompt_template = models.TextField(
        verbose_name="Template del prompt",
        help_text="Prompt con placeholders {variable}"
    )
    descripcion = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descripción",
        help_text="Descripción del propósito del template"
    )
    activo = models.BooleanField(
        default=True,
        verbose_name="Activo"
    )
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Template de Prompt"
        verbose_name_plural = "Templates de Prompts"
        ordering = ['nombre_etiqueta']
    
    def __str__(self):
        return self.nombre_etiqueta


class AnalisisIA(models.Model):
    """Modelo para almacenar análisis realizados por IA"""
    nombre_etiqueta = models.CharField(
        max_length=100,
        verbose_name="Nombre de la etiqueta"
    )
    prompt_usado = models.TextField(
        verbose_name="Prompt usado"
    )
    datos_entrada = models.JSONField(
        verbose_name="Datos de entrada",
        help_text="JSON con los datos analizados"
    )
    resultado = models.TextField(
        verbose_name="Resultado del análisis"
    )
    creado_en = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Análisis de IA"
        verbose_name_plural = "Análisis de IA"
        ordering = ['-creado_en']
    
    def __str__(self):
        return f"{self.nombre_etiqueta} - {self.creado_en.strftime('%Y-%m-%d %H:%M')}"