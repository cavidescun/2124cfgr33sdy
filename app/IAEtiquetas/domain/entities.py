from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any

@dataclass
class PromptPlantilla:
    nombre_etiqueta: str
    prompt_template: str
    descripcion: Optional[str] = None


@dataclass
class AnalisisIaEntity:
    id: Optional[int]
    nombre_etiqueta: str
    prompt_usado: str
    datos_entrada: Dict[str, Any]
    resultado: str
    creado_en: Optional[datetime] = None