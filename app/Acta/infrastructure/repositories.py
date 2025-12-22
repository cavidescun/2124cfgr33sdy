
from app.Core.infrastructure.models import RegistroCalificado
from app.Acta.infrastructure.models import Acta
from app.Acta.domain.entities import ActaEntity
from app.Acta.domain.repositories import ActaRepository
from rest_framework.exceptions import NotFound, ParseError
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
            estatus=acta_entity.estatus,
            etiquetas_dinamicas=acta_entity.etiquetas_dinamicas,
            creado_por_id=acta_entity.creado_por_id,
        )

        return ActaEntity(
            id=acta_model.id,
            estatus=acta_model.estatus,
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
            aprobado=model.aprobado,
            llave_maestra=model.llave_maestra.llave_documento,  
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
            model = Acta.objects.select_related("llave_maestra").get(
                llave_maestra_id=llave_id
            )
        except Acta.DoesNotExist:
            raise NotFound(f"No existe un acta con llave {llave_id}")


        return ActaEntity(
            id=model.id,
            estatus=model.estatus,
            aprobado=model.aprobado,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    
    def find_by_llave_update(self, llave_id: str) -> ActaEntity:
        """
        Recupera una Acta usando la llave maestra.
        """
        try:
            model = Acta.objects.select_related("llave_maestra").get(
                llave_maestra_id=llave_id
            )
        except Acta.DoesNotExist:
            raise NotFound(f"No existe un acta con llave {llave_id}")

        if model.llave_maestra and model.llave_maestra.unificado:
            raise ParseError(
                "Ya no se puede editar esta parte del proceso porque la información ya fue unificada."
            )

        return ActaEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,
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
        model.etiquetas_dinamicas = acta_entity.etiquetas_dinamicas
        model.modificado_por=acta_entity.modificado_por
        model.save(update_fields=["etiquetas_dinamicas", "actualizado_en","modificado_por"])

        return ActaEntity(
            id=model.id,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    

    def estatus(self, llave_id: str) -> ActaEntity:
        try:
            model = Acta.objects.get(llave_maestra_id=llave_id)
        except Acta.DoesNotExist:
            raise NotFound(f"No existe un acta con llave {llave_id}")
        
        return ActaEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,  
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )




    def find_by_llave_approved(self, llave_id: str) -> ActaEntity:
        """
        Recupera una Acta usando la llave maestra.
        """
        try:
            model = Acta.objects.select_related("llave_maestra").get(
                llave_maestra_id=llave_id
            )
        except Acta.DoesNotExist:
            raise NotFound(f"No existe un acta con llave {llave_id}")

        if model.aprobado:
            raise ParseError(
                "Ya fue aprobado esta acta."
            )

        return ActaEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )

    def aprobar_acta(self, llave_id: str, aprobado: bool, usuario) -> None:
        try:
            model = Acta.objects.get(llave_maestra_id=llave_id)
        except Acta.DoesNotExist:
            raise NotFound(f"No existe un acta con llave {llave_id}")

        if model.aprobado is not None:
            raise ParseError("Ya fue aprobado esta acta.")

        model.aprobado = aprobado
        model.aprobado_por = usuario
        model.save(update_fields=["aprobado", "aprobado_por", "actualizado_en"])