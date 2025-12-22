
from app.Biblioteca.domain.repositories import BibliotecaRepository


class ActualizarBiblioteca:
    def __init__(self, biblioteca_repo: BibliotecaRepository):
        self.biblioteca_repo = biblioteca_repo

    def ejecutar(self, llave_id: str, etiquetas_dinamicas: dict,user):
        proyeccion_tecnologica = self.biblioteca_repo.find_by_llave_update(llave_id)
        actuales = proyeccion_tecnologica.etiquetas_dinamicas
        if "variables" in actuales:
            actuales_vars = actuales["variables"]
        else:
            actuales_vars = actuales.get("etiquetas_dinamicas", {}).get("variables", {})
        nuevas = etiquetas_dinamicas.get("variables", {})
        actuales_vars.update(nuevas)
        proyeccion_tecnologica.etiquetas_dinamicas = {"variables": actuales_vars}
        proyeccion_tecnologica.modificado_por=user
        return self.biblioteca_repo.update(proyeccion_tecnologica)
    