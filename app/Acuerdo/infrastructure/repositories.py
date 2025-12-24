
from app.Core.infrastructure.models.models import RegistroCalificado
from app.Acuerdo.domain.entities import AcuerdoEntity
from app.Acuerdo.infrastructure.models import Acuerdo
from app.Acuerdo.domain.repositories import AcuerdoRepository
from rest_framework.exceptions import NotFound,ParseError
from django.core.exceptions import ObjectDoesNotExist

class AcuerdoRepositoryImpl(AcuerdoRepository):
    def save(self, acuerdo_entity: AcuerdoEntity)  -> AcuerdoEntity:
        registro_model = RegistroCalificado.objects.get(llave_documento=acuerdo_entity.llave_maestra)
        acuerdo_model = Acuerdo.objects.create(
            llave_maestra=registro_model,
            estatus=acuerdo_entity.estatus,
            etiquetas_dinamicas=acuerdo_entity.etiquetas_dinamicas,
            creado_por_id=acuerdo_entity.creado_por_id,
        )

        return AcuerdoEntity(
            id=acuerdo_model.id,
            estatus=acuerdo_model.estatus,
            llave_maestra=acuerdo_model.llave_maestra.llave_documento,
            etiquetas_dinamicas=acuerdo_model.etiquetas_dinamicas,
            creado_en=acuerdo_model.creado_en,
            actualizado_en=acuerdo_model.actualizado_en,
            creado_por_id=acuerdo_model.creado_por_id,
        )
    
    def find_by_id(self, id: int) -> AcuerdoEntity:
        try:
            model = Acuerdo.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise ValueError(f"No existe un acuerdo con id { id}")
        return AcuerdoEntity(
            id=model.id,
            llave_maestra=model.llave_maestra,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
        )
    
    def find_by_llave(self, llave_id: str) -> AcuerdoEntity:
        try:
            model = Acuerdo.objects.get(llave_maestra_id=llave_id)
        except ObjectDoesNotExist:

            raise NotFound(f"No existe un acuerdo de programa con llave {llave_id}")
        return AcuerdoEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    
    def estatus(self, llave_id: str) -> AcuerdoEntity:
        try:
            model = Acuerdo.objects.get(llave_maestra_id=llave_id)
        except Acuerdo.DoesNotExist:
            raise NotFound(f"No existe un Acuerdo con llave {llave_id}")
        
        return AcuerdoEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,  
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    
    def estatus_flag(self, llave_id: str) -> None:
        try:
            model = Acuerdo.objects.get(llave_maestra_id=llave_id)
        except Acuerdo.DoesNotExist:
            return
        if model.estatus is True:
            raise NotFound(
                f"Ya existe un Acuerdo activo con la llave {llave_id}"
            )
        return
    
    def find_by_llave_update(self, llave_id: str) -> AcuerdoEntity:
        """
        Recupera una AcuerdoEntity usando la llave maestra.
        """
        try:
            model = Acuerdo.objects.select_related("llave_maestra").get(
                llave_maestra_id=llave_id
            )
        except Acuerdo.DoesNotExist:
            raise NotFound(f"No existe un AcuerdoEntity con llave {llave_id}")

        if model.llave_maestra and model.llave_maestra.unificado:
            raise ParseError(
                "Ya no se puede editar esta parte del proceso porque la información ya fue unificada."
            )

        return AcuerdoEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    
    def update(self, acta_entity: AcuerdoEntity) -> AcuerdoEntity:
        """
        Actualiza una AcuerdoEntity Tecnologica existente.
        """
        try:
            model = Acuerdo.objects.get(llave_maestra_id=acta_entity.llave_maestra)
        except Acuerdo.DoesNotExist:
            raise NotFound(f"No existe un AcuerdoEntity Tecnologica con llave {acta_entity.llave_maestra}")
        model.etiquetas_dinamicas = acta_entity.etiquetas_dinamicas
        model.modificado_por=acta_entity.modificado_por
        model.save(update_fields=[
        "etiquetas_dinamicas",
        "modificado_por",
        "actualizado_en",
    ])


        return AcuerdoEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    
        
