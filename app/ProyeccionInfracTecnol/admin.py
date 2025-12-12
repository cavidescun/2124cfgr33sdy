from django.contrib import admin
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from .models import ProyeccionInfracTecnol

@admin.register(ProyeccionInfracTecnol)
class ProyeccionInfracTecnolAdmin(admin.ModelAdmin):
    formfield_overrrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }

    list_display = ("llave_maestra",)
    search_fields = ("llave_maestra",)
    readonly_fields = ("creado_en", "actualizado_en")

    fieldsets = (
        (
            "Informacion General",
            {
                "fields": ("llave_maestra",),
            },
        ),
        (
            "Etiquetas dinamicas",
            {
                "fields": ("etiquetas_dinamicas",),
                "description": "Agrega o edita etiquetas dinamicas en formato JSON(usa comillas dobles)",
            },
        ),
        (
            "Auditoria",
            {
                "fields":("creado_en","actualizado_en")
            }
        )
    )
