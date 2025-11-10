from enum import Enum
from app.Acta.application.schemas.schemas import FormularioPosgrado
import typing
from datetime import date


class FormularioPosgradoMapper:
    
    @staticmethod
    def to_etiquetas(data: dict) -> dict:
        """Frontend → BD (con validación automática)."""
        form_data = data.get("form", data)
        fields_dict = (
            {f["label"]: f["value"] for f in form_data.get("fields", [])}
            if "fields" in form_data
            else data
        )
        formulario = FormularioPosgrado.model_validate(fields_dict)
        variables_dict = formulario.model_dump(by_alias=False, exclude_none=True, mode='json')
        
        return {
            "metadata": {
                "title": form_data.get("title", "Formulario Posgrados"),
                "slug": form_data.get("slug", "formulario-posgrados")
            },
            "variables": variables_dict
        }
    
    @staticmethod
    def from_etiquetas(etiquetas: dict) -> dict:
        """BD → Frontend."""
        variables = etiquetas.get("variables", {})
        metadata = etiquetas.get("metadata", {})
        
        formulario = FormularioPosgrado.model_validate(variables)
    
        fields = [
            {
                "name": name,
                "label": info.alias or name,
                "type": _infer_type(info, getattr(formulario, name)),
                "value": getattr(formulario, name),
                **(_get_options(info) or {})
            }
            for name, info in FormularioPosgrado.model_fields.items()
        ]
        
        return {
            "form": {
                "title": metadata.get("title", "Formulario Posgrados"),
                "slug": metadata.get("slug", "formulario-posgrados"),
                "fields": fields
            }
        }


def _infer_type(field_info, value) -> str:
    """Infiere el tipo de campo basado en el field_info y el valor."""
    annotation = field_info.annotation
    if hasattr(typing, 'get_origin') and typing.get_origin(annotation) is typing.Union:
        args = typing.get_args(annotation)
        annotation = args[0] if args else annotation
    if annotation == date:
        return "date"
    if annotation == bool:
        return "boolean"
    if annotation in (int, float) or (hasattr(annotation, '__origin__') and annotation.__origin__ in (int, float)):
        return "number"
    if hasattr(typing, 'get_origin') and typing.get_origin(annotation) is list:
        return "multiselect"
    if 'EmailStr' in str(annotation):
        return "email"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, (int, float)):
        return "number"
    if isinstance(value, list):
        return "multiselect"
    if isinstance(value, date):
        return "date"
    
    field_name = field_info.alias or ""
    if "perfil" in field_name.lower() or "descripcion" in field_name.lower():
        return "textarea"
    
    if hasattr(annotation, '__mro__') and Enum in annotation.__mro__:
        return "select"
    
    return "text"


def _get_options(field_info) -> dict | None:
    """Obtiene las opciones si el campo es un Enum."""
    annotation = field_info.annotation
    
    if hasattr(typing, 'get_origin') and typing.get_origin(annotation) is typing.Union:
        args = typing.get_args(annotation)
        annotation = args[0] if args else annotation
    
    if hasattr(annotation, '__mro__') and Enum in annotation.__mro__:
        return {"options": [item.value for item in annotation]}
    
    return None