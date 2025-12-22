from dependency_injector import containers, providers
from app.Acta.infrastructure.repositories import ActaRepositoryImpl
from app.Core.infrastructure.repositories.repositories import RegistroCalificadoRepositoryImpl
from app.ProyeccionTecnologica.application.use_cases.actualizar_proyeccion_tecnologica import ActualizarProyeccionTecnologica
from app.ProyeccionTecnologica.infrastructure.repositories import ProyeccionTecnologicaRepositoryImpl
from app.ProyeccionTecnologica.application.use_cases.crear_proyeccion_tecnologica import CrearProyeccionTecnologica
from app.ProyeccionTecnologica.application.use_cases.obtener_proyeccion_tecnologica import ObtenerProyeccionTecnologica

class ProyeccionTecnologicaContainer(containers.DeclarativeContainer):
    proyeccion_repo = providers.Factory(ProyeccionTecnologicaRepositoryImpl)
    registro_repo = providers.Factory(RegistroCalificadoRepositoryImpl)
    acta_repo = providers.Factory(ActaRepositoryImpl)

    crear_proyeccion_tecnologica = providers.Factory(
        CrearProyeccionTecnologica,
        proyeccion_repo=proyeccion_repo,
        registro_repo=registro_repo,
        acta_repo=acta_repo
    )

    obtener_proyeccion_tecnologica = providers.Factory(
        ObtenerProyeccionTecnologica,
        proyeccion_repo=proyeccion_repo
    )

    actualizar_proyeccion_tecnologica=providers.Factory(
        ActualizarProyeccionTecnologica,
        proyeccion_repo=proyeccion_repo
    )
