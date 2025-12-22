from app.Acta.domain.repositories import ActaRepository
from app.Acuerdo.domain.repositories import AcuerdoRepository
from app.Biblioteca.domain.repositories import BibliotecaRepository
from app.ProyeccionFinanciera.domain.repositories import ProyeccionFinancieraRepository
from app.ProyeccionInfracTecnol.domain.repositories import ProyeccionInfracTecnolRepository
from app.ProyeccionTecnologica.domain.repositories import ProyeccionTecnologicaRepository

class PuntoDeControl:
    def __init__(self, acta_repo: ActaRepository, 
                 biblioteca_repo: BibliotecaRepository,
                 acuerdo_repo: AcuerdoRepository,
                 proyeccion_fi_repo: ProyeccionFinancieraRepository,
                 proyeccion_te_repo:ProyeccionInfracTecnolRepository,
                 tecnologico_repo:ProyeccionTecnologicaRepository,
                ):
                
                
                self.acta_repo = acta_repo
                self.biblioteca_repo = biblioteca_repo
                self.acuerdo_repo = acuerdo_repo
                self.proyeccion_fi_repo = proyeccion_fi_repo
                self.proyeccion_te_repo = proyeccion_te_repo
                self.tecnologico_repo = tecnologico_repo


    def ejecutar(self, llave_id) -> dict:
        
        acta = self.acta_repo.estatus(llave_id)
        biblioteca = self.biblioteca_repo.estatus(llave_id)
        acuerdo = self.acuerdo_repo.estatus(llave_id)
        proyeccion_fi = self.proyeccion_fi_repo.estatus(llave_id)
        proyeccion_te = self.proyeccion_te_repo.estatus(llave_id)
        proyeccion_tecnologica=self.tecnologico_repo.estatus(llave_id)

        return {
            "acta": acta.estatus if acta else None,
            "biblioteca": biblioteca.estatus if biblioteca else None,
            "acuerdo": acuerdo.estatus if acuerdo else None,
            "proyeccion_financiera": proyeccion_fi.estatus if proyeccion_fi else None,
            "proyeccion_infra_tecnologica": proyeccion_te.estatus if proyeccion_te else None,
            "proyeccion_tecnologica":proyeccion_tecnologica.estatus if proyeccion_tecnologica else None,
        }