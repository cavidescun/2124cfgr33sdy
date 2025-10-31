import random
import string
import uuid
from app.Acta.domain.entities import ActaEntity
from app.Acta.domain.repositories import ActaRepository
from app.Acta.application.mappers import FormularioPosgradoMapper


class CrearActa:
    def __init__(self, repo: ActaRepository):
        self.repo = repo

    def ejectutar(self, **data) -> ActaEntity:
        """
        Crea una entidad Acta a partir del formulario recibido.
        Si el usuario no envía una llave_maestra, se genera automáticamente.
        """

        # 1️⃣ Obtener los campos del formulario
        data_fields = data.get("data", {})

        # 2️⃣ Obtener o generar la llave maestra
        llave_maestra = data.get("llave_maestra")
        if not llave_maestra:
            # Genera una llave única en formato LLAVE-UUID
            llave_maestra = f"LLAVE-{uuid.uuid4().hex[:8].upper()}"

        # 3️⃣ Mapear las etiquetas dinámicas limpias
        etiquetas = FormularioPosgradoMapper.to_etiquetas(data_fields)

        # 4️⃣ Crear la entidad Acta
        acta = ActaEntity(
            id=None,
            llave_maestra=None,
            etiquetas_dinamicas=etiquetas,
        )

        # 5️⃣ Guardar y retornar la entidad persistida
        return self.repo.save(acta)

