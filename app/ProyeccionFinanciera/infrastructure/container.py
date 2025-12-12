from dependency_injector import containers, providers
from app.Core.infrastructure.repositories import RegistroCalificadoRepositoryImpl
from app.ProyeccionFinanciera.application.use_cases.crear_proyeccionFinanciera import CrearProyeccionFinanciera
from app.ProyeccionFinanciera.application.use_cases.obtener_proyeccionFinanciera import ObtenerProyeccionFinanciera
from app.ProyeccionFinanciera.infrastructure.repositories import ProyeccionFinancieraRepositoryImpl

class ProyeccionFinancieraContainer(containers.DeclarativeContainer):
    proyeccion_repo = providers.Factory(ProyeccionFinancieraRepositoryImpl)
    registro_repo = providers.Factory(RegistroCalificadoRepositoryImpl)

    crear_proyeccionFinanciera = providers.Factory(
        CrearProyeccionFinanciera,
        proyeccion_repo=proyeccion_repo,
        registro_repo=registro_repo
    )

    obtener_proyeccionFinanciera = providers.Factory(
        ObtenerProyeccionFinanciera,
        proyeccion_repo=proyeccion_repo
    )
