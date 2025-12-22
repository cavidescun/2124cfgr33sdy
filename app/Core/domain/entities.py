from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class RegistroCalificadoEntity:
    """
    Entidad de dominio pura que representa un registro calificado.
    """

    id: Optional[int]
    llave_documento: str
    numero_acta: str
    tipo: str
    snies: str
    unificado: bool = False   
    informe_final: Optional = None  # type: ignore
    creado_en: Optional[datetime] = None
    actualizado_en: Optional[datetime] = None

    def resumen(self) -> str:
        return f"{self.tipo}: {self.llave_documento} (SNIES {self.snies})"
    

@dataclass
class UserEntity:
    """
    Entidad de dominio pura que representa un usuario del sistema.
    """

    id: Optional[int]
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool
    is_staff: bool

    date_joined: Optional[datetime] = None
    last_login: Optional[datetime] = None

    def nombre_completo(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()

    def puede_recibir_correos(self) -> bool:
        return self.is_active and bool(self.email)
