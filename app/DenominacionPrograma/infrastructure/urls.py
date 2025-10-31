from django.urls import path

from .views import DenominacionProgramaView

urlpatterns = [
    path("", DenominacionProgramaView.as_view(), name="crear_denominacion_programa"),
]
