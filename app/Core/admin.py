from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.db import models
from app.Core.infrastructure.models.models import RegistroCalificado
from app.Core.infrastructure.models.models_snies import *
from django_json_widget.widgets import JSONEditorWidget
admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Información personal'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Fechas importantes'), {'fields': ('last_login', 'date_joined')}),
    )

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)




@admin.register(RegistroCalificado)
class RegistroCalificadoAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }

    list_display = (
        "llave_documento",
        "unificado",
        "tipo",
        "snies",
        "creado_en",
        "actualizado_en",
    )

    list_editable = ("unificado",)  

    search_fields = ("llave_documento", "tipo", "snies")
    list_filter = ("tipo", "unificado")
    ordering = ("-creado_en",)


"""
Configuración del admin de Django para los modelos SNIES
"""



@admin.register(CampoAmplio)
class CampoAmplioAdmin(admin.ModelAdmin):
    list_display = ('id_amplio', 'nombre_amplio')
    search_fields = ('id_amplio', 'nombre_amplio')
    list_filter = ('nombre_amplio',)
    
    def get_queryset(self, request):
        return super().get_queryset(request).using('snies')


@admin.register(ProgramaAcademico)
class ProgramaAcademicoAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_snies_del_programa',
        'nombre_del_programa',
        'nombre_institucion',
        'estado_programa',
        'nivel_de_formacion',
        'modalidad',
        'departamento_oferta_programa',
        'municipio_oferta_programa'
    )
    list_filter = (
        'estado_programa',
        'nivel_academico',
        'nivel_de_formacion',
        'modalidad',
        'sector',
        'caracter_academico',
        'departamento_oferta_programa',
        'programa_en_convenio'
    )
    search_fields = (
        'codigo_snies_del_programa',
        'nombre_del_programa',
        'nombre_institucion',
        'codigo_institucion',
        'titulo_otorgado',
        'municipio_oferta_programa'
    )
    readonly_fields = (
        'fecha_de_registro_en_snies',
        'fecha_carga',
        'fecha_actualizacion',
        'fila_excel'
    )
    
    fieldsets = (
        ('Información de la Institución', {
            'fields': (
                'codigo_institucion_padre',
                'codigo_institucion',
                'nombre_institucion',
                'estado_institucion',
                'caracter_academico',
                'sector'
            )
        }),
        ('Información del Programa', {
            'fields': (
                'registro_unico',
                'codigo_snies_del_programa',
                'codigo_anterior_icfes',
                'nombre_del_programa',
                'titulo_otorgado',
                'estado_programa'
            )
        }),
        ('Reconocimiento y Aprobación', {
            'fields': (
                'justificacion',
                'justificacion_detallada',
                'reconocimiento_del_ministerio',
                'resolucion_de_aprobacion',
                'fecha_de_resolucion',
                'fecha_ejecutoria',
                'vigencia_años',
                'fecha_de_registro_en_snies'
            )
        }),
        ('Clasificación CINE y NBC', {
            'fields': (
                'cine_f_2013_ac_campo_amplio',
                'cine_f_2013_ac_campo_especifico',
                'cine_f_2013_ac_campo_detallado',
                'area_de_conocimiento',
                'nucleo_basico_del_conocimiento'
            )
        }),
        ('Características Académicas', {
            'fields': (
                'nivel_academico',
                'nivel_de_formacion',
                'modalidad',
                'numero_creditos',
                'numero_periodos_de_duracion',
                'periodicidad',
                'se_ofrece_por_ciclos_propedeuticos',
                'periodicidad_admisiones'
            )
        }),
        ('Ubicación y Oferta', {
            'fields': (
                'programa_en_convenio',
                'departamento_oferta_programa',
                'municipio_oferta_programa',
                'costo_matricula_estud_nuevos'
            )
        }),
        ('Información Adicional', {
            'fields': (
                'vigencia_transitoria',
                'observacion_decreto_1174_23',
                'fecha_carga',
                'fecha_actualizacion',
                'fila_excel'
            ),
            'classes': ('collapse',)
        })
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).using('snies')
    
@admin.register(ConsolidadoEducacionSuperior)
class ConsolidadoEducacionSuperiorAdmin(admin.ModelAdmin):
    list_display = (
        'anio',
        'semestre',
        'codigo_institucion',
        'institucion',
        'codigo_snies_programa',
        'programa_academico',
        'nivel_formacion',
        'modalidad',
        'total_inscritos',
        'total_admitidos',
        'total_matriculados',
        'total_graduados'
    )
    list_filter = (
        'anio',
        'semestre',
        'nivel_formacion',
        'modalidad',
        'departamento_programa'
    )
    search_fields = (
        'institucion',
        'programa_academico',
        'codigo_snies_programa',
        'municipio_programa'
    )
    ordering = ('-anio', '-semestre', 'institucion')
    
    fieldsets = (
        ('Información Temporal', {
            'fields': ('anio', 'semestre')
        }),
        ('Información Institucional', {
            'fields': (
                'codigo_institucion',
                'institucion'
            )
        }),
        ('Información del Programa', {
            'fields': (
                'codigo_snies_programa',
                'programa_academico',
                'nivel_formacion',
                'modalidad'
            )
        }),
        ('Ubicación', {
            'fields': (
                'departamento_programa',
                'municipio_programa'
            )
        }),
        ('Estadísticas de Estudiantes', {
            'fields': (
                'total_inscritos',
                'total_admitidos',
                'total_matriculados',
                'total_graduados'
            )
        })
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).using('snies')
