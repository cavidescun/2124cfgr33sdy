from django.urls import path

from .views import AspectosCurricularesView

urlpatterns = [
    path("", AspectosCurricularesView.as_view(), name="crear_aspecto_curricular"),
]
