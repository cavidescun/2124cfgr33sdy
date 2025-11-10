from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from enum import Enum
from datetime import date


class Nivel(str, Enum):
    PREGRADO = "Pregrado"
    POSGRADO = "Posgrado"


class Ciclo(str, Enum):
    ESPECIALIZACION = "Especialización"
    MAESTRIA = "Maestría"
    DOCTORADO = "Doctorado"


class TipoRegistro(str, Enum):
    REGISTRO_CALIFICADO = "Registro Calificado"
    ACREDITACION = "Acreditación"


class Modalidad(str, Enum):
    PRESENCIAL = "Presencial"
    VIRTUAL = "Virtual"
    MIXTA = "Mixta"


class Periodicidad(str, Enum):
    SEMESTRAL = "Semestral"
    ANUAL = "Anual"
    TRIMESTRAL = "Trimestral"


class CampoAmplio(str, Enum):
    INGENIERIA = "Ingeniería, Industria y Construcción"
    CIENCIAS_SOCIALES = "Ciencias Sociales"
    EDUCACION = "Educación"
    SALUD = "Salud"
    ARTES = "Artes"


class AreaConocimiento(str, Enum):
    BELLAS_ARTES = "Bellas Artes"
    CIENCIAS_SOCIALES = "Ciencias Sociales"
    CIENCIAS_NATURALES = "Ciencias Naturales"
    INGENIERIA = "Ingeniería"


class FormularioPosgrado(BaseModel):
    proceso: str = Field(alias="Proceso")
    busqueda_snies: int = Field(alias="Búsqueda de SNIES")
    nivel: Nivel = Field(alias="Nivel")
    ciclo: Ciclo = Field(alias="Ciclo")
    tipo_registro: TipoRegistro = Field(alias="Tipo de Registro")
    escuela_datos: str = Field(alias="Escuela")
    correo_director: EmailStr = Field(alias="Correo del Director de Escuela")
    viabilidad_financiera: bool = Field(alias="Viabilidad Financiera")
    fecha: date = Field(alias="Fecha de Creación")
    nombre_de_programa: str = Field(alias="Nombre de la Especialización", max_length=200)
    titulo_especialista: str = Field(alias="Título de la Especialización a Otorgar", max_length=200)
    perfil_especialista: str = Field(default="", alias="Perfil de la Especialización")
    duracion_programa: int = Field(alias="Duración de la Especialización (meses)", gt=0)
    regional_programa: str = Field(default="", alias="Regional(es)")
    periodicidad_programa: Periodicidad = Field(alias="Periodicidad de Admisión")
    admitidos_programa: int = Field(alias="Cantidad de Estudiantes 1er Semestre", ge=0)
    modalidad_programa: Modalidad = Field(alias="Modalidad")
    campo_amplio: CampoAmplio = Field(alias="Campo Amplio")
    campo_especifico: str = Field(alias="Campo Específico")
    campo_detallado: str = Field(alias="Campo Detallado")
    area_de_conocimiento: AreaConocimiento = Field(alias="Área del Conocimiento")
    nucleo_basico_conocimiento: str = Field(alias="Núcleo Básico del Conocimiento")
    programas_similares: List[str] = Field(default_factory=list, alias="Programas Similares")

    model_config = {"populate_by_name": True, "use_enum_values": True}