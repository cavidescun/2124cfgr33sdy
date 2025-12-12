from app.Acta.domain.repositories import ActaRepository
from app.Acuerdo.domain.repositories import AcuerdoRepository
from app.Biblioteca.domain.repositories import BibliotecaRepository
from app.Core.domain.repositories import RegistroCalificadoRepository
from app.ProyeccionFinanciera.domain.repositories import ProyeccionFinancieraRepository
from app.ProyeccionInfracTecnol.domain.repositories import ProyeccionInfracTecnolRepository


class UnificarInformacion:
    def __init__(self, acta_repo: ActaRepository, 
                 biblioteca_repo: BibliotecaRepository,
                 acuerdo_repo: AcuerdoRepository,
                 proyeccion_fi_repo: ProyeccionFinancieraRepository,
                 proyeccion_te_repo:ProyeccionInfracTecnolRepository,
                 registro_repo: RegistroCalificadoRepository):
                
                
                self.acta_repo = acta_repo
                self.biblioteca_repo = biblioteca_repo
                self.acuerdo_repo = acuerdo_repo
                self.proyeccion_fi_repo = proyeccion_fi_repo
                self.proyeccion_te_repo = proyeccion_te_repo
                self.registro_repo = registro_repo

    def ejecutar(self, llave) -> dict:
        fuentes = [
            self.acta_repo.find_by_llave(llave),
            self.biblioteca_repo.find_by_llave(llave),
            self.acuerdo_repo.find_by_llave(llave),
            self.proyeccion_fi_repo.find_by_llave(llave),
            self.proyeccion_te_repo.find_by_llave(llave)
        ]
        variables_unificadas = {}
        for fuente in fuentes:
            if not fuente:
                continue
            etiquetas = getattr(fuente, "etiquetas_dinamicas", None)
            if not etiquetas or not isinstance(etiquetas, dict):
                continue
            variables = (
                etiquetas
                .get("etiquetas_dinamicas", {})
                .get("variables", {})
            )
            if isinstance(variables, dict):
                variables_unificadas.update(variables)
        data={"etiquetas_dinamicas": {
                "variables": variables_unificadas
            }}
        self.registro_repo.update_by_llave(llave,data)
        return data