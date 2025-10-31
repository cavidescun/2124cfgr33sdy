from django.urls import path

from .views import GenerarLLaveMaestraView, DescargarCarpetaView

urlpatterns = [
    path(
        "GenerarLLaveMaestraView/",
        GenerarLLaveMaestraView.as_view(),
        name="Generar LLave Maestra",
    ),
 path("descargar/<str:llave>/", DescargarCarpetaView.as_view(), name="descargar_carpeta"),
]
