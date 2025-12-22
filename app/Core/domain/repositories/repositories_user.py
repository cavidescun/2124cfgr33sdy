from abc import ABC, abstractmethod

from app.Core.domain.entities import UserEntity
from typing import List


class UserRepository(ABC):
    """Interfaz abstracta del repositorio de DenominacionPrograma."""

    @abstractmethod
    def get_all_emails(self) -> List[str]:
        pass



