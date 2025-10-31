from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class ImagenConfig:
    key: str
    path: str
    width: float = 12.0


@dataclass
class ContextoReporte:
    imagenes: List[ImagenConfig] = field(default_factory=list)
    tablas: Dict[str, List[Dict[str, Any]]] = field(default_factory=dict)
    variables: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {**self.variables, **self.tablas}
