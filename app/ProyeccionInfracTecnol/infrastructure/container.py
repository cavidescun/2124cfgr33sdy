from dependency_injector import containers, providers
from app.Acta.infrastructure.repositories import ActaRepositoryImpl
from app.Core.infrastructure.repositories.repositories import RegistroCalificadoRepositoryImpl
from app.ProyeccionInfracTecnol.application.use_cases.actualizar_proyeccion_infrac_tecnol import ActualizarProyeccionInfracTecnol
from app.ProyeccionInfracTecnol.infrastructure.repositories import ProyeccionInfracTecnolRepositoryImpl
from app.ProyeccionInfracTecnol.application.use_cases.crear_proyeccionInfracTecnol import CrearProyeccionInfracTecnol
from app.ProyeccionInfracTecnol.application.use_cases.obtener_proyeccionInfracTecnol import ObtenerProyeccionInfracTecnol

class ProyeccionInfracTecnolContainer(containers.DeclarativeContainer):
    proyeccion_repo = providers.Factory(ProyeccionInfracTecnolRepositoryImpl)
    registro_repo = providers.Factory(RegistroCalificadoRepositoryImpl)
    acta_repo = providers.Factory(ActaRepositoryImpl)

    crear_proyeccion_infrac_tecnol = providers.Factory(
        CrearProyeccionInfracTecnol,
        proyeccion_repo=proyeccion_repo,
        registro_repo=registro_repo,
        acta_repo=acta_repo
    )

    obtener_proyeccion_infrac_tecnol = providers.Factory(
        ObtenerProyeccionInfracTecnol,
        proyeccion_repo=proyeccion_repo
    )

    actualizar_proyeccion_infrac_tecnol = providers.Factory(
        ActualizarProyeccionInfracTecnol,
        proyeccion_repo=proyeccion_repo
    )
