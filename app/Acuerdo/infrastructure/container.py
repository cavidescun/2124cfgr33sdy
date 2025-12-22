from dependency_injector import containers, providers
from app.Acta.infrastructure.repositories import ActaRepositoryImpl
from app.Acuerdo.application.use_cases.actualizar_acuerdo import ActualizarAcuerdo
from app.Core.infrastructure.repositories.repositories import RegistroCalificadoRepositoryImpl
from app.Acuerdo.infrastructure.repositories import AcuerdoRepositoryImpl
from app.Acuerdo.application.use_cases.crear_acuerdo import CrearAcuerdo
from app.Acuerdo.application.use_cases.obtener_acuerdo import ObtenerAcuerdo

class AcuerdoContainer(containers.DeclarativeContainer):
    acuerdo_repo = providers.Factory(AcuerdoRepositoryImpl)
    acta_repo = providers.Factory(ActaRepositoryImpl)
    registro_repo = providers.Factory(RegistroCalificadoRepositoryImpl)

    crear_acuerdo = providers.Factory(
        CrearAcuerdo,
        acuerdo_repo=acuerdo_repo,
        registro_repo=registro_repo,
        acta_repo=acta_repo
    )

    obtener_acuerdo = providers.Factory(
        ObtenerAcuerdo,
        acuerdo_repo=acuerdo_repo
    )

    actualizar_acuerdo = providers.Factory(
        ActualizarAcuerdo,
        acuerdo_repo=acuerdo_repo
    )

