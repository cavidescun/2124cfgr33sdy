from django.urls import path

from .views import EmailTokenView,UnificacionInformacionView,GenerarInformeView,DescargarInformeView

urlpatterns = [

   path("unificar-informacion",UnificacionInformacionView.as_view(),name="unifica informacion"),
   path('token/email/', EmailTokenView.as_view(), name='token_by_email'),
   path('generar-informe', GenerarInformeView.as_view(), name='token_by_email'),
   path('descargar-informe', DescargarInformeView.as_view(), name='descargar-informe'),

]
