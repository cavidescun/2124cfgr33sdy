from app.Biblioteca.domain.repositories import BibliotecaRepository
from app.Biblioteca.application.mappers import FormularioRecursosMapper

class ObtenerBiblioteca:
    def __init__(self, biblioteca_repo: BibliotecaRepository):
        self.biblioteca_repo = biblioteca_repo

    def ejecutar(self, acta_id: int) -> dict:
        acta = self.biblioteca_repo.find_by_id(acta_id)
        return FormularioRecursosMapper.from_etiquetas(acta.etiquetas_dinamicas)
