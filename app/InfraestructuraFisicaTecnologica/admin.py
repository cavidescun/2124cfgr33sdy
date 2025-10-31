from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from .models import InfraestructuraFisicaTecnologica


@admin.register(InfraestructuraFisicaTecnologica)
class DenominacionProgramaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }
    list_display = ("llave_maestra",)
    search_fields = ("llave_maestra",)
    readonly_fields = ("creado_en", "actualizado_en")

    readonly_fields = ("creado_en", "actualizado_en")

    fieldsets = (
        (
            "Etiquetas dinámicas",
            {
                "fields": ("etiquetas_dinamicas",),
                "description": "Agrega o edita etiquetas dinámicas en formato JSON (usa comillas dobles)",
            },
        ),
        (
            "Auditoría",
            {
                "fields": ("creado_en", "actualizado_en"),
            },
        ),
    )
