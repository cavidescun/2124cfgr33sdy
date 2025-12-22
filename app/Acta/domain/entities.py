# app/Acta/domain/entities.py
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any


@dataclass
class ActaEntity:
    id: Optional[int] = None
    llave_maestra: Optional[str] = None
    estatus: Optional[bool] = None
    aprobado: Optional[bool] = None
    etiquetas_dinamicas: Optional[Dict[str, Any]] = None
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None
    creado_por_id: Optional[int] = None
    modificado_por: Optional[int] = None
