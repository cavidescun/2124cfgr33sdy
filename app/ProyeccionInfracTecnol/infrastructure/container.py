from dependency_injector import containers, providers
from app.Core.infrastructure.repositories import RegistroCalificadoRepositoryImpl
from app.ProyeccionInfracTecnol.infrastructure.repositories import ProyeccionInfracTecnolRepositoryImpl
from app.ProyeccionInfracTecnol.application.use_cases.crear_proyeccionInfracTecnol import CrearProyeccionInfracTecnol
from app.ProyeccionInfracTecnol.application.use_cases.obtener_proyeccionInfracTecnol import ObtenerProyeccionInfracTecnol

class ProyeccionInfracTecnolContainer(containers.DeclarativeContainer):
    proyeccion_repo = providers.Factory(ProyeccionInfracTecnolRepositoryImpl)
    registro_repo = providers.Factory(RegistroCalificadoRepositoryImpl)

    crear_proyeccion_infrac_tecnol = providers.Factory(
        CrearProyeccionInfracTecnol,
        proyeccion_repo=proyeccion_repo,
        registro_repo=registro_repo
    )

    obtener_proyeccion_infrac_tecnol = providers.Factory(
        ObtenerProyeccionInfracTecnol,
        proyeccion_repo=proyeccion_repo
    )
