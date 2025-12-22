
from app.Core.domain.repositories.repositories import RegistroCalificadoRepository
from app.shared.logic.contextoreporte import ContextoReporte as Word
from app.shared.CrearDocumento import CrearDocumento as CrearDocumentoBase
from app.shared.logic.contextoreporte import ContextoReporte as Word
from rest_framework.exceptions import  ParseError
class CrearDocumento:
    def __init__(self, registro_repo: RegistroCalificadoRepository, crear_documento: Word):    
        self.registro_repo = registro_repo
        self.crear_documento = crear_documento

    def ejecutar(self, llave_id) -> dict:
        entity = self.registro_repo.find_by_llave(llave_id)
        if entity is None:
            raise ParseError("No existe el registro")
        if  not entity.unificado:
            raise ParseError("No se ha unificado toda la informacion")
        informe = entity.informe_final or {}
        variables = informe.get("etiquetas_dinamicas", {}).get("variables", {})
        plantilla = self.seleccionar_plantilla(variables)
        contexto = self.crear_documento(variables=variables)
        servicio = CrearDocumentoBase()
        servicio.generar_multiples_en_segundo_plano(contexto, [plantilla], llave_id)
        return {
            "contexto": contexto.to_dict(),
            "plantilla": plantilla
        }

    def seleccionar_plantilla(self, variables: dict) -> str:
        """
        Retorna la KEY del archivo en S3 según nivel y ciclo o tipo_programa
        """

        nivel = variables.get("nivel", "").strip().lower()
        ciclo = variables.get("ciclo", "").strip().lower()
        tipo_programa = variables.get("tipo_programa", "").strip().lower()

        base_path = "documents/"  # carpeta dentro del bucket

        if nivel == "posgrado":

            if ciclo in ["especialización", "especializacion"]:
                return base_path + "posgrado/especializacion/especializacion.docx"

            if ciclo in ["maestría", "maestria"]:
                return base_path + "posgrado/maestria/maestria.docx"

            if ciclo == "doctorado":
                return base_path + "posgrado/doctorado/doctorado.docx"

            raise Exception(f"No existe plantilla para posgrado con ciclo '{ciclo}'")

        if nivel == "pregrado":

            if tipo_programa in ["técnico", "tecnico"]:
                return base_path + "pregrado/tecnico/tecnico.docx"

            if tipo_programa in ["tecnologo", "tecnológico"]:
                return base_path + "pregrado/tecnologo/tecnologo.docx"

            if tipo_programa == "profesional":
                return base_path + "pregrado/profesional/profesional.docx"

            raise Exception(f"No existe plantilla para pregrado tipo '{tipo_programa}'")

        raise Exception(f"No existe plantilla para nivel '{nivel}'")