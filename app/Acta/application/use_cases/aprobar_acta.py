
from app.Acta.domain.repositories import ActaRepository

class AprobarActa:
    def __init__(self, acta_repo: ActaRepository):
        self.acta_repo = acta_repo

    def ejecutar(self, llave_id: str, aprobado: bool, usuario):
        self.acta_repo.find_by_llave_approved(llave_id)

        self.acta_repo.aprobar_acta(
            llave_id=llave_id,
            aprobado=aprobado,
            usuario=usuario
        )

        return "ok"