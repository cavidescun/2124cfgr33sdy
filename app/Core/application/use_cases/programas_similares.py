from app.Core.domain.repositories.repositories_sines import SniesRepository

class ProgramasSimilares:
    def __init__(self, repo_snies: SniesRepository):
        self.repo_snies = repo_snies

    def ejecutar(self, filtros):
        return self.repo_snies.buscar_programas_similares(filtros)
