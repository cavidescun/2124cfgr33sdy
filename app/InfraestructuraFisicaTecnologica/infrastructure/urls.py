from django.urls import path

from .views import InfraestructuraFisicaTecnologicaView

urlpatterns = [
    path(
        "",
        InfraestructuraFisicaTecnologicaView.as_view(),
        name="infraestructura_fisica_tecnologica",
    ),
]
