import uuid
import os
from app.Acta.domain.entities import ActaEntity
from app.Acta.domain.repositories import ActaRepository
from app.Core.domain.entities import RegistroCalificadoEntity
from app.Core.domain.repositories.repositories import RegistroCalificadoRepository
from app.shared.email.email_service import EmailService
from app.shared.email.email_template_renderer import EmailTemplateRenderer


FRONTEND_BASE_URL = os.getenv("FRONTEND_BASE_URL", "http://localhost:4200")


class CrearActa:
    def __init__(
        self,
        acta_repo: ActaRepository,
        registro_repo: RegistroCalificadoRepository,
        email_service: EmailService,
        template_renderer: EmailTemplateRenderer,
    ):
        self.acta_repo = acta_repo
        self.registro_repo = registro_repo
        self.email_service = email_service
        self.template_renderer = template_renderer

    def ejecutar(self, **data) -> ActaEntity:
        creado_por = data.pop("creado_por", None)
        llave_maestra = self._generar_llave_maestra()
        numero_acta = self._generar_numero_acta()
        self._crear_registro_calificado(
            llave_maestra=llave_maestra,
            numero_acta=numero_acta,
            data=data,
        )
        acta = self._crear_acta(
            llave_maestra=llave_maestra,
            creado_por=creado_por,
            data=data,
        )

        self._enviar_correo(acta, creado_por, llave_maestra, numero_acta, data)
        return acta

    def _generar_llave_maestra(self) -> str:
        return f"LLAVE-{uuid.uuid4().hex[:8].upper()}"

    def _generar_numero_acta(self) -> str:
        return uuid.uuid4().hex[:8].upper()

    def _crear_registro_calificado(self, llave_maestra, numero_acta, data):
        registro = RegistroCalificadoEntity(
            id=None,
            llave_documento=llave_maestra,
            numero_acta=numero_acta,
            tipo=data.get("tipo", "Posgrado"),
            snies=data.get("snies"),
        )
        self.registro_repo.save(registro)

    def _crear_acta(self, llave_maestra, creado_por, data) -> ActaEntity:
        acta = ActaEntity(
            id=None,
            estatus=True,
            llave_maestra=llave_maestra,
            etiquetas_dinamicas=data.get("etiquetas_dinamicas", {}),
            creado_por_id=creado_por.id if creado_por else None,
        )
        return self.acta_repo.save(acta)

    def _construir_url_aprobacion(self, llave_maestra: str) -> str:
        return f"{FRONTEND_BASE_URL}/#/aprobacion-acta/{llave_maestra}"

    def _enviar_correo(self, acta, creado_por, llave_maestra, numero_acta, data):
        if not creado_por or not creado_por.email:
            return

        variables = (
            data
            .get("etiquetas_dinamicas", {})
            .get("variables", {})
        )

        correo_director = variables.get("correo_director")
        url_aprobacion = self._construir_url_aprobacion(llave_maestra)

        html_body = self.template_renderer.render(
            "acta_creada.html",
            nombre_usuario=creado_por,
            llave_maestra=llave_maestra,
            numero_acta=numero_acta,
            variables=variables,
            url_aprobacion=url_aprobacion,
        )

        self.email_service.send_email(
            to=correo_director,
            subject="📄 Acta creada exitosamente | CUN",
            html_body=html_body,
        )
