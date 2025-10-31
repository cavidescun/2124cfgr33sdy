from app.InvestigacionesInnovacion.domain.entities import InvestigacionesInnovacionEntity
from app.InvestigacionesInnovacion.domain.repositories import (
    InvestigacionesInnovacionRepository,
)

from .models import InvestigacionesInnovacion


class InvestigacionesInnovacionRepositoryImpl(InvestigacionesInnovacionRepository):
    def save(
        self, programa: InvestigacionesInnovacionEntity
    ) -> InvestigacionesInnovacionEntity:
        model = InvestigacionesInnovacion.objects.create(**programa.__dict__)
        return InvestigacionesInnovacionEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )

    def find_by_id(self, id: int) -> InvestigacionesInnovacionEntity:
        model = InvestigacionesInnovacion.objects.get(pk=id)
        return InvestigacionesInnovacionEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )
