import uuid
from app.Biblioteca.domain.entities import BibliotecaEntity
from app.Biblioteca.domain.repositories import BibliotecaRepository
from app.Biblioteca.application.mappers import FormularioRecursosMapper
from app.Core.domain.entities import RegistroCalificadoEntity
from app.Core.domain.repositories import RegistroCalificadoRepository


class CrearBiblioteca:
    def __init__(self, biblioteca_repo: BibliotecaRepository, registro_repo: RegistroCalificadoRepository):
        self.biblioteca_repo = biblioteca_repo
        self.registro_repo = registro_repo

    def ejecutar(self, **data) -> BibliotecaEntity:
        """
        Crea una entidad Acta a partir del formulario recibido.
        Si el usuario no envía una llave_maestra, se genera automáticamente
        y se crea un nuevo RegistroCalificado asociado.
        """
        llave_maestra = f"LLAVE-{uuid.uuid4().hex[:8].upper()}"
        registro = RegistroCalificadoEntity(
                id=None,
                llave_documento=llave_maestra,
                tipo=data.get("tipo", "Posgrado"),
                snies=data.get("snies", None),
            )
        self.registro_repo.save(registro)
        etiquetas = FormularioRecursosMapper.to_etiquetas(data)
        biblioteca = BibliotecaEntity(
                id=None,
                llave_maestra=llave_maestra,
                etiquetas_dinamicas=etiquetas,
            )
        return self.biblioteca_repo.save(biblioteca)