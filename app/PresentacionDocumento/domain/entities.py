from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any


@dataclass
class PresentacionDocumentoEntity:
    """
    Entidad de dominio pura: representa un programa con etiquetas dinámicas.
    """

    id: Optional[int]
    llave_maestra: str
    etiquetas_dinamicas: Optional[Dict[str, Any]] = None
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None
