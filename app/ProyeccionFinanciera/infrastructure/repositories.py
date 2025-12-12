import uuid
from app.Core.infrastructure.models import RegistroCalificado
from app.ProyeccionFinanciera.domain.entities import ProyeccionFinancieraEntity
from app.ProyeccionFinanciera.infrastructure.models import ProyeccionFinanciera
from app.ProyeccionFinanciera.domain.repositories import ProyeccionFinancieraRepository
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist

class ProyeccionFinancieraRepositoryImpl(ProyeccionFinancieraRepository):
    def save(self, proyeccion_entity: ProyeccionFinancieraEntity)  -> ProyeccionFinancieraEntity:
        registro_model = RegistroCalificado.objects.get(llave_documento=proyeccion_entity.llave_maestra)
        proyeccion_model = ProyeccionFinanciera.objects.create(
            llave_maestra = registro_model,
            etiquetas_dinamicas = proyeccion_entity.etiquetas_dinamicas
        )

        return ProyeccionFinancieraEntity(
            id=proyeccion_model.id,
            llave_maestra=proyeccion_model.llave_maestra.llave_documento,
            etiquetas_dinamicas=proyeccion_model.etiquetas_dinamicas,
            creado_en=proyeccion_model.creado_en,
            actualizado_en=proyeccion_model.actualizado_en
        )
    
    def find_by_id(self, id: int) -> ProyeccionFinancieraEntity:
        try:
            model = ProyeccionFinanciera.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise ValueError(f"No existe un acuerdo con id { id}")
        return ProyeccionFinancieraEntity(
            id=model.id,
            llave_maestra=model.llave_maestra,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
        )
    
    def find_by_llave(self, llave_id: str) -> ProyeccionFinancieraEntity:
        try:
            model = ProyeccionFinanciera.objects.get(llave_maestra_id=llave_id)
        except ObjectDoesNotExist:
            raise NotFound(f"No existe un ProyeccionFinanciera de programa con llave {llave_id}")
        return ProyeccionFinancieraEntity(
            id=model.id,
            llave_maestra=model.llave_maestra,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
        )