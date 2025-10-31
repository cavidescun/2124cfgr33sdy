from app.JustificacionPrograma.domain.entities import JustificacionProgramaEntity
from app.JustificacionPrograma.domain.repositories import (
    JustificacionProgramaRepository,
)

from .models import JustificacionPrograma


class JustificacionProgramaRepositoryImpl(JustificacionProgramaRepository):
    def save(
        self, programa: JustificacionProgramaEntity
    ) -> JustificacionProgramaEntity:
        model = JustificacionPrograma.objects.create(**programa.__dict__)
        return JustificacionProgramaEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )

    def find_by_id(self, id: int) -> JustificacionProgramaEntity:
        model = JustificacionPrograma.objects.get(pk=id)
        return JustificacionProgramaEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )
