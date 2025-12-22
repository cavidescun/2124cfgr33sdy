from dependency_injector import containers, providers

from app.Acta.infrastructure.repositories import ActaRepositoryImpl
from app.Acuerdo.infrastructure.repositories import AcuerdoRepositoryImpl
from app.Biblioteca.infrastructure.repositories import BibliotecaRepositoryImpl
from app.Core.application.use_cases.crear_documento import CrearDocumento
from app.Core.application.use_cases.descargar_informe import DescargarInforme
from app.Core.application.use_cases.obtener_llaves import ObtenerLlave
from app.Core.application.use_cases.crear_llaves import  CrearLlave

from app.Core.application.use_cases.punto_de_control import PuntoDeControl
from app.Core.application.use_cases.unificar_informacion import UnificarInformacion
from app.Core.infrastructure.repositories.repositories import RegistroCalificadoRepositoryImpl
from app.Core.infrastructure.repositories.repositories_user import UserRepositoryImpl
from app.ProyeccionFinanciera.infrastructure.repositories import ProyeccionFinancieraRepositoryImpl
from app.ProyeccionInfracTecnol.infrastructure.repositories import ProyeccionInfracTecnolRepositoryImpl
from app.ProyeccionTecnologica.infrastructure.repositories import ProyeccionTecnologicaRepositoryImpl
from app.shared.logic.contextoreporte import ContextoReporte
from app.shared.email.email_service_impl import MailServiceImpl
from app.shared.email.email_template_renderer import EmailTemplateRenderer



class CoreContainer(containers.DeclarativeContainer):
    """Contenedor de dependencias del módulo Acta."""

    registro_repo = providers.Factory(RegistroCalificadoRepositoryImpl)
    acta_repo = providers.Factory(ActaRepositoryImpl)
    biblioteca_repo = providers.Factory(BibliotecaRepositoryImpl)
    acuerdo_repo = providers.Factory(AcuerdoRepositoryImpl)
    proyeccion_fi_repo = providers.Factory(ProyeccionFinancieraRepositoryImpl)
    proyeccion_te_repo = providers.Factory(ProyeccionInfracTecnolRepositoryImpl)
    tecnologico_repo = providers.Factory(ProyeccionTecnologicaRepositoryImpl)
    email_service=providers.Factory(MailServiceImpl)
    template_renderer = providers.Singleton(EmailTemplateRenderer)
    repo_user = providers.Singleton(UserRepositoryImpl)


    obtener_llave = providers.Factory(
        ObtenerLlave,
        registro_calificado_repo=registro_repo
    )

    crear_llave = providers.Factory(
        CrearLlave,
        registro_calificado_repo=registro_repo
    )

    unificar_informacion = providers.Factory(
        UnificarInformacion,
        acta_repo=acta_repo,
        biblioteca_repo=biblioteca_repo,
        acuerdo_repo=acuerdo_repo,
        proyeccion_fi_repo=proyeccion_fi_repo,
        proyeccion_te_repo=proyeccion_te_repo,
        tecnologico_repo=tecnologico_repo,
        registro_repo=registro_repo,
        email_service=email_service,
        template_renderer=template_renderer,
        repo_user=repo_user
    )


    crear_documento = providers.Factory(
        CrearDocumento,
        registro_repo=registro_repo,
        crear_documento=ContextoReporte  
    )

    descargar_informe = providers.Factory(
        DescargarInforme,
        registro_calificado_repo=registro_repo
    )


    punto_de_control = providers.Factory(
        PuntoDeControl,
        acta_repo=acta_repo,
        biblioteca_repo=biblioteca_repo,
        acuerdo_repo=acuerdo_repo,
        proyeccion_fi_repo=proyeccion_fi_repo,
        proyeccion_te_repo=proyeccion_te_repo,
        tecnologico_repo=tecnologico_repo
    )

