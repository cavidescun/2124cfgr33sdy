from abc import ABC, abstractmethod


class EmailService(ABC):

    @abstractmethod
    def send_email(self, to: str | list[str], subject: str, html_body: str) -> None:
        pass
