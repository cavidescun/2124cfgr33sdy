import logging
import os
import threading


from app.shared.logic.generadoreporte import GeneradorReporte
from app.shared.logic.contextoreporte import ContextoReporte

logger = logging.getLogger(__name__)
generador = GeneradorReporte()


class CrearDocumento:
    def generar_documento(
        self,
        contexto: ContextoReporte,
        plantilla: str,
        nombre_salida: str = "reporte.docx",
        llave_maestra: str = None,
    ) -> None:
        """
        Genera un documento basado en el contexto de reporte proporcionado.
        El contexto incluye imágenes, tablas y variables.

        Args:
            contexto: Contexto con datos del reporte
            plantilla: Ruta de la plantilla a usar
            nombre_salida: Nombre del archivo de salida
            llave_maestra: Carpeta principal donde se guardará el documento
        """
        for imagen in contexto.imagenes:
            if not os.path.exists(imagen.path):
                logger.warning(f"La imagen {imagen.path} no existe.")

        # Si hay llave maestra, construir la ruta completa
        if llave_maestra:
            ruta_completa = os.path.join(llave_maestra, nombre_salida)
        else:
            ruta_completa = nombre_salida

        generador.generar_reporte(plantilla, contexto, ruta_completa)

        for img in contexto.imagenes:
            if os.path.exists(img.path):
                os.remove(img.path)
                logger.debug(f"Imagen temporal eliminada: {img.path}")

    def tarea(
        self,
        contexto: ContextoReporte,
        plantillas: list[str],
        llave_maestra: str = None,
        numero: int = None,
    ):
        """
        Tarea que genera múltiples documentos de forma secuencial.

        Args:
            contexto: Contexto con datos del reporte
            plantillas: Lista de rutas de plantillas
            llave_maestra: Carpeta principal donde se guardarán los documentos
            numero: Número que se usará como nombre del archivo
        """
        for plantilla in plantillas:
            # Si se proporciona número, usarlo como nombre, sino usar el nombre de la plantilla
            if numero is not None:
                nombre_salida = f"{numero}.docx"
            else:
                nombre_salida = f"reporte_{os.path.basename(plantilla)}"

            try:
                logger.info(f"Iniciando generación desde plantilla: {plantilla}")
                self.generar_documento(
                    contexto, plantilla, nombre_salida, llave_maestra
                )
                logger.info(f"Documento generado exitosamente: {nombre_salida}")
            except Exception as e:
                logger.error(f"Error al generar {plantilla}: {e}", exc_info=True)

    def generar_multiples_en_segundo_plano(
        self,
        contexto: ContextoReporte,
        plantillas: list[str],
        llave_maestra: str = None,
        numero: int = None,
    ) -> None:
        """
        Lanza la generación de múltiples documentos en segundo plano usando hilos.

        Args:
            contexto: Contexto con datos del reporte
            plantillas: Lista de rutas de plantillas
            llave_maestra: Carpeta principal donde se guardarán los documentos (ej: "LLAVE-F5557BF5")
            numero: Número que se usará como nombre del archivo (ej: 1 -> "1.docx")
        """
        hilo = threading.Thread(
            target=self.tarea,
            args=(contexto, plantillas, llave_maestra, numero),
            daemon=True,
        )
        hilo.start()
        logger.info(
            f"Generación de documentos lanzada en segundo plano con {len(plantillas)} plantillas."
        )
