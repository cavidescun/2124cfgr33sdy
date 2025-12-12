import uuid
from app.Core.infrastructure.models import RegistroCalificado
from app.ProyeccionInfracTecnol.domain.entities import ProyeccionInfracTecnolEntity
from app.ProyeccionInfracTecnol.models import ProyeccionInfracTecnol
from app.ProyeccionInfracTecnol.domain.repositories import ProyeccionInfracTecnolRepository
from rest_framework.exceptions import NotFound
from django.core.exceptions import ObjectDoesNotExist

class ProyeccionInfracTecnolRepositoryImpl(ProyeccionInfracTecnolRepository):
    def save(self, proyeccion_entity: ProyeccionInfracTecnolEntity)  -> ProyeccionInfracTecnolEntity:
        registro_model = RegistroCalificado.objects.get(llave_documento=proyeccion_entity.llave_maestra)
        proyeccion_model = ProyeccionInfracTecnol.objects.create(
            llave_maestra = registro_model,
            etiquetas_dinamicas = proyeccion_entity.etiquetas_dinamicas
        )

        return ProyeccionInfracTecnolEntity(
            id=proyeccion_model.id,
            llave_maestra=proyeccion_model.llave_maestra.llave_documento,
            etiquetas_dinamicas=proyeccion_model.etiquetas_dinamicas,
            creado_en=proyeccion_model.creado_en,
            actualizado_en=proyeccion_model.actualizado_en
        )
    
    def find_by_id(self, id: int) -> ProyeccionInfracTecnolEntity:
        try:
            model = ProyeccionInfracTecnol.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise NotFound(f"No existe un acuerdo con id { id}")
        return ProyeccionInfracTecnolEntity(
            id=model.id,
            llave_maestra=model.llave_maestra,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
        )
    
    def find_by_llave(self, llave_id: str) -> ProyeccionInfracTecnolEntity:
        try:
            model = ProyeccionInfracTecnol.objects.get(llave_maestra__llave_documento=llave_id)
        except ObjectDoesNotExist:
            raise NotFound(f"No existe una proyección de infraestructura tecnológica con llave {llave_id}")
        return ProyeccionInfracTecnolEntity(
            id=model.id,
            llave_maestra=model.llave_maestra,
            etiquetas_dinamicas=model.etiquetas_dinamicas,
            creado_en=model.creado_en,
            actualizado_en=model.actualizado_en,
        )