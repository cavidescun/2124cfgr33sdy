from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any
from enum import Enum


@dataclass
class ActaEntity:
    id: Optional[int]
    llave_maestra: Optional[str]
    etiquetas_dinamicas: Optional[Dict[str, Any]] = None
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None
