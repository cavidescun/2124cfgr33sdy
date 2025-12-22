from django.urls import path

from .views import ProyeccionTecnologicaView

urlpatterns = [
    path("",ProyeccionTecnologicaView.as_view(), name="proyeccion_tecnologica")
]