from dependency_injector import containers, providers
from .repositories import AnalisisIARepositoryImpl, PromptTemplateRepositoryImpl
from .services.openai_services import OpenAIService
from ..application.use_cases import AnalizarConIA


class AIAnalyzerContainer(containers.DeclarativeContainer):
    """Contenedor de dependencias del módulo AIAnalyzer"""
    
    ia_service = providers.Factory(OpenAIService)
    analisis_repo = providers.Factory(AnalisisIARepositoryImpl)
    template_repo = providers.Factory(PromptTemplateRepositoryImpl)
    
    analizar_con_ia = providers.Factory(
        AnalizarConIA,
        ia_service=ia_service,
        analisis_repo=analisis_repo,
        template_repo=template_repo
    )