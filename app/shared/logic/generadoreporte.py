import logging
import os
from docx import Document
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
from .contextoreporte import ContextoReporte
from app.shared.utils.tabla_contenido.crear_toc_y_convertir_pdf import GestorTablaContenido


class GeneradorReporte:
    """
    Clase responsable de generar documentos Word (.docx) a partir de plantillas y contextos.
    Utiliza `docxtpl` para reemplazar variables, imágenes y tablas dentro de una plantilla DOCX.
    Opcionalmente puede agregar tablas de contenido y convertir a PDF.
    """

    def __init__(self, logger: logging.Logger | None = None):
        self.logger = logger or logging.getLogger(__name__)
        # Inicializar gestor de TOC con el mismo logger
        self.gestor_toc = GestorTablaContenido(logger=self.logger)

    def generar_reporte(
        self,
        plantilla_path: str,
        contexto: ContextoReporte,
        output_file: str = "reporte.docx",
        agregar_toc: bool = True,
        texto_referencia_toc: str = "PRESENTACIÓN",
        convertir_pdf: bool = False
    ) -> str:

        self.logger.info(
            f"📝 Iniciando generación de reporte desde plantilla: {plantilla_path}"
        )

        # Determinar ruta destino
        destino = self._determinar_ruta_destino(output_file)

        # Validar plantilla
        if not os.path.exists(plantilla_path):
            raise FileNotFoundError(f"No se encontró la plantilla: {plantilla_path}")

        # Eliminar archivo existente
        self._eliminar_archivo_existente(destino)

        # Renderizar DOCX
        doc = DocxTemplate(plantilla_path)
        context_dict = contexto.to_dict()
        self._insertar_imagenes(doc, contexto, context_dict)

        # Validar variables antes del render
        self._validar_y_reportar_variables(doc, context_dict)

        # Guardar documento generado
        try:
            doc.render(context_dict)
            doc.save(destino)
            self.logger.info(f"✅ Documento generado en: {destino}")
        except Exception as e:
            self.logger.error(f"Error al generar documento: {e}", exc_info=True)
            raise

        # 🚀 PRIMERO agregar TOCs (documento fresco)
        if agregar_toc:
            self.logger.warning("🔥 Ejecutando inserción de tablas de contenido…")
            self._agregar_tablas_contenido(destino, texto_referencia_toc)

        # 🚀 Después limpiar filas vacías (python-docx no rompe TOC)
        self._limpiar_filas_vacias(destino)

        # Convertir a PDF
        if convertir_pdf:
            self._convertir_documento_a_pdf(destino)

        return destino

    # ----------------------------------------------------------------------
    # MÉTODOS PRIVADOS - ORGANIZACIÓN DEL FLUJO
    # ----------------------------------------------------------------------

    def _determinar_ruta_destino(self, output_file: str) -> str:
        """Determina la ruta completa donde se guardará el documento."""
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        if os.path.dirname(output_file):
            # output_file tiene ruta relativa (ej: "reportes/LLAVE-XXX/1.docx")
            if os.path.exists(desktop_path):
                destino = os.path.join(desktop_path, output_file)
            else:
                fallback_dir = os.path.join(os.getcwd(), "output")
                destino = os.path.join(fallback_dir, output_file)
                self.logger.warning(
                    f"⚠ No se encontró el escritorio. Se usará: {fallback_dir}"
                )

            # Crear directorios intermedios
            directorio_destino = os.path.dirname(destino)
            os.makedirs(directorio_destino, exist_ok=True)
            self.logger.debug(f"Directorio asegurado: {directorio_destino}")
        else:
            # Es solo un nombre de archivo
            if os.path.exists(desktop_path):
                destino = os.path.join(desktop_path, output_file)
            else:
                fallback_dir = os.path.join(os.getcwd(), "output")
                os.makedirs(fallback_dir, exist_ok=True)
                destino = os.path.join(fallback_dir, output_file)
                self.logger.warning(
                    f"⚠ No se encontró el escritorio. Se usará: {fallback_dir}"
                )

        return destino

    def _eliminar_archivo_existente(self, destino: str) -> None:
        """Elimina el archivo si ya existe para evitar conflictos."""
        if os.path.exists(destino):
            try:
                os.remove(destino)
                self.logger.debug(f"Archivo anterior eliminado: {destino}")
            except PermissionError:
                msg = f"Cierra el archivo '{destino}' antes de regenerarlo."
                self.logger.error(msg)
                raise PermissionError(msg)

    def _validar_y_reportar_variables(self, doc: DocxTemplate, context_dict: dict) -> None:
        """Valida variables de la plantilla y reporta problemas."""
        validacion = self.validar_variables_faltantes(doc, context_dict)

        if validacion['faltantes'] or validacion['vacias']:
            total_problemas = len(validacion['faltantes']) + len(validacion['vacias'])
            self.logger.warning(
                f"⚠ Se encontraron {total_problemas} variable(s) con problemas:"
            )

            if validacion['faltantes']:
                self.logger.warning(
                    f"   Variables NO definidas en contexto ({len(validacion['faltantes'])}):"
                )
                for var in validacion['faltantes']:
                    self.logger.warning(f"      • {var}")

            if validacion['vacias']:
                self.logger.warning(
                    f"   Variables definidas pero VACÍAS ({len(validacion['vacias'])}):"
                )
                for var in validacion['vacias']:
                    self.logger.warning(f"      • {var} = {repr(context_dict.get(var))}")

    def _agregar_tablas_contenido(self, destino: str, texto_referencia: str) -> None:
        """Agrega tablas de contenido al documento generado."""
        self.logger.info("📑 Agregando tablas de contenido...")
        exito_toc = self.gestor_toc.agregar_todas_las_toc(
            doc_path=destino,
            output_path=destino,  # Sobreescribe el mismo archivo
            texto_buscar=texto_referencia,
            incluir_salto_pagina=True
        )

        if exito_toc:
            self.logger.info("✅ Tablas de contenido agregadas correctamente")
            self.logger.info(
                "💡 Recuerda: Abre el documento en Word y presiona Ctrl+A → F9 para actualizar los índices"
            )
        else:
            self.logger.warning("⚠ No se pudieron agregar las tablas de contenido")

    def _convertir_documento_a_pdf(self, destino: str) -> None:
        """Convierte el documento Word a PDF."""
        self.logger.info("📄 Convirtiendo documento a PDF...")
        pdf_path = destino.replace('.docx', '.pdf')
        exito_pdf = self.gestor_toc.convertir_a_pdf(destino, pdf_path)

        if exito_pdf:
            self.logger.info(f"✅ PDF generado: {pdf_path}")
        else:
            self.logger.warning("⚠ No se pudo convertir a PDF automáticamente")

    # ----------------------------------------------------------------------
    # MÉTODOS PÚBLICOS - VALIDACIÓN Y PROCESAMIENTO
    # ----------------------------------------------------------------------

    def validar_variables_faltantes(self, doc: DocxTemplate, context_dict: dict) -> dict:
        """
        Valida qué variables de la plantilla no están en el contexto o están vacías.
        
        Returns:
            dict con keys: 'faltantes', 'vacias', 'total_variables', 'ok'
        """
        try:
            variables_plantilla = doc.get_undeclared_template_variables()

            faltantes = []
            vacias = []

            for var in variables_plantilla:
                if var not in context_dict:
                    faltantes.append(var)
                else:
                    valor = context_dict[var]
                    if valor is None or valor == "" or valor == [] or valor == {}:
                        vacias.append(var)

            return {
                'faltantes': sorted(faltantes),
                'vacias': sorted(vacias),
                'total_variables': len(variables_plantilla),
                'ok': len(faltantes) == 0 and len(vacias) == 0
            }

        except Exception as e:
            self.logger.error(f"Error al validar variables: {e}", exc_info=True)
            return {
                'faltantes': [],
                'vacias': [],
                'total_variables': 0,
                'ok': False,
                'error': str(e)
            }

    # ----------------------------------------------------------------------

    def _insertar_imagenes(
        self, doc: DocxTemplate, contexto: ContextoReporte, context_dict: dict
    ) -> None:
        """Inserta las imágenes configuradas en el contexto dentro del documento."""
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
        """Elimina filas vacías de las tablas del documento generado."""
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