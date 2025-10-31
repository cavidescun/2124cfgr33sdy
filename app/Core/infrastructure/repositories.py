from app.Core.domain.entities import RegistroCalificadoEntity
from app.Core.domain.repositories import RegistroCalificadoRepository

from .models import RegistroCalificado


class RegistroCalificadoRepositoryImpl(RegistroCalificadoRepository):
    """Implementación concreta usando Django ORM."""

    def save(self, programa: RegistroCalificadoEntity) -> RegistroCalificadoEntity:
        model = RegistroCalificado.objects.create(**programa.__dict__)
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
