from django.urls import path

from .views import PresentacionDocumentoView

urlpatterns = [
    path(
        "",
        PresentacionDocumentoView.as_view(),
        name="presentacion_documento",
    ),
]
