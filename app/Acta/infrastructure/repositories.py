# app/Acta/infrastructure/repositories.py

import uuid
from app.Core.infrastructure.models import RegistroCalificado
from app.Acta.infrastructure.models import  Acta
from app.Acta.domain.entities import ActaEntity
from app.Acta.domain.repositories import ActaRepository
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist
class ActaRepositoryImpl(ActaRepository):
    def save(self, acta_entity: ActaEntity) -> ActaEntity:
        """
        Guarda una Acta en la base de datos, incluyendo quién la creó.
        """

        registro_model = RegistroCalificado.objects.get(llave_documento=acta_entity.llave_maestra)
        acta_model = Acta.objects.create(
            llave_maestra=registro_model,
            etiquetas_dinamicas=acta_entity.etiquetas_dinamicas,
            creado_por_id=acta_entity.creado_por_id, 
        )
        return ActaEntity(
            id=acta_model.id,
            llave_maestra=acta_model.llave_maestra.llave_documento,
            etiquetas_dinamicas=acta_model.etiquetas_dinamicas,
            creado_en=acta_model.creado_en,
            actualizado_en=acta_model.actualizado_en,
            creado_por_id=acta_model.creado_por_id,
        )

    def find_by_id(self, id: int) -> ActaEntity:
        """Recupera una entidad Acta desde la base de datos."""
        try:
            model = Acta.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise ValueError(f"No existe un acta con id {id}")
        return ActaEntity(
            id=model.id,
            llave_maestra=model.llave_maestra,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
        )
