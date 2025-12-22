import json
import os
import requests
import logging
from app.shared.email.email_service import EmailService

logger = logging.getLogger(__name__)

class MailServiceImpl(EmailService):
    def send_email(self, to: str | list[str], subject: str, html_body: str) -> None:
        email_enabled = os.getenv("EMAIL_ENABLED", "true").lower() == "true"
        
        if not email_enabled:
            recipients = [to] if isinstance(to, str) else to
            logger.info(f"📧 [SIMULACIÓN] Email NO enviado (EMAIL_ENABLED=false)")
            logger.info(f"   Para: {', '.join(recipients)}")
            logger.info(f"   Asunto: {subject}")
            logger.debug(f"   Cuerpo HTML: {html_body[:100]}...")
            return
        
        recipients = [to] if isinstance(to, str) else to
        
        payload = {
            "from": {
                "address": os.getenv("ZEPTOMAIL_ADDRESS"),
                "name": os.getenv("ZEPTOMAIL_NAME"),
            },
            "to": [
                {"email_address": {"address": email}} for email in recipients
            ],
            "subject": subject,
            "htmlbody": html_body
        }
        
        headers = {
            "Authorization": f"Zoho-enczapikey {os.getenv('ZEPTOMAIL_KEY')}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(
                os.getenv("ZEPTOMAIL_URL"),
                headers=headers,
                data=json.dumps(payload),
                timeout=10
            )
            
            logger.info(f"ZeptoMail response status: {response.status_code}")
            logger.debug(f"ZeptoMail response body: {response.text}")
            response.raise_for_status()
            
        except requests.exceptions.HTTPError as e:
            logger.error(f"Error enviando email: {e}")
            logger.error(f"Response body: {response.text}")
            
            if response.status_code == 403:
                error_msg = "Error de autenticación con ZeptoMail. Verifica tu API key y que el dominio esté verificado."
            else:
                error_msg = f"Error al enviar email: {response.status_code}"
            
            raise Exception(error_msg) from e