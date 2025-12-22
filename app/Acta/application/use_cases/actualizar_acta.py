
from app.Acta.domain.repositories import ActaRepository

class ActualizarActa:
    def __init__(self, acta_repo: ActaRepository):
        self.acta_repo = acta_repo
   

    def ejecutar(self, llave_id: str, etiquetas_dinamicas: dict,user):
        acta = self.acta_repo.find_by_llave_update(llave_id)
        actuales = acta.etiquetas_dinamicas
        if "variables" in actuales:
            actuales_vars = actuales["variables"]
        else:
            actuales_vars = actuales.get("etiquetas_dinamicas", {}).get("variables", {})

        nuevas = etiquetas_dinamicas.get("variables", {})
        actuales_vars.update(nuevas)

        acta.etiquetas_dinamicas = {"variables": actuales_vars}
        acta.modificado_por=user
        return self.acta_repo.update(acta)