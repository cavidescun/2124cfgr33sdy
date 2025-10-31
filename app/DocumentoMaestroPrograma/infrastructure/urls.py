from django.urls import path

from .views import DocumentoPorLlaveView

urlpatterns = [
    path(
        "",
        DocumentoPorLlaveView.as_view(),
        name="presentacion_documento",
    ),
]
