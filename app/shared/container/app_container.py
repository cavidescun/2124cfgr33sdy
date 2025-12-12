from dependency_injector import containers, providers
from app.Acta.infrastructure.container import ActaContainer
from app.Biblioteca.infrastructure.container import BibliotecaContainer
from app.Core.infrastructure.container import CoreContainer
from app.IAEtiquetas.infrastructure.container import AIAnalyzerContainer
from app.Acuerdo.infrastructure.container import AcuerdoContainer
from app.ProyeccionFinanciera.infrastructure.container import ProyeccionFinancieraContainer
from app.ProyeccionInfracTecnol.infrastructure.container import ProyeccionInfracTecnolContainer
class ApplicationContainer(containers.DeclarativeContainer):
    """Contenedor global de la aplicación."""

    acta = providers.Container(ActaContainer)
    biblioteca = providers.Container(BibliotecaContainer)
    core = providers.Container(CoreContainer)
    ai_analyzer = providers.Container(AIAnalyzerContainer)
    acuerdo = providers.Container(AcuerdoContainer)
    proyeccion_financiera = providers.Container(ProyeccionFinancieraContainer)
    proyeccion_infrac_tecnol = providers.Container(ProyeccionInfracTecnolContainer)
    
