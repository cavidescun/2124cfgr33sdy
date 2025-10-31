from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any

@dataclass
class ProfesoresEntity:
    id: Optional[int]
    llave_maestra: str
    etiquetas_dinamicas: Optional[Dict[str, Any]] = None
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None
