from django.urls import path

from .views import AcuerdoView

urlpatterns = [
    path("",AcuerdoView.as_view(), name="acuerdo")
]