from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any


@dataclass
class InfraestructuraFisicaTecnologicaEntity:
    """
    Entidad de dominio pura: representa un InfraestructuraFisicaTecnologica con etiquetas dinámicas.
    """

    id: Optional[int]
    llave_maestra: str = None
    etiquetas_dinamicas: Optional[Dict[str, Any]] = None
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None
