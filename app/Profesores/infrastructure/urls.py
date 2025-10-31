from django.urls import path

from .views import ProferoresView

urlpatterns = [
    path("", ProferoresView.as_view(), name="crear_profesores"),
]
