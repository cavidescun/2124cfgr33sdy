from django.urls import path

from .views import ProyeccionFinancieraView

urlpatterns = [
    path("",ProyeccionFinancieraView.as_view(), name="proyeccion_financiera" ),
]