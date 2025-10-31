from app.SectorExterno.domain.entities import SectorExternoEntity
from app.SectorExterno.domain.repositories import (
    SectorExternoRepository,
)

from .models import SectorExterno


class SectorExternoRepositoryImpl(SectorExternoRepository):
    def save(
        self, programa: SectorExternoEntity
    ) -> SectorExternoEntity:
        model = SectorExterno.objects.create(**programa.__dict__)
        return SectorExternoEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )

    def find_by_id(self, id: int) -> SectorExternoEntity:
        model = SectorExterno.objects.get(pk=id)
        return SectorExternoEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )
