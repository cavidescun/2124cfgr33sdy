import os
import json
import httpx
from typing import Dict, Any, Optional
from app.IAEtiquetas.domain.services import IAService

class OpenAIService(IAService):
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("La clave de API de OpenAI no está configurada en las variables de entorno.")

        from openai import OpenAI

        self.client = OpenAI(api_key=api_key)
       
    def analizar(self, prompt: str, datos: Dict[str, Any]) -> str:
        try:
            prompt_formateado = self._formatear_prompt(prompt, datos)
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "system",
                        "content": "Eres un asistente experto en analisis de datos"
                    },
                    {
                        "role": "user",
                        "content": prompt_formateado
                    }
                ],
                temperature=0.7,
                max_tokens=2000
            )

            return response.choices[0].message.content
        except Exception as e:
            import traceback
            error_detail = traceback.format_exc()
            raise RuntimeError(f"Error al analizar los datos con OpenAI: {str(e)}\nDetalles: {error_detail}")

    def _formatear_prompt(self, prompt: str, datos: Dict[str, Any]) -> str:
        datos_str = json.dumps(datos, indent=2, ensure_ascii=False)
        prompt_formateado = prompt.replace("{datos}", datos_str)

        for key, value in datos.items():
            placeholder = f"{{{key}}}"
            if placeholder in prompt_formateado:
                prompt_formateado = prompt_formateado.replace(placeholder, str(value))
        
        return prompt_formateado