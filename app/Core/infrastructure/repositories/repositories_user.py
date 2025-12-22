from django.contrib.auth import get_user_model
from typing import List

from app.Core.domain.repositories.repositories_user import UserRepository

class UserRepositoryImpl(UserRepository):

    def get_all_emails(self) -> List[str]:
        User = get_user_model()
        return list(
            User.objects
            .filter(is_active=True)
            .exclude(email__isnull=True)
            .exclude(email__exact="")
            .values_list("email", flat=True)
        )
