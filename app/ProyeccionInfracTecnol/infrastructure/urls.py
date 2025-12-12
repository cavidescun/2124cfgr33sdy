from django.urls import path

from .views import ProyeccionInfracTecnolView

urlpatterns = [
    path("",ProyeccionInfracTecnolView.as_view(), name="proyeccion_infrac_tecnol")
]