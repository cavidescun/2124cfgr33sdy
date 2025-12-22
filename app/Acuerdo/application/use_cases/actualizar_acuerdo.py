
from app.Acuerdo.domain.repositories import AcuerdoRepository

class ActualizarAcuerdo:
    def __init__(self, acuerdo_repo: AcuerdoRepository):
        self.acuerdo_repo = acuerdo_repo
   

    def ejecutar(self, llave_id: str, etiquetas_dinamicas: dict,user):
        proyeccion_tecnologica = self.acuerdo_repo.find_by_llave_update(llave_id)
        actuales = proyeccion_tecnologica.etiquetas_dinamicas
        if "variables" in actuales:
            actuales_vars = actuales["variables"]
        else:
            actuales_vars = actuales.get("etiquetas_dinamicas", {}).get("variables", {})

        nuevas = etiquetas_dinamicas.get("variables", {})
        actuales_vars.update(nuevas)

        proyeccion_tecnologica.etiquetas_dinamicas = {"variables": actuales_vars}
        proyeccion_tecnologica.modificado_por=user

        return self.acuerdo_repo.update(proyeccion_tecnologica)