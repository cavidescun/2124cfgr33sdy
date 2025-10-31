# app/Acta/infrastructure/repositories.py

import uuid
from app.Core.infrastructure.models import RegistroCalificado
from app.Acta.infrastructure.models import  Acta
from app.Acta.domain.entities import ActaEntity
from app.Acta.domain.repositories import ActaRepository
from rest_framework.exceptions import NotFound

class ActaRepositoryImpl(ActaRepository):
    def save(self, programa: ActaEntity) -> ActaEntity:
        """
        Guarda una entidad Acta en la base de datos usando el ORM de Django.
        Si no se pasa una llave_maestra, genera una automáticamente (única).
        """

        data = programa.__dict__.copy()
        if not data.get("llave_maestra"):
            nueva_llave = str(uuid.uuid4())
            registro = RegistroCalificado.objects.create(llave_documento=nueva_llave)
            data["llave_maestra"] = registro
        else:
            try:
                data["llave_maestra"] = RegistroCalificado.objects.get(
                    llave_documento=data["llave_maestra"]
                )
            except RegistroCalificado.DoesNotExist:
                raise NotFound(detail=f"No existe un RegistroCalificado con llave_documento='{data['llave_maestra']}'")

        model = Acta.objects.create(**data)
        return ActaEntity(
            id=model.id,
            llave_maestra=model.llave_maestra,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
        )

    def find_by_id(self, id: int) -> ActaEntity:
        """Recupera una entidad Acta desde la base de datos."""
        model = Acta.objects.get(pk=id)
        return ActaEntity(
            id=model.id,
            llave_maestra=model.llave_maestra,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
        )
    def find_by_id(self, id: int) -> ActaEntity:
        """Recupera una entidad Acta desde la base de datos."""
        model = Acta.objects.get(pk=id)
        return ActaEntity(
            id=model.id,
            llave_maestra=model.llave_maestra,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
        )
