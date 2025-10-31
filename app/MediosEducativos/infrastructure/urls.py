from django.urls import path

from .views import MediosEducativosView

urlpatterns = [
    path("", MediosEducativosView.as_view(), name="crear_medio_educativo"),
]
