from dependency_injector import containers, providers
from app.Acta.infrastructure.repositories import ActaRepositoryImpl
from app.Core.infrastructure.repositories.repositories import RegistroCalificadoRepositoryImpl
from app.ProyeccionFinanciera.application.use_cases.actualizar_proyeccion_financiera import ActualizarProyeccionFinanciera
from app.ProyeccionFinanciera.application.use_cases.crear_proyeccionFinanciera import CrearProyeccionFinanciera
from app.ProyeccionFinanciera.application.use_cases.obtener_proyeccionFinanciera import ObtenerProyeccionFinanciera
from app.ProyeccionFinanciera.infrastructure.repositories import ProyeccionFinancieraRepositoryImpl

class ProyeccionFinancieraContainer(containers.DeclarativeContainer):
    proyeccion_repo = providers.Factory(ProyeccionFinancieraRepositoryImpl)
    registro_repo = providers.Factory(RegistroCalificadoRepositoryImpl)
    acta_repo = providers.Factory(ActaRepositoryImpl)

    crear_proyeccionFinanciera = providers.Factory(
        CrearProyeccionFinanciera,
        proyeccion_repo=proyeccion_repo,
        registro_repo=registro_repo,
        acta_repo=acta_repo
    )

    obtener_proyeccionFinanciera = providers.Factory(
        ObtenerProyeccionFinanciera,
        proyeccion_repo=proyeccion_repo
    )

    
    actualizar_proyeccion_financiera = providers.Factory(
        ActualizarProyeccionFinanciera,
        proyeccion_repo=proyeccion_repo
    )
