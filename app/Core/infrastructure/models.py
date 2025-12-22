from django.db import models


class RegistroCalificado(models.Model):
    llave_documento = models.CharField(
        "Llave del documento", max_length=300, unique=True
    )
    tipo = models.CharField("Tipo de documento", max_length=50, null=True, blank=True)
    numero_acta = models.CharField("acta", max_length=50, unique=True, null=True, blank=True)
    unificado = models.BooleanField(
        null=True,
        default=False,
        help_text="Indica si ya se realizo la unificacion"
    )
    snies = models.CharField("SNIES", max_length=50, unique=True, null=True, blank=True)
    informe_final = models.JSONField(
        "Campos adicionales",
        default=dict,
        blank=True,
        help_text="Diccionario con etiquetas dinamicas definidas por el usuario",
    )
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.llave_documento


