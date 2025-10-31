import logging
import os
from docx import Document
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
from .contextoreporte import ContextoReporte


class GeneradorReporte:
    """
    Clase responsable de generar documentos Word (.docx) a partir de plantillas y contextos.
    Utiliza `docxtpl` para reemplazar variables, imágenes y tablas dentro de una plantilla DOCX.
    """

    def __init__(self, logger: logging.Logger | None = None):
        self.logger = logger or logging.getLogger(__name__)

    def generar_reporte(
        self,
        plantilla_path: str,
        contexto: ContextoReporte,
        output_file: str = "reporte.docx",
    ) -> None:
        """
        Genera un documento .docx basado en una plantilla y un contexto.
        Guarda el archivo final en el escritorio del usuario si existe,
        o en una carpeta local de respaldo si no.
        """
        self.logger.info(
            f"📝 Iniciando generación de reporte desde plantilla: {plantilla_path}"
        )

        # Intentar guardar en el escritorio del usuario
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        # Si output_file ya tiene una ruta relativa (ej: "reportes/LLAVE-XXX/1.docx")
        if os.path.dirname(output_file):
            # Determinar el directorio base
            if os.path.exists(desktop_path):
                destino = os.path.join(desktop_path, output_file)
            else:
                # Carpeta alternativa dentro del contenedor o app
                fallback_dir = os.path.join(os.getcwd(), "output")
                destino = os.path.join(fallback_dir, output_file)
                self.logger.warning(
                    f"⚠ No se encontró el escritorio. Se usará: {fallback_dir}"
                )

            # CRÍTICO: Crear todos los directorios intermedios
            directorio_destino = os.path.dirname(destino)
            os.makedirs(directorio_destino, exist_ok=True)
            self.logger.debug(f"Directorio asegurado: {directorio_destino}")
        else:
            # Es solo un nombre de archivo, usar Desktop o fallback
            if os.path.exists(desktop_path):
                destino = os.path.join(desktop_path, output_file)
            else:
                fallback_dir = os.path.join(os.getcwd(), "output")
                os.makedirs(fallback_dir, exist_ok=True)
                destino = os.path.join(fallback_dir, output_file)
                self.logger.warning(
                    f"⚠ No se encontró el escritorio. Se usará: {fallback_dir}"
                )

        # Validar plantilla
        if not os.path.exists(plantilla_path):
            msg = f"No se encontró la plantilla: {plantilla_path}"
            self.logger.error(msg)
            raise FileNotFoundError(msg)

        # Eliminar archivo existente si ya estaba
        if os.path.exists(destino):
            try:
                os.remove(destino)
                self.logger.debug(f"Archivo anterior eliminado: {destino}")
            except PermissionError:
                msg = f"Cierra el archivo '{destino}' antes de regenerarlo."
                self.logger.error(msg)
                raise PermissionError(msg)

        # Renderizar documento
        doc = DocxTemplate(plantilla_path)
        context_dict = contexto.to_dict()
        self._insertar_imagenes(doc, contexto, context_dict)

        try:
            doc.render(context_dict)
            doc.save(destino)
            self.logger.info(f"✅ Documento generado correctamente en: {destino}")
        except Exception as e:
            self.logger.error(f"Error al generar documento: {e}", exc_info=True)
            raise RuntimeError(f"Error al generar documento: {e}")

        # Limpieza final
        self._limpiar_filas_vacias(destino)

    # ----------------------------------------------------------------------

    def _insertar_imagenes(
        self, doc: DocxTemplate, contexto: ContextoReporte, context_dict: dict
    ) -> None:
        """
        Inserta las imágenes configuradas en el contexto dentro del documento.
        """
        for img_config in contexto.imagenes:
            if not os.path.exists(img_config.path):
                self.logger.warning(f"⚠ Imagen no encontrada: {img_config.path}")
                continue

            try:
                context_dict[img_config.key] = InlineImage(
                    doc, img_config.path, width=Cm(img_config.width)
                )
                self.logger.debug(f"Imagen insertada correctamente: {img_config.key}")
            except Exception as e:
                self.logger.error(
                    f"Error al insertar imagen {img_config.path}: {e}",
                    exc_info=True,
                )

    # ----------------------------------------------------------------------

    def _limpiar_filas_vacias(self, output_file: str) -> None:
        """
        Elimina filas vacías de las tablas del documento generado.
        """
        try:
            generated_doc = Document(output_file)
            filas_eliminadas = 0

            for table in generated_doc.tables:
                if table.rows:
                    last_row = table.rows[-1]
                    if all(not cell.text.strip() for cell in last_row.cells):
                        table._tbl.remove(last_row._tr)
                        filas_eliminadas += 1

            generated_doc.save(output_file)

            if filas_eliminadas > 0:
                self.logger.debug(
                    f"Se eliminaron {filas_eliminadas} filas vacías en {output_file}"
                )
            else:
                self.logger.debug(f"No se encontraron filas vacías en {output_file}")

        except Exception as e:
            self.logger.warning(f"No se pudo limpiar filas vacías: {e}", exc_info=True)
