from django.urls import path

from .views import SectorExternoView

urlpatterns = [
    path("", SectorExternoView.as_view(), name="crear_sector_externo"),
]
