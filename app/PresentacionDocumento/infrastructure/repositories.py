from app.PresentacionDocumento.domain.entities import PresentacionDocumentoEntity
from app.PresentacionDocumento.domain.repositories import PresentacionDocumentoRepository

from .models import PresentacionDocumento


class PresentacionDocumentoRepositoryImpl(PresentacionDocumentoRepository):
    """Implementación concreta usando Django ORM."""

    def save(self, programa: PresentacionDocumentoEntity) -> PresentacionDocumentoEntity:
        model = PresentacionDocumento.objects.create(**programa.__dict__)
        return PresentacionDocumento(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )

    def find_by_id(self, id: int) -> PresentacionDocumentoEntity:
        model = PresentacionDocumento.objects.get(pk=id)
        return PresentacionDocumentoEntity(
            id=model.id,
            **{
                field.name: getattr(model, field.name)
                for field in model._meta.fields
                if field.name != "id"
            }
        )
