from app.ActividadesAcademicas.domain.entities import ActividadesAcademicasEntity
from app.ActividadesAcademicas.domain.repositories import (
    ActividadesAcademicasRepository,
)

from .models import ActividadesAcademicas


class ActividadesAcademicasRepositoryImpl(ActividadesAcademicasRepository):
    def save(
        self, programa: ActividadesAcademicasEntity
    ) -> ActividadesAcademicasEntity:
        model = ActividadesAcademicas.objects.create(**programa.__dict__)
        return ActividadesAcademicasEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )

    def find_by_id(self, id: int) -> ActividadesAcademicasEntity:
        model = ActividadesAcademicas.objects.get(pk=id)
        return ActividadesAcademicasEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )
