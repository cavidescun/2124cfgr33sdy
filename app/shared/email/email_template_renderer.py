from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path


class EmailTemplateRenderer:
    def __init__(self):
        templates_path = Path(__file__).parent / "templates"

        self.env = Environment(
            loader=FileSystemLoader(templates_path),
            autoescape=select_autoescape(["html", "xml"])
        )

    def render(self, template_name: str, **context) -> str:
        template = self.env.get_template(template_name)
        return template.render(**context)
