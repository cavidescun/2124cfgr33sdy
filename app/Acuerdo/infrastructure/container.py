from dependency_injector import containers, providers
from app.Core.infrastructure.repositories import RegistroCalificadoRepositoryImpl
from app.Acuerdo.infrastructure.repositories import AcuerdoRepositoryImpl
from app.Acuerdo.application.use_cases.crear_acuerdo import CrearAcuerdo
from app.Acuerdo.application.use_cases.obtener_acuerdo import ObtenerAcuerdo

class AcuerdoContainer(containers.DeclarativeContainer):
    acuerdo_repo = providers.Factory(AcuerdoRepositoryImpl)
    registro_repo = providers.Factory(RegistroCalificadoRepositoryImpl)

    crear_acuerdo = providers.Factory(
        CrearAcuerdo,
        acuerdo_repo=acuerdo_repo,
        registro_repo=registro_repo
    )

    obtener_acuerdo = providers.Factory(
        ObtenerAcuerdo,
        acuerdo_repo=acuerdo_repo
    )
