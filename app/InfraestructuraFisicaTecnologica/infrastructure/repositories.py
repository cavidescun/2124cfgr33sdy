from app.InfraestructuraFisicaTecnologica.domain.entities import (
    InfraestructuraFisicaTecnologicaEntity,
)
from app.InfraestructuraFisicaTecnologica.domain.repositories import (
    InfraestructuraFisicaTecnologicaRepository,
)
from .models import InfraestructuraFisicaTecnologica


class InfraestructuraFisicaTecnologicaImpl(InfraestructuraFisicaTecnologicaRepository):
    """Implementación concreta usando Django ORM."""

    def save(
        self, programa: InfraestructuraFisicaTecnologicaEntity
    ) -> InfraestructuraFisicaTecnologicaEntity:
        model = InfraestructuraFisicaTecnologica.objects.create(**programa.__dict__)
        return InfraestructuraFisicaTecnologicaEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )

    def find_by_id(self, id: int) -> InfraestructuraFisicaTecnologicaEntity:
        model = InfraestructuraFisicaTecnologica.objects.get(pk=id)
        return InfraestructuraFisicaTecnologicaEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )
