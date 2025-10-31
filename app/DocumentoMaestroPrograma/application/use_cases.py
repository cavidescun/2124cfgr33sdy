"""
Casos de uso para el sistema de unión de documentos Word.
Ubicación: infrastructure/services/use_cases.py
"""

from app.DocumentoMaestroPrograma.infrastructure.services.document_merger import (
    DocumentMerger,
)


class DocumentMergerUseCases:
    """Casos de uso para la gestión de documentos."""

    def __init__(self, base_path="output"):
        """
        Inicializa los casos de uso.

        Args:
            base_path (str): Carpeta raíz donde están las llaves
        """
        self.merger = DocumentMerger(base_path=base_path, verbose=True)

    def unir_y_generar_documento_completo(
        self, llave_maestra, texto_referencia="PRESENTACIÓN"
    ):
        """
        Caso de uso: Unir documentos y generar documento final con TOCs.

        Args:
            llave_maestra (str): Identificador de la llave
            texto_referencia (str): Texto antes del cual insertar las TOCs

        Returns:
            dict: Resultado del proceso con rutas de archivos generados
        """
        try:
            resultado = self.merger.procesar_completo(llave_maestra, texto_referencia)

            if resultado["success"]:
                return {
                    "status": "success",
                    "message": "Documento generado exitosamente",
                    "archivos": {
                        "unificado": resultado["unificado"],
                        "final": resultado["final"],
                    },
                }
            else:
                return {"status": "error", "message": "No se pudo completar el proceso"}
        except Exception as e:
            return {
                "status": "error",
                "message": f"Error al procesar documentos: {str(e)}",
            }

    def unir_documentos_solamente(self, llave_maestra, nombre_salida=None):
        """
        Caso de uso: Solo unir documentos sin agregar TOCs.

        Args:
            llave_maestra (str): Identificador de la llave
            nombre_salida (str, optional): Nombre del archivo de salida

        Returns:
            dict: Resultado del proceso
        """
        try:
            if nombre_salida is None:
                nombre_salida = f"{llave_maestra}_unificado.docx"

            archivo = self.merger.unir_documentos(llave_maestra, nombre_salida)

            if archivo:
                return {
                    "status": "success",
                    "message": "Documentos unidos exitosamente",
                    "archivo": archivo,
                }
            else:
                return {
                    "status": "error",
                    "message": "No se pudieron unir los documentos",
                }
        except Exception as e:
            return {"status": "error", "message": f"Error al unir documentos: {str(e)}"}

    def agregar_indices_a_documento(
        self, ruta_documento, ruta_salida=None, texto_referencia="PRESENTACIÓN"
    ):
        """
        Caso de uso: Agregar índices a un documento existente.

        Args:
            ruta_documento (str): Ruta del documento de entrada
            ruta_salida (str, optional): Ruta del documento de salida
            texto_referencia (str): Texto de referencia para insertar índices

        Returns:
            dict: Resultado del proceso
        """
        try:
            if ruta_salida is None:
                nombre_base = ruta_documento.replace(".docx", "")
                ruta_salida = f"{nombre_base}_con_indices.docx"

            archivo = self.merger.agregar_toc(
                ruta_documento, ruta_salida, texto_referencia
            )

            return {
                "status": "success",
                "message": "Índices agregados exitosamente",
                "archivo": archivo,
            }
        except Exception as e:
            return {"status": "error", "message": f"Error al agregar índices: {str(e)}"}

    def procesar_multiples_llaves(self, lista_llaves, texto_referencia="PRESENTACIÓN"):
        """
        Caso de uso: Procesar múltiples llaves en lote.

        Args:
            lista_llaves (list): Lista de llaves a procesar
            texto_referencia (str): Texto de referencia para TOCs

        Returns:
            dict: Resultados del procesamiento en lote
        """
        resultados = []
        exitosos = 0
        fallidos = 0

        for llave in lista_llaves:
            self.merger._print(f"\n{'='*60}")
            self.merger._print(f"Procesando llave: {llave}")
            self.merger._print(f"{'='*60}")

            resultado = self.unir_y_generar_documento_completo(llave, texto_referencia)

            if resultado["status"] == "success":
                exitosos += 1
            else:
                fallidos += 1

            resultados.append({"llave": llave, "resultado": resultado})

        return {
            "status": "completed",
            "total": len(lista_llaves),
            "exitosos": exitosos,
            "fallidos": fallidos,
            "detalles": resultados,
        }

    def cambiar_modo_verbose(self, verbose):
        """
        Cambia el modo verbose del merger.

        Args:
            verbose (bool): True para activar mensajes, False para desactivar
        """
        self.merger.verbose = verbose
