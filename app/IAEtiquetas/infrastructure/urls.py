from django.urls import path
from .views import (
    AnalizarIAView,
    PromptTemplatesView,
    PromptTemplateDetailView,
    PromptTemplatesBatchView
)

urlpatterns = [
    path("analizar/", AnalizarIAView.as_view(), name="analizar_ia"),
    path("templates/", PromptTemplatesView.as_view(), name="templates_list_create"),
    path("templates/batch/", PromptTemplatesBatchView.as_view(), name="templates_batch_create"),
    path("templates/<str:nombre_etiqueta>/", PromptTemplateDetailView.as_view(), name="template_detail"),
]