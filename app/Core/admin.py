from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.db import models
from app.Core.infrastructure.models import RegistroCalificado
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
