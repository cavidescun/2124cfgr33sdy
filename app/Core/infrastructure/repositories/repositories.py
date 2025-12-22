from app.Core.domain.entities import RegistroCalificadoEntity
from app.Core.domain.repositories.repositories import RegistroCalificadoRepository
from rest_framework.exceptions import NotFound, ParseError
from ..models import RegistroCalificado
from typing import Dict, List


class RegistroCalificadoRepositoryImpl(RegistroCalificadoRepository):
    """Implementación concreta usando Django ORM."""

    def save(self, programa: RegistroCalificadoEntity) -> RegistroCalificadoEntity:
        data = programa.__dict__.copy()
        if data.get("informe_final") is None:
            data["informe_final"] = {}

        model = RegistroCalificado.objects.create(**data)

        return RegistroCalificadoEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )

    def find_by_id(self, id: int) -> RegistroCalificadoEntity:
        model = RegistroCalificado.objects.get(pk=id)
        return RegistroCalificadoEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )
     
    def find_by_llave(self, llave_id: str) -> RegistroCalificadoEntity:
        try:
            model = RegistroCalificado.objects.get(llave_documento=llave_id)
        except RegistroCalificado.DoesNotExist:
           raise NotFound(f"No existe un RegistroCalificado con llave {llave_id}")
        data = {
            field.name: getattr(model, field.name)
            for field in model._meta.fields
        }
        return RegistroCalificadoEntity(**data)

    def exists_by_llave(self, llave: str) -> bool:
        return RegistroCalificado.objects.filter(llave_documento=llave).exists()
    
    def all(self, page: int = None, page_size: int = None):
        """
        Retorna registros con paginación opcional.
        Si page y page_size son None, retorna todos los registros.
        """
        queryset = RegistroCalificado.objects.all().order_by("-creado_en")
        
        # Si se solicita paginación, aplicarla
        if page is not None and page_size is not None:
            offset = (page - 1) * page_size
            queryset = queryset[offset:offset + page_size]
        
        resultado = []
        for model in queryset:
            data = {
                field.name: getattr(model, field.name)
                for field in sorted(model._meta.fields, key=lambda f: f.name)
                if field.name != "id"
            }
            entity = RegistroCalificadoEntity(
                id=model.id,
                **data
            )
            resultado.append(entity)

        return resultado
    
    def count_all(self) -> int:
        """Retorna el conteo total de registros."""
        return RegistroCalificado.objects.count()
    
    def update_by_llave(self, llave: str, data: dict) -> RegistroCalificadoEntity:
        model = RegistroCalificado.objects.get(llave_documento=llave)

        if model.unificado:
            raise ParseError(
                "No se puede volver a unificar porque el registro ya fue unificado."
            )
        model.informe_final = data
        model.unificado = True
        model.save()
        return model
