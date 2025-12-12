import uuid
from app.Core.infrastructure.models import RegistroCalificado
from app.Acuerdo.domain.entities import AcuerdoEntity
from app.Acuerdo.infrastructure.models import Acuerdo
from app.Acuerdo.domain.repositories import AcuerdoRepository
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist

class AcuerdoRepositoryImpl(AcuerdoRepository):
    def save(self, acuerdo_entity: AcuerdoEntity)  -> AcuerdoEntity:
        registro_model = RegistroCalificado.objects.get(llave_documento=acuerdo_entity.llave_maestra)
        acuerdo_model = Acuerdo.objects.create(
            llave_maestra = registro_model,
            etiquetas_dinamicas = acuerdo_entity.etiquetas_dinamicas
        )

        return AcuerdoEntity(
            id=acuerdo_model.id,
            llave_maestra=acuerdo_model.llave_maestra.llave_documento,
            etiquetas_dinamicas=acuerdo_model.etiquetas_dinamicas,
            creado_en=acuerdo_model.creado_en,
            actualizado_en=acuerdo_model.actualizado_en
        )
    
    def find_by_id(self, id: int) -> AcuerdoEntity:
        try:
            model = Acuerdo.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise ValueError(f"No existe un acuerdo con id { id}")
        return AcuerdoEntity(
            id=model.id,
            llave_maestra=model.llave_maestra,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
        )
    
    def find_by_llave(self, llave_id: str) -> AcuerdoEntity:
        try:
            model = Acuerdo.objects.get(llave_maestra_id=llave_id)
        except ObjectDoesNotExist:

            raise NotFound(f"No existe un acuerdo de programa con llave {llave_id}")
        return AcuerdoEntity(
            id=model.id,
            llave_maestra=model.llave_maestra,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
        )