from django.urls import path

from .views import JustificacionProgramaView

urlpatterns = [
    path("", JustificacionProgramaView.as_view(), name="crear_justificacion_programa"),
]
