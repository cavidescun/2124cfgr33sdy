import logging
import tempfile
from pathlib import Path
from docx import Document
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
import boto3

from .contextoreporte import ContextoReporte
from app.shared.utils.tabla_contenido.crear_toc_y_convertir_pdf import (
    GestorTablaContenido
)


class GeneradorReporte:
    """
    Genera documentos Word (.docx) a partir de plantillas almacenadas en S3
    y guarda el resultado FINAL únicamente en S3.

    No persiste ningún archivo en la máquina (solo temporales).
    """

    def __init__(self, logger: logging.Logger | None = None):
        self.logger = logger or logging.getLogger(__name__)
        self.gestor_toc = GestorTablaContenido(logger=self.logger)

        self.s3 = boto3.client("s3")
        self.bucket_name = "cun-repo-registrocalificado"

    # ------------------------------------------------------------------
    # MÉTODO PRINCIPAL
    # ------------------------------------------------------------------

    def generar_reporte(
        self,
        plantilla_s3_key: str,
        contexto: ContextoReporte,
        s3_destino: str,
        agregar_toc: bool = True,
        texto_referencia_toc: str = "PRESENTACIÓN"
    ) -> str:
        """
        Genera el documento a partir de una plantilla en S3 y guarda
        el resultado final SOLO en S3.
        """

        plantilla_tmp: Path | None = None
        salida_tmp: Path | None = None

        try:
            # 1️⃣ Descargar plantilla (temporal)
            plantilla_tmp = self._descargar_desde_s3_tmp(plantilla_s3_key)

            # 2️⃣ Crear archivo temporal de salida
            salida_tmp = self._crear_tmp_docx()

            # 3️⃣ Renderizar documento
            doc = DocxTemplate(str(plantilla_tmp))
            context_dict = contexto.to_dict()

            self._insertar_imagenes(doc, contexto, context_dict)
            self._validar_y_reportar_variables(doc, context_dict)

            doc.render(context_dict)
            doc.save(str(salida_tmp))

            # 4️⃣ TOC
            if agregar_toc:
                self._agregar_tablas_contenido(
                    str(salida_tmp),
                    texto_referencia_toc
                )

            # 5️⃣ Limpieza de tablas
            self._limpiar_filas_vacias(str(salida_tmp))

            # 6️⃣ Subir resultado final a S3
            self._subir_a_s3(salida_tmp, s3_destino)

            self.logger.info(
                f"✅ Documento generado correctamente en S3: {s3_destino}"
            )

            return s3_destino

        finally:
            # 🧹 Limpieza total de temporales
            self._limpiar_tmp(plantilla_tmp, salida_tmp)

    # ------------------------------------------------------------------
    # S3
    # ------------------------------------------------------------------

    def _descargar_desde_s3_tmp(self, s3_key: str) -> Path:
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
        self.s3.download_file(
            Bucket=self.bucket_name,
            Key=s3_key,
            Filename=tmp.name
        )
        self.logger.info(f"📥 Plantilla descargada desde S3: {s3_key}")
        return Path(tmp.name)

    def _subir_a_s3(self, ruta_local: Path, s3_key: str) -> None:
        self.s3.upload_file(
            Filename=str(ruta_local),
            Bucket=self.bucket_name,
            Key=s3_key
        )
        self.logger.info(f"☁ Documento subido a S3: {s3_key}")

    # ------------------------------------------------------------------
    # TEMPORALES
    # ------------------------------------------------------------------

    def _crear_tmp_docx(self) -> Path:
        return Path(
            tempfile.NamedTemporaryFile(delete=False, suffix=".docx").name
        )

    def _limpiar_tmp(self, *paths: Path | None) -> None:
        for p in paths:
            try:
                if p and p.exists():
                    p.unlink()
            except Exception:
                pass

    # ------------------------------------------------------------------
    # VALIDACIÓN
    # ------------------------------------------------------------------

    def _validar_y_reportar_variables(self, doc: DocxTemplate, context_dict: dict) -> None:
        validacion = self.validar_variables_faltantes(doc, context_dict)

        if validacion["faltantes"] or validacion["vacias"]:
            self.logger.warning(
                "⚠ Variables con problemas detectadas en la plantilla:"
            )

            for var in validacion["faltantes"]:
                self.logger.warning(f"   ❌ FALTANTE: {var}")

            for var in validacion["vacias"]:
                self.logger.warning(f"   ⚠ VACÍA: {var}")

    def validar_variables_faltantes(self, doc: DocxTemplate, context_dict: dict) -> dict:
        variables = doc.get_undeclared_template_variables()
        faltantes = []
        vacias = []

        for var in variables:
            if var not in context_dict:
                faltantes.append(var)
            else:
                v = context_dict[var]
                if v in (None, "", [], {}):
                    vacias.append(var)

        return {
            "faltantes": sorted(faltantes),
            "vacias": sorted(vacias),
            "ok": not faltantes and not vacias
        }

    # ------------------------------------------------------------------
    # IMÁGENES
    # ------------------------------------------------------------------

    def _insertar_imagenes(
        self,
        doc: DocxTemplate,
        contexto: ContextoReporte,
        context_dict: dict
    ) -> None:
        for img in contexto.imagenes:
            if not Path(img.path).exists():
                self.logger.warning(f"⚠ Imagen no encontrada: {img.path}")
                continue

            context_dict[img.key] = InlineImage(
                doc,
                img.path,
                width=Cm(img.width)
            )

    # ------------------------------------------------------------------
    # POSTPROCESO
    # ------------------------------------------------------------------

    def _agregar_tablas_contenido(self, docx_path: str, texto: str) -> None:
        self.gestor_toc.agregar_todas_las_toc(
            doc_path=docx_path,
            output_path=docx_path,
            texto_buscar=texto,
            incluir_salto_pagina=True
        )

    def _limpiar_filas_vacias(self, docx_path: str) -> None:
        doc = Document(docx_path)

        for table in doc.tables:
            if table.rows:
                last_row = table.rows[-1]
                if all(not cell.text.strip() for cell in last_row.cells):
                    table._tbl.remove(last_row._tr)

        doc.save(docx_path)
