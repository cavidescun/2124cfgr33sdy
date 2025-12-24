from app.Core.infrastructure.models.models import RegistroCalificado
from app.ProyeccionFinanciera.domain.entities import ProyeccionFinancieraEntity
from app.ProyeccionFinanciera.infrastructure.models import ProyeccionFinanciera
from app.ProyeccionFinanciera.domain.repositories import ProyeccionFinancieraRepository
from rest_framework.exceptions import NotFound,ParseError
from django.core.exceptions import ObjectDoesNotExist

class ProyeccionFinancieraRepositoryImpl(ProyeccionFinancieraRepository):
    def save(self, proyeccion_entity: ProyeccionFinancieraEntity)  -> ProyeccionFinancieraEntity:

        registro_model = RegistroCalificado.objects.get(llave_documento=proyeccion_entity.llave_maestra)
        biblioteca_model = ProyeccionFinanciera.objects.create(
            llave_maestra=registro_model,
            estatus=proyeccion_entity.estatus,
            etiquetas_dinamicas=proyeccion_entity.etiquetas_dinamicas,
            creado_por_id=proyeccion_entity.creado_por_id,
        )

        return ProyeccionFinancieraEntity(
            id=biblioteca_model.id,
            estatus=biblioteca_model.estatus,
            llave_maestra=biblioteca_model.llave_maestra.llave_documento,
            etiquetas_dinamicas=biblioteca_model.etiquetas_dinamicas,
            creado_en=biblioteca_model.creado_en,
            actualizado_en=biblioteca_model.actualizado_en,
            creado_por_id=biblioteca_model.creado_por_id,
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
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    
    def estatus(self, llave_id: str) -> ProyeccionFinancieraEntity:
        try:
            model = ProyeccionFinanciera.objects.get(llave_maestra_id=llave_id)
        except ProyeccionFinanciera.DoesNotExist:
            raise NotFound(f"No existe un Proyeccion Financiera con llave {llave_id}")
        
        return ProyeccionFinancieraEntity(
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
            model = ProyeccionFinanciera.objects.get(llave_maestra_id=llave_id)
        except ProyeccionFinanciera.DoesNotExist:
            return
        if model.estatus is True:
            raise NotFound(
                f"Ya existe un ProyeccionFinanciera activo con la llave {llave_id}"
            )
        return
    
    def find_by_llave_update(self, llave_id: str) -> ProyeccionFinancieraEntity:
        """
        Recupera una AcuerdoEntity usando la llave maestra.
        """
        try:
            model = ProyeccionFinanciera.objects.select_related("llave_maestra").get(
                llave_maestra_id=llave_id
            )
        except ProyeccionFinanciera.DoesNotExist:
            raise NotFound(f"No existe un AcuerdoEntity con llave {llave_id}")

        if model.llave_maestra and model.llave_maestra.unificado:
            raise ParseError(
                "Ya no se puede editar esta parte del proceso porque la información ya fue unificada."
            )

        return ProyeccionFinancieraEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    
    def update(self, acta_entity: ProyeccionFinancieraEntity) -> ProyeccionFinancieraEntity:
        """
        Actualiza una AcuerdoEntity Tecnologica existente.
        """
        try:
            model = ProyeccionFinanciera.objects.get(llave_maestra_id=acta_entity.llave_maestra)
        except ProyeccionFinanciera.DoesNotExist:
            raise NotFound(f"No existe un AcuerdoEntity Tecnologica con llave {acta_entity.llave_maestra}")
        model.etiquetas_dinamicas = acta_entity.etiquetas_dinamicas
        model.modificado_por=acta_entity.modificado_por
        model.save(update_fields=[
        "etiquetas_dinamicas",
        "modificado_por",
        "actualizado_en",
    ]) 


        return ProyeccionFinancieraEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    
        

