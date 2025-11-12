from typing import Dict, Any, Optional
from app.IAEtiquetas.domain.entities import AnalisisIaEntity, PromptPlantilla
from app.IAEtiquetas.domain.repositories import AnalisisIARepository, PromptPlantillaRepository
from app.IAEtiquetas.domain.services import IAService


class AnalizarConIA:    
    def __init__(
        self,
        ia_service: IAService,
        analisis_repo: AnalisisIARepository,
        template_repo: PromptPlantillaRepository
    ):
        self.ia_service = ia_service
        self.analisis_repo = analisis_repo
        self.template_repo = template_repo
    
    def ejecutar(
        self,
        nombre_etiqueta: str,
        datos: Dict[str, Any],
        prompt_custom: Optional[str] = None
    ) -> AnalisisIaEntity:
        if prompt_custom:
            prompt = prompt_custom
        else:
            template = self.template_repo.get_by_nombre_etiqueta(nombre_etiqueta)
            if not template:
                raise ValueError(
                    f"No se encontró un template para la etiqueta '{nombre_etiqueta}'. "
                    f"Proporciona un prompt_custom o crea el template en la base de datos."
                )
            prompt = template.prompt_template

        resultado = self.ia_service.analizar(prompt, datos)

        analisis = AnalisisIaEntity(
            id=None,
            nombre_etiqueta=nombre_etiqueta,
            prompt_usado=prompt,
            datos_entrada=datos,
            resultado=resultado
        )
        
        return self.analisis_repo.save(analisis)


class CrearTemplate:
    def __init__(self, template_repo: PromptPlantillaRepository):
        self.template_repo = template_repo
    
    def ejecutar(
        self,
        nombre_etiqueta: str,
        prompt_template: str,
        descripcion: Optional[str] = None
    ) -> PromptPlantilla:
        if not prompt_template or not prompt_template.strip():
            raise ValueError("El prompt_template no puede estar vacío")

        if not nombre_etiqueta or not nombre_etiqueta.strip():
            raise ValueError("El nombre_etiqueta no puede estar vacío")

        template = PromptPlantilla(
            nombre_etiqueta=nombre_etiqueta.strip(),
            prompt_template=prompt_template,
            descripcion=descripcion
        )
        
        return self.template_repo.save(template)


class ObtenerTemplate:
    def __init__(self, template_repo: PromptPlantillaRepository):
        self.template_repo = template_repo
    
    def ejecutar(self, nombre_etiqueta: str) -> Optional[PromptPlantilla]:

        return self.template_repo.get_by_nombre_etiqueta(nombre_etiqueta)


class ListarTemplates:
    def __init__(self, template_repo: PromptPlantillaRepository):
        self.template_repo = template_repo
    
    def ejecutar(self):
        return self.template_repo.get_all()


class EliminarTemplate:  
    def __init__(self, template_repo: PromptPlantillaRepository):
        self.template_repo = template_repo
    
    def ejecutar(self, nombre_etiqueta: str) -> bool:
        return self.template_repo.delete_by_nombre_etiqueta(nombre_etiqueta)