from app.DenominacionPrograma.domain.entities import DenominacionProgramaEntity
from app.DenominacionPrograma.domain.repositories import DenominacionProgramaRepository

from .models import DenominacionPrograma


class DenominacionProgramaRepositoryImpl(DenominacionProgramaRepository):
    """Implementación concreta usando Django ORM."""

    def save(self, programa: DenominacionProgramaEntity) -> DenominacionProgramaEntity:
        model = DenominacionPrograma.objects.create(**programa.__dict__)
        return DenominacionProgramaEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )

    def find_by_id(self, id: int) -> DenominacionProgramaEntity:
        model = DenominacionPrograma.objects.get(pk=id)
        return DenominacionProgramaEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )
