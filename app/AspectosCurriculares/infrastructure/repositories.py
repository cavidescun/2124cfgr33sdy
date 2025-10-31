from app.AspectosCurriculares.domain.entities import AspectosCurricularesEntity
from app.AspectosCurriculares.domain.repositories import (
    AspectosCurricularesRepository,
)

from .models import AspectosCurriculares


class AspectosCurricularesRepositoryImpl(AspectosCurricularesRepository):
    def save(
        self, programa: AspectosCurricularesEntity
    ) -> AspectosCurricularesEntity:
        model = AspectosCurriculares.objects.create(**programa.__dict__)
        return AspectosCurricularesEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )

    def find_by_id(self, id: int) -> AspectosCurricularesEntity:
        model = AspectosCurriculares.objects.get(pk=id)
        return AspectosCurricularesEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )
