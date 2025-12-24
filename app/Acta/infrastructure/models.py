from django.conf import settings
from django.db import models
from app.Core.infrastructure.models.models import RegistroCalificado


class Acta(models.Model):
    llave_maestra = models.ForeignKey(
        RegistroCalificado,
        to_field="llave_documento",
        on_delete=models.CASCADE,
        related_name="acta",
        null=True,
        blank=True,
    )

    etiquetas_dinamicas = models.JSONField(
        "Campos adicionales",
        default=dict,
        blank=True,
        help_text="Diccionario con etiquetas dinamicas definidas por el usuario",
    )

    estatus = models.BooleanField(
        default=False,
        help_text="Indica si el acta ha sido validada como correcta"
    )

    aprobado = models.BooleanField(
        null=True,
        default=None,
        help_text="Indica si el director de escuela lo aprobó"
    )

    aprobado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="actas_aprobadas",
    )

    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="actas_creadas",
    )

    modificado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="actas_modificadas",
    )

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.llave_maestra.llave_documento) if self.llave_maestra else "Sin llave maestra"
