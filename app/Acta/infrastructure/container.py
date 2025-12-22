from dependency_injector import containers, providers
from app.Acta.application.use_cases.actualizar_acta import ActualizarActa
from app.Acta.application.use_cases.aprobar_acta import AprobarActa
from app.Acta.infrastructure.repositories import ActaRepositoryImpl
from app.Core.infrastructure.repositories.repositories import RegistroCalificadoRepositoryImpl
from app.Acta.application.use_cases.crear_acta import CrearActa
from app.Acta.application.use_cases.obtener_acta import ObtenerActa

from app.shared.email.email_service_impl import MailServiceImpl
from app.shared.email.email_template_renderer import EmailTemplateRenderer


class ActaContainer(containers.DeclarativeContainer):
    """Contenedor de dependencias del módulo Acta."""

    acta_repo = providers.Factory(ActaRepositoryImpl)
    registro_repo = providers.Factory(RegistroCalificadoRepositoryImpl)
    email_service=providers.Factory(MailServiceImpl)
    template_renderer = providers.Singleton(EmailTemplateRenderer)
    
    crear_acta = providers.Factory(
        CrearActa,
        acta_repo=acta_repo,
        registro_repo=registro_repo,
        email_service=email_service,
        template_renderer=template_renderer,
    )

    obtener_acta = providers.Factory(
        ObtenerActa,
        acta_repo=acta_repo
    )

    actualizar_acta = providers.Factory(
        ActualizarActa,
        acta_repo=acta_repo
    )

    aprobar_acta= providers.Factory(
        AprobarActa,
        acta_repo=acta_repo
    )
