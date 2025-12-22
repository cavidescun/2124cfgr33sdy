from app.ProyeccionInfracTecnol.domain.entities import ProyeccionInfracTecnolEntity
from app.ProyeccionInfracTecnol.domain.repositories import ProyeccionInfracTecnolRepository

class ActualizarProyeccionInfracTecnol:
    def __init__(self, proyeccion_repo: ProyeccionInfracTecnolRepository):
        self.proyeccion_repo = proyeccion_repo

    def ejecutar(self, llave_id: str, etiquetas_dinamicas: dict,user):
        proyeccion_financiera = self.proyeccion_repo.find_by_llave_update(llave_id)
        actuales = proyeccion_financiera.etiquetas_dinamicas
        if "variables" in actuales:
            actuales_vars = actuales["variables"]
        else:
            actuales_vars = actuales.get("etiquetas_dinamicas", {}).get("variables", {})
        nuevas = etiquetas_dinamicas.get("variables", {})
        actuales_vars.update(nuevas)
        proyeccion_financiera.etiquetas_dinamicas = {"variables": actuales_vars}
        proyeccion_financiera.modificado_por=user
        return self.proyeccion_repo.update(proyeccion_financiera)