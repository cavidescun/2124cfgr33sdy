from django.db import models
from django.core.validators import MinValueValidator

from app.Core.infrastructure.models import RegistroCalificado


class DenominacionPrograma(models.Model):
    etiquetas_dinamicas = models.JSONField(
        "Campos adicionales",
        default=dict,
        blank=True,
        help_text="Diccionario con etiquetas dinámicas definidas por el usuario",
    )

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    llave_maestra = models.ForeignKey(
        RegistroCalificado,
        to_field="llave_documento",
        on_delete=models.CASCADE,
        related_name="denominacion_programa",
        null=True,
        blank=True,
    )

    def __str__(self):
        return (
            str(self.llave_maestra.llave_documento)
            if self.llave_maestra
            else "Sin llave maestra"
        )
