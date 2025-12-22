from dependency_injector import containers, providers
from app.Acta.infrastructure.repositories import ActaRepositoryImpl
from app.Biblioteca.application.use_cases.actualizar_biblioteca import ActualizarBiblioteca
from app.Biblioteca.infrastructure.repositories import BibliotecaRepositoryImpl
from app.Core.infrastructure.repositories.repositories import RegistroCalificadoRepositoryImpl
from app.Biblioteca.application.use_cases.crear_biblioteca import CrearBiblioteca
from app.Biblioteca.application.use_cases.obtener_biblioteca import ObtenerBiblioteca


class BibliotecaContainer(containers.DeclarativeContainer):
    """Contenedor de dependencias del módulo biblioteca."""

    biblioteca_repo = providers.Factory(BibliotecaRepositoryImpl)
    registro_repo = providers.Factory(RegistroCalificadoRepositoryImpl)
    acta_repo = providers.Factory(ActaRepositoryImpl)

    crear_biblioteca = providers.Factory(
        CrearBiblioteca,
        biblioteca_repo=biblioteca_repo,
        registro_repo=registro_repo,
        acta_repo=acta_repo
    )

    obtener_biblioteca = providers.Factory(
        ObtenerBiblioteca,
        biblioteca_repo=biblioteca_repo
    )

    actualizar_biblioteca= providers.Factory(
        ActualizarBiblioteca,
        biblioteca_repo=biblioteca_repo
    )
