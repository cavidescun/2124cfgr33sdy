from django.urls import path

from .views import ActividadesAcademicasView

urlpatterns = [
    path("", ActividadesAcademicasView.as_view(), name="crear_actividad_academica"),
]
