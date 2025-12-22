from zoneinfo import ZoneInfo

from app.Acta.domain.repositories import ActaRepository
from app.Acuerdo.domain.repositories import AcuerdoRepository
from app.Biblioteca.domain.repositories import BibliotecaRepository
from app.Core.domain.repositories.repositories import RegistroCalificadoRepository
from app.Core.domain.repositories.repositories_user import UserRepository
from app.ProyeccionFinanciera.domain.repositories import ProyeccionFinancieraRepository
from app.ProyeccionInfracTecnol.domain.repositories import ProyeccionInfracTecnolRepository
from app.ProyeccionTecnologica.domain.repositories import ProyeccionTecnologicaRepository
from app.shared.email.email_service import EmailService
from app.shared.email.email_template_renderer import EmailTemplateRenderer


class UnificarInformacion:
    def __init__(
        self,
        acta_repo: ActaRepository,
        biblioteca_repo: BibliotecaRepository,
        acuerdo_repo: AcuerdoRepository,
        proyeccion_fi_repo: ProyeccionFinancieraRepository,
        proyeccion_te_repo: ProyeccionInfracTecnolRepository,
        registro_repo: RegistroCalificadoRepository,
        tecnologico_repo: ProyeccionTecnologicaRepository,
        email_service: EmailService,
        template_renderer: EmailTemplateRenderer,
        repo_user: UserRepository,
    ):
        self.acta_repo = acta_repo
        self.biblioteca_repo = biblioteca_repo
        self.acuerdo_repo = acuerdo_repo
        self.proyeccion_fi_repo = proyeccion_fi_repo
        self.proyeccion_te_repo = proyeccion_te_repo
        self.tecnologico_repo = tecnologico_repo
        self.registro_repo = registro_repo
        self.email_service = email_service
        self.template_renderer = template_renderer
        self.repo_user = repo_user

    def ejecutar(self, llave) -> dict:
        fuentes = [
            self.acta_repo.find_by_llave(llave),
            self.biblioteca_repo.find_by_llave(llave),
            self.acuerdo_repo.find_by_llave(llave),
            self.proyeccion_fi_repo.find_by_llave(llave),
            self.proyeccion_te_repo.find_by_llave(llave),
            self.tecnologico_repo.find_by_llave(llave),
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

        data = {
            "etiquetas_dinamicas": {
                "variables": variables_unificadas
            }
        }

        # 🔹 Actualiza registro calificado
        registro_calificado_entity = self.registro_repo.update_by_llave(
            llave,
            data
        )

        # 🔹 Conversión y formateo de fecha (Bogotá, Colombia)
        fecha_utc = registro_calificado_entity.actualizado_en
        fecha_bogota = fecha_utc.astimezone(ZoneInfo("America/Bogota"))

        meses = [
            "enero", "febrero", "marzo", "abril", "mayo", "junio",
            "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
        ]

        fecha_formateada = (
            f"{fecha_bogota.day} de "
            f"{meses[fecha_bogota.month - 1]} de "
            f"{fecha_bogota.year} a las "
            f"{fecha_bogota:%H:%M}"
        )

        # 🔹 Envío de correo
        emails = self.repo_user.get_all_emails()

        html_body = self.template_renderer.render(
            "unificacion.html",
            llave_maestra=llave,
            fecha_unificacion=fecha_formateada
        )

        self.email_service.send_email(
            to=emails,
            subject="📄 Unificación | CUN",
            html_body=html_body,
        )

        return data
