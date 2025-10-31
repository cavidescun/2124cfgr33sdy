from django.urls import path

from .views import InvestigacionesInnovacionView

urlpatterns = [
    path("",InvestigacionesInnovacionView.as_view(), name="crear_investigaciones_innovacion"),
]
