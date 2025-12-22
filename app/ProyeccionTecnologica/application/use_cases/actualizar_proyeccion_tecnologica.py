
from app.ProyeccionTecnologica.domain.repositories import ProyeccionTecnologicaRepository

class ActualizarProyeccionTecnologica:
    def __init__(self, proyeccion_repo: ProyeccionTecnologicaRepository):
        self.proyeccion_repo = proyeccion_repo
   

    def ejecutar(self, llave_id: str, etiquetas_dinamicas: dict,user):
        proyeccion_tecnologica = self.proyeccion_repo.find_by_llave_update(llave_id)
        actuales = proyeccion_tecnologica.etiquetas_dinamicas
        if "variables" in actuales:
            actuales_vars = actuales["variables"]
        else:
            actuales_vars = actuales.get("etiquetas_dinamicas", {}).get("variables", {})

        nuevas = etiquetas_dinamicas.get("variables", {})
        actuales_vars.update(nuevas)

        proyeccion_tecnologica.etiquetas_dinamicas = {"variables": actuales_vars}
        proyeccion_tecnologica.modificado_por=user
        return self.proyeccion_repo.update(proyeccion_tecnologica)