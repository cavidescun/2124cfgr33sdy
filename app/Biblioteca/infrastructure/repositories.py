
from app.Core.infrastructure.models.models import RegistroCalificado
from app.Biblioteca.infrastructure.models import Biblioteca
from app.Biblioteca.domain.entities import BibliotecaEntity
from app.Biblioteca.domain.repositories import BibliotecaRepository
from rest_framework.exceptions import NotFound,ParseError
from django.core.exceptions import ObjectDoesNotExist
class BibliotecaRepositoryImpl(BibliotecaRepository):
    def save(self, biblioteca_entity: BibliotecaEntity) -> BibliotecaEntity:
        """
        Guarda una Acta en la base de datos.
        Convierte llave_maestra (string) en instancia del modelo RegistroCalificado.
        """

        registro_model = RegistroCalificado.objects.get(llave_documento=biblioteca_entity.llave_maestra)
        biblioteca_model = Biblioteca.objects.create(
            llave_maestra=registro_model,
            estatus=biblioteca_entity.estatus,
            etiquetas_dinamicas=biblioteca_entity.etiquetas_dinamicas,
            creado_por_id=biblioteca_entity.creado_por_id,
        )

        return BibliotecaEntity(
            id=biblioteca_model.id,
            estatus=biblioteca_model.estatus,
            llave_maestra=biblioteca_model.llave_maestra.llave_documento,
            etiquetas_dinamicas=biblioteca_model.etiquetas_dinamicas,
            creado_en=biblioteca_model.creado_en,
            actualizado_en=biblioteca_model.actualizado_en,
            creado_por_id=biblioteca_model.creado_por_id,
        )
        

    def find_by_id(self, id: int) -> BibliotecaEntity:
        """Recupera una entidad Acta desde la base de datos."""
        try:
            model = Biblioteca.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise ValueError(f"No existe una biblioteca con id {id}")
        return BibliotecaEntity(
            id=model.id,
            llave_maestra=model.llave_maestra,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
        )

    def find_by_llave(self, llave_id: str) -> BibliotecaEntity:
        """Recupera una entidad Acta desde la base de datos usando la llave maestra."""
        try:
            model = Biblioteca.objects.get(llave_maestra_id=llave_id)
        except Biblioteca.DoesNotExist:
           raise NotFound(f"No existe un biblioteca con llave {llave_id}")
        return BibliotecaEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    

    def estatus(self, llave_id: str) -> BibliotecaEntity:
        try:
            model = Biblioteca.objects.get(llave_maestra_id=llave_id)
        except Biblioteca.DoesNotExist:
            raise NotFound(f"No existe un Biblioteca con llave {llave_id}")
        
        return BibliotecaEntity(
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
            model = Biblioteca.objects.get(llave_maestra_id=llave_id)
        except Biblioteca.DoesNotExist:
            return
        if model.estatus is True:
            raise NotFound(
                f"Ya existe un biblioteca activo con la llave {llave_id}"
            )
        return
    
    def find_by_llave_update(self, llave_id: str) -> BibliotecaEntity:
        """
        Recupera una AcuerdoEntity usando la llave maestra.
        """
        try:
            model = Biblioteca.objects.select_related("llave_maestra").get(
                llave_maestra_id=llave_id
            )
        except Biblioteca.DoesNotExist:
            raise NotFound(f"No existe un AcuerdoEntity con llave {llave_id}")

        if model.llave_maestra and model.llave_maestra.unificado:
            raise ParseError(
                "Ya no se puede editar esta parte del proceso porque la información ya fue unificada."
            )

        return BibliotecaEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    
    def update(self, acta_entity: BibliotecaEntity) -> BibliotecaEntity:
        """
        Actualiza una AcuerdoEntity Tecnologica existente.
        """
        try:
            model = Biblioteca.objects.get(llave_maestra_id=acta_entity.llave_maestra)
        except Biblioteca.DoesNotExist:
            raise NotFound(f"No existe un AcuerdoEntity Tecnologica con llave {acta_entity.llave_maestra}")
        model.etiquetas_dinamicas = acta_entity.etiquetas_dinamicas
        model.modificado_por=acta_entity.modificado_por
        model.save(update_fields=[
        "etiquetas_dinamicas",
        "modificado_por",
        "actualizado_en",
    ]) 


        return BibliotecaEntity(
            id=model.id,
            estatus=model.estatus,
            llave_maestra=model.llave_maestra.llave_documento,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
            creado_por_id=model.creado_por_id,
        )
    
        
