from typing import Optional, List
from app.IAEtiquetas.domain.entities import AnalisisIaEntity, PromptPlantilla
from app.IAEtiquetas.domain.repositories import AnalisisIARepository, PromptPlantillaRepository
from .models import AnalisisIA, PromptTemplateModel


class AnalisisIARepositoryImpl(AnalisisIARepository):
    def save(self, analisis: AnalisisIaEntity) -> AnalisisIaEntity:
        model = AnalisisIA.objects.create(
            nombre_etiqueta=analisis.nombre_etiqueta,
            prompt_usado=analisis.prompt_usado,
            datos_entrada=analisis.datos_entrada,
            resultado=analisis.resultado
        )
        
        return AnalisisIaEntity(
            id=model.id,
            nombre_etiqueta=model.nombre_etiqueta,
            prompt_usado=model.prompt_usado,
            datos_entrada=model.datos_entrada,
            resultado=model.resultado,
            creado_en=model.creado_en
        )
    
    def find_by_id(self, id: int) -> Optional[AnalisisIaEntity]:
        try:
            model = AnalisisIA.objects.get(pk=id)
            return AnalisisIaEntity(
                id=model.id,
                nombre_etiqueta=model.nombre_etiqueta,
                prompt_usado=model.prompt_usado,
                datos_entrada=model.datos_entrada,
                resultado=model.resultado,
                creado_en=model.creado_en
            )
        except AnalisisIA.DoesNotExist:
            return None


class PromptTemplateRepositoryImpl(PromptPlantillaRepository):
    def get_by_nombre_etiqueta(self, nombre_etiqueta: str) -> Optional[PromptPlantilla]:
        try:
            model = PromptTemplateModel.objects.get(
                nombre_etiqueta=nombre_etiqueta,
                activo=True
            )
            return PromptPlantilla(
                nombre_etiqueta=model.nombre_etiqueta,
                prompt_template=model.prompt_template,
                descripcion=model.descripcion
            )
        except PromptTemplateModel.DoesNotExist:
            return None
    
    def save(self, template: PromptPlantilla) -> PromptPlantilla:
        model, created = PromptTemplateModel.objects.update_or_create(
            nombre_etiqueta=template.nombre_etiqueta,
            defaults={
                'prompt_template': template.prompt_template,
                'descripcion': template.descripcion
            }
        )
        
        return PromptPlantilla(
            nombre_etiqueta=model.nombre_etiqueta,
            prompt_template=model.prompt_template,
            descripcion=model.descripcion
        )
    
    def get_all(self) -> List[PromptPlantilla]:
        templates = PromptTemplateModel.objects.filter(activo=True).order_by('nombre_etiqueta')
        return [
            PromptPlantilla(
                nombre_etiqueta=t.nombre_etiqueta,
                prompt_template=t.prompt_template,
                descripcion=t.descripcion
            )
            for t in templates
        ]
    
    def delete_by_nombre_etiqueta(self, nombre_etiqueta: str) -> bool:
        try:
            template = PromptTemplateModel.objects.get(nombre_etiqueta=nombre_etiqueta)
            template.activo = False
            template.save()
            return True
        except PromptTemplateModel.DoesNotExist:
            return False