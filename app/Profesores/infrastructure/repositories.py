from app.Profesores.domain.entities import ProfesoresEntity
from app.Profesores.domain.repositories import (
    ProfesoresRepository,
)

from .models import Profesores


class ProfesoresRepositoryImpl(ProfesoresRepository):
    def save(self, programa: ProfesoresEntity) -> ProfesoresEntity:
        model = Profesores.objects.create(**programa.__dict__)
        return ProfesoresEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )

    def find_by_id(self, id: int) -> ProfesoresEntity:
        model = Profesores.objects.get(pk=id)
        return ProfesoresEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )
