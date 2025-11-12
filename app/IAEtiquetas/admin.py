from django.contrib import admin
from .infrastructure.models import PromptTemplateModel, AnalisisIA


@admin.register(PromptTemplateModel)
class PromptTemplateAdmin(admin.ModelAdmin):
    list_display = ('nombre_etiqueta', 'descripcion', 'activo', 'actualizado_en')
    search_fields = ('nombre_etiqueta', 'descripcion')
    list_filter = ('activo', 'creado_en')
    readonly_fields = ('creado_en', 'actualizado_en')
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre_etiqueta', 'descripcion', 'activo')
        }),
        ('Template', {
            'fields': ('prompt_template',),
            'description': 'Usa {datos} para insertar todos los datos como JSON, o {campo} para campos específicos'
        }),
        ('Auditoría', {
            'fields': ('creado_en', 'actualizado_en'),
            'classes': ('collapse',)
        }),
    )


@admin.register(AnalisisIA)
class AnalisisIAAdmin(admin.ModelAdmin):
    list_display = ('nombre_etiqueta', 'creado_en')
    search_fields = ('nombre_etiqueta', 'resultado')
    list_filter = ('nombre_etiqueta', 'creado_en')
    readonly_fields = ('creado_en',)
    
    fieldsets = (
        ('Información', {
            'fields': ('nombre_etiqueta', 'creado_en')
        }),
        ('Prompt', {
            'fields': ('prompt_usado',),
            'classes': ('collapse',)
        }),
        ('Datos', {
            'fields': ('datos_entrada',),
            'classes': ('collapse',)
        }),
        ('Resultado', {
            'fields': ('resultado',)
        }),
    )