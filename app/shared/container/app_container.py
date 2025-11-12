from dependency_injector import containers, providers
from app.Acta.infrastructure.container import ActaContainer
from app.Biblioteca.infrastructure.container import BibliotecaContainer
from app.Core.infrastructure.container import CoreContainer
from app.IAEtiquetas.infrastructure.container import AIAnalyzerContainer
class ApplicationContainer(containers.DeclarativeContainer):
    """Contenedor global de la aplicación."""

    acta = providers.Container(ActaContainer)
    biblioteca = providers.Container(BibliotecaContainer)
    core = providers.Container(CoreContainer)
    ai_analyzer = providers.Container(AIAnalyzerContainer) 
