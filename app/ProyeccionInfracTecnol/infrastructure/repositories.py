import uuid
from app.Core.infrastructure.models import RegistroCalificado
from app.ProyeccionInfracTecnol.domain.entities import ProyeccionInfracTecnolEntity
from app.ProyeccionInfracTecnol.models import ProyeccionInfracTecnol
from app.ProyeccionInfracTecnol.domain.repositories import ProyeccionInfracTecnolRepository
from rest_framework.exceptions import NotFound,ParseError
from django.core.exceptions import ObjectDoesNotExist

class ProyeccionInfracTecnolRepositoryImpl(ProyeccionInfracTecnolRepository):
    def save(self, proyeccion_entity: ProyeccionInfracTecnolEntity)  -> ProyeccionInfracTecnolEntity:
        registro_model = RegistroCalificado.objects.get(llave_documento=proyeccion_entity.llave_maestra)
        biblioteca_model = ProyeccionInfracTecnol.objects.create(
            llave_maestra=registro_model,
            estatus=proyeccion_entity.estatus,
            etiquetas_dinamicas=proyeccion_entity.etiquetas_dinamicas,
            creado_por_id=proyeccion_entity.creado_por_id,
        )

        return ProyeccionInfracTecnolEntity(
            id=biblioteca_model.id,
            estatus=biblioteca_model.estatus,
            llave_maestra=biblioteca_model.llave_maestra.llave_documento,
            etiquetas_dinamicas=biblioteca_model.etiquetas_dinamicas,
            creado_en=biblioteca_model.creado_en,
            actualizado_en=biblioteca_model.actualizado_en,
            creado_por_id=biblioteca_model.creado_por_id,
        )
        
    
    def find_by_id(self, id: int) -> ProyeccionInfracTecnolEntity:
        try:
            model = ProyeccionInfracTecnol.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise NotFound(f"No existe un acuerdo con id { id}")
        return ProyeccionInfracTecnolEntity(
            id=model.id,
            llave_maestra=model.llave_maestra,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
        )
    
    def find_by_llave(self, llave_id: str) -> ProyeccionInfracTecnolEntity:
        try:
            model = ProyeccionInfracTecnol.objects.get(llave_maestra__llave_documento=llave_id)
        except ObjectDoesNotExist:
            raise NotFound(f"No existe una proyección de infraestructura tecnológica con llave {llave_id}")
        return ProyeccionInfracTecnolEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    
    def estatus(self, llave_id: str) -> ProyeccionInfracTecnolEntity:
        try:
            model = ProyeccionInfracTecnol.objects.get(llave_maestra_id=llave_id)
        except ProyeccionInfracTecnol.DoesNotExist:
            raise NotFound(f"No existe un Proyeccion Infrac Tecnol con llave {llave_id}")
        
        return ProyeccionInfracTecnolEntity(
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
            model = ProyeccionInfracTecnol.objects.get(llave_maestra_id=llave_id)
        except ProyeccionInfracTecnol.DoesNotExist:
            return
        if model.estatus is True:
            raise NotFound(
                f"Ya existe un Proyeccion Proyeccion Infrac activo con la llave {llave_id}"
            )
        return
    

    
    def find_by_llave_update(self, llave_id: str) -> ProyeccionInfracTecnolEntity:
        """
        Recupera una AcuerdoEntity usando la llave maestra.
        """
        try:
            model = ProyeccionInfracTecnol.objects.select_related("llave_maestra").get(
                llave_maestra_id=llave_id
            )
        except ProyeccionInfracTecnol.DoesNotExist:
            raise NotFound(f"No existe un AcuerdoEntity con llave {llave_id}")

        if model.llave_maestra and model.llave_maestra.unificado:
            raise ParseError(
                "Ya no se puede editar esta parte del proceso porque la información ya fue unificada."
            )

        return ProyeccionInfracTecnolEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    
    def update(self, acta_entity: ProyeccionInfracTecnolEntity) -> ProyeccionInfracTecnolEntity:
        """
        Actualiza una AcuerdoEntity Tecnologica existente.
        """
        try:
            model = ProyeccionInfracTecnol.objects.get(llave_maestra_id=acta_entity.llave_maestra)
        except ProyeccionInfracTecnol.DoesNotExist:
            raise NotFound(f"No existe un AcuerdoEntity Tecnologica con llave {acta_entity.llave_maestra}")
        model.etiquetas_dinamicas = acta_entity.etiquetas_dinamicas
        model.modificado_por=acta_entity.modificado_por
        model.save(update_fields=[
        "etiquetas_dinamicas",
        "modificado_por",
        "actualizado_en",
    ]) 


        return ProyeccionInfracTecnolEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    
        


        
