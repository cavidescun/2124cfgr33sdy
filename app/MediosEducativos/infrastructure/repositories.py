from app.MediosEducativos.domain.entities import MediosEducativosEntity
from app.MediosEducativos.domain.repositories import (
    MediosEducativosRepository,
)

from .models import MediosEducativos


class MediosEducativosRepositoryImpl(MediosEducativosRepository):
    def save(
        self, programa: MediosEducativosEntity
    ) -> MediosEducativosEntity:
        model = MediosEducativos.objects.create(**programa.__dict__)
        return MediosEducativosEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )

    def find_by_id(self, id: int) -> MediosEducativosEntity:
        model = MediosEducativos.objects.get(pk=id)
        return MediosEducativosEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )
