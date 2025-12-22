
from app.Acta.domain.repositories import ActaRepository
from app.Biblioteca.domain.entities import BibliotecaEntity
from app.Biblioteca.domain.repositories import BibliotecaRepository
from app.Core.domain.repositories.repositories import RegistroCalificadoRepository
from rest_framework.exceptions import NotFound

class CrearBiblioteca:
    def __init__(self, biblioteca_repo: BibliotecaRepository, registro_repo: RegistroCalificadoRepository,acta_repo: ActaRepository):
        self.biblioteca_repo = biblioteca_repo
        self.registro_repo = registro_repo
        self.acta_repo = acta_repo

    def ejecutar(self, **data) -> BibliotecaEntity:
        """
        Crea una entidad Acta a partir del formulario recibido.
        Si el usuario no envía una llave_maestra, se genera automáticamente
        y se crea un nuevo RegistroCalificado asociado.
        """
      
        creado_por = data.pop("creado_por", None)  
        llave_maestra = data.pop("llave_maestra", None)

        acta=self.acta_repo.find_by_llave(llave_maestra) 
        if not acta.aprobado:
            raise NotFound(f"no se ha aprobado la acta de la llave {llave_maestra}")
        self.biblioteca_repo.estatus_flag(llave_maestra)
        biblioteca = BibliotecaEntity(
            id=None,
            estatus=True,
            llave_maestra=llave_maestra,
            etiquetas_dinamicas=data,
            creado_por_id=creado_por.id if creado_por else None,  
            )
        return self.biblioteca_repo.save(biblioteca)