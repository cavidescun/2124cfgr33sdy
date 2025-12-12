
from app.Core.infrastructure.models import RegistroCalificado
from app.Acta.infrastructure.models import Acta
from app.Acta.domain.entities import ActaEntity
from app.Acta.domain.repositories import ActaRepository
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist


class ActaRepositoryImpl(ActaRepository):

    def save(self, acta_entity: ActaEntity) -> ActaEntity:
        """
        Crea una Acta nueva en la base de datos.
        """
        registro_model = RegistroCalificado.objects.get(
            llave_documento=acta_entity.llave_maestra
        )

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
        """
        Recupera una Acta usando su ID.
        """
        try:
            model = Acta.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise NotFound(f"No existe un acta con id {id}")

        return ActaEntity(
            id=model.id,
            llave_maestra=model.llave_maestra.llave_documento,  # FIX ✔
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )

    def find_by_llave(self, llave_id: str) -> ActaEntity:
        """
        Recupera una Acta usando la llave maestra.
        """
        try:
            model = Acta.objects.get(llave_maestra_id=llave_id)
        except Acta.DoesNotExist:
            raise NotFound(f"No existe un acta con llave {llave_id}")

        return ActaEntity(
            id=model.id,
            llave_maestra=model.llave_maestra.llave_documento,  # FIX ✔
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )

    def update(self, acta_entity: ActaEntity) -> ActaEntity:
        """
        Actualiza una Acta existente.
        """
        try:
            model = Acta.objects.get(llave_maestra_id=acta_entity.llave_maestra)
        except Acta.DoesNotExist:
            raise NotFound(f"No existe un acta con llave {acta_entity.llave_maestra}")

        # Actualiza solo etiquetas dinámicas
        model.etiquetas_dinamicas = acta_entity.etiquetas_dinamicas
        model.save(update_fields=["etiquetas_dinamicas", "actualizado_en"])

        return ActaEntity(
            id=model.id,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
