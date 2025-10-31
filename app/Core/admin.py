# app/admin.py
from django.contrib import admin
from django.utils.html import format_html

from app.Core.infrastructure.models import RegistroCalificado

from .models import PlantillaDocumento


@admin.register(PlantillaDocumento)
class PlantillaDocumentoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "ver_archivo", "actualizado_en")
    list_filter = ("tipo",)
    search_fields = ("nombre",)

    def ver_archivo(self, obj):
        if obj.archivo:
            return format_html(
                '<a href="{}" target="_blank" rel="noopener noreferrer">📄 Abrir documento</a>',
                obj.archivo.url,
            )
        return "Sin archivo"

    ver_archivo.short_description = "Archivo"


@admin.register(RegistroCalificado)
class RegistroCalificadoAdmin(admin.ModelAdmin):
    list_display = ("llave_documento", "tipo", "snies", "creado_en", "actualizado_en")
    search_fields = ("llave_documento", "tipo", "snies")
    list_filter = ("tipo",)
    ordering = ("-creado_en",)
