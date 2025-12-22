from app.Core.infrastructure.models import RegistroCalificado
from app.ProyeccionTecnologica.domain.entities import ProyeccionTecnologicaEntity
from app.ProyeccionTecnologica.models import ProyeccionTecnologica
from app.ProyeccionTecnologica.domain.repositories import ProyeccionTecnologicaRepository
from rest_framework.exceptions import NotFound, ParseError
from django.core.exceptions import ObjectDoesNotExist

class ProyeccionTecnologicaRepositoryImpl(ProyeccionTecnologicaRepository):
    def save(self, proyeccion_entity: ProyeccionTecnologicaEntity)  -> ProyeccionTecnologicaEntity:
        registro_model = RegistroCalificado.objects.get(llave_documento=proyeccion_entity.llave_maestra)
        biblioteca_model = ProyeccionTecnologica.objects.create(
            llave_maestra=registro_model,
            estatus=proyeccion_entity.estatus,
            etiquetas_dinamicas=proyeccion_entity.etiquetas_dinamicas,
            creado_por_id=proyeccion_entity.creado_por_id,
        )

        return ProyeccionTecnologicaEntity(
            id=biblioteca_model.id,
            estatus=biblioteca_model.estatus,
            llave_maestra=biblioteca_model.llave_maestra.llave_documento,
            etiquetas_dinamicas=biblioteca_model.etiquetas_dinamicas,
            creado_en=biblioteca_model.creado_en,
            actualizado_en=biblioteca_model.actualizado_en,
            creado_por_id=biblioteca_model.creado_por_id,
        )
        
    
    def find_by_id(self, id: int) -> ProyeccionTecnologicaEntity:
        try:
            model = ProyeccionTecnologica.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise NotFound(f"No existe un acuerdo con id { id}")
        return ProyeccionTecnologicaEntity(
            id=model.id,
            llave_maestra=model.llave_maestra,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
        )
    
    def find_by_llave(self, llave_id: str) -> ProyeccionTecnologicaEntity:
        try:
            model = ProyeccionTecnologica.objects.get(llave_maestra__llave_documento=llave_id)
        except ObjectDoesNotExist:
            raise NotFound(f"No existe una proyección de infraestructura tecnológica con llave {llave_id}")
        return ProyeccionTecnologicaEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    
    def estatus(self, llave_id: str) -> ProyeccionTecnologicaEntity:
        try:
            model = ProyeccionTecnologica.objects.get(llave_maestra_id=llave_id)
        except ProyeccionTecnologica.DoesNotExist:
            raise NotFound(f"No existe un Proyeccion Infrac Tecnol con llave {llave_id}")
        
        return ProyeccionTecnologicaEntity(
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
            model = ProyeccionTecnologica.objects.get(llave_maestra_id=llave_id)
        except ProyeccionTecnologica.DoesNotExist:
            return
        if model.estatus is True:
            raise NotFound(
                f"Ya existe un Proyeccion Tecnologica activo con la llave {llave_id}"
            )
        return
        
    def find_by_llave_update(self, llave_id: str) -> ProyeccionTecnologicaEntity:
        """
        Recupera una Acta usando la llave maestra.
        """
        try:
            model = ProyeccionTecnologica.objects.select_related("llave_maestra").get(
                llave_maestra_id=llave_id
            )
        except ProyeccionTecnologica.DoesNotExist:
            raise NotFound(f"No existe un acta con llave {llave_id}")

        if model.llave_maestra and model.llave_maestra.unificado:
            raise ParseError(
                "Ya no se puede editar esta parte del proceso porque la información ya fue unificada."
            )

        return ProyeccionTecnologicaEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    
    def update(self, proyeccion_tecnologica_entity: ProyeccionTecnologicaEntity) -> ProyeccionTecnologicaEntity:
        """
        Actualiza una Proyeccion Tecnologica existente.
        """
        try:
            model = ProyeccionTecnologica.objects.get(llave_maestra_id=proyeccion_tecnologica_entity.llave_maestra)
        except ProyeccionTecnologica.DoesNotExist:
            raise NotFound(f"No existe un Proyeccion Tecnologica con llave {proyeccion_tecnologica_entity.llave_maestra}")
        model.etiquetas_dinamicas = proyeccion_tecnologica_entity.etiquetas_dinamicas
        model.modificado_por=proyeccion_tecnologica_entity.modificado_por
        model.save(update_fields=["etiquetas_dinamicas", "actualizado_en","modificado_por"])

        return ProyeccionTecnologicaEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    