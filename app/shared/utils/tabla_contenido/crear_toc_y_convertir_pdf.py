import os
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt
from docx.enum.text import WD_BREAK
import pypandoc
from pathlib import Path


def crear_campo_toc(tipo="contenido"):
    """
    Crea los elementos XML para diferentes tipos de tablas de contenido.

    Parámetros:
    - tipo: 'contenido', 'tablas' o 'figuras'
    """
    fldChar_begin = OxmlElement("w:fldChar")
    fldChar_begin.set(qn("w:fldCharType"), "begin")

    instrText = OxmlElement("w:instrText")
    instrText.set(qn("xml:space"), "preserve")

    if tipo == "contenido":
        instrText.text = r'TOC \o "1-3" \h \z \u'
    elif tipo == "tablas":
        instrText.text = r'TOC \h \z \c "Tabla"'
    elif tipo == "figuras":
        instrText.text = r'TOC \h \z \c "Figura"'

    fldChar_separate = OxmlElement("w:fldChar")
    fldChar_separate.set(qn("w:fldCharType"), "separate")

    updateFields = OxmlElement("w:updateFields")
    updateFields.set(qn("w:val"), "true")

    fldChar_end = OxmlElement("w:fldChar")
    fldChar_end.set(qn("w:fldCharType"), "end")

    return fldChar_begin, instrText, fldChar_separate, updateFields, fldChar_end


def insertar_toc_en_parrafo(paragraph, tipo="contenido"):
    """
    Inserta un campo TOC en un párrafo existente.
    """
    run = paragraph.add_run()
    elementos = crear_campo_toc(tipo)

    r_element = run._r
    for elemento in elementos:
        r_element.append(elemento)


def unir_documentos_word(carpeta_input, archivo_output):
    """
    Une todos los archivos .docx de una carpeta en un solo documento.

    Parámetros:
    - carpeta_input: ruta de la carpeta con los archivos .docx
    - archivo_output: nombre del archivo de salida
    """
    # Obtener todos los archivos .docx de la carpeta
    archivos_docx = sorted(
        [
            f
            for f in os.listdir(carpeta_input)
            if f.endswith(".docx") and not f.startswith("~")
        ]
    )

    if not archivos_docx:
        print(f"❌ No se encontraron archivos .docx en la carpeta: {carpeta_input}")
        return None

    print(f"📄 Archivos encontrados ({len(archivos_docx)}):")
    for i, archivo in enumerate(archivos_docx, 1):
        print(f"   {i}. {archivo}")

    # Crear el documento base con el primer archivo
    doc_unificado = Document(os.path.join(carpeta_input, archivos_docx[0]))
    print(f"\n🔄 Uniendo documentos...")

    # Añadir los demás documentos
    for archivo in archivos_docx[1:]:
        ruta_archivo = os.path.join(carpeta_input, archivo)
        doc_temp = Document(ruta_archivo)

        # Agregar un salto de página antes del siguiente documento
        doc_unificado.add_page_break()

        # Copiar todos los elementos del documento temporal
        for elemento in doc_temp.element.body:
            doc_unificado.element.body.append(elemento)

        print(f"   ✓ Añadido: {archivo}")

    # Guardar el documento unificado
    doc_unificado.save(archivo_output)
    print(f"\n✅ Documentos unidos en: {archivo_output}")

    return archivo_output


def agregar_todas_las_toc(doc_path, output_path, texto_buscar="PRESENTACIÓN"):
    """
    Inserta tabla de contenido, índice de tablas e índice de figuras
    justo antes de un texto específico en el documento.

    Parámetros:
    - doc_path: ruta del documento de entrada
    - output_path: ruta del documento de salida
    - texto_buscar: texto antes del cual insertar las TOC (default: "PRESENTACIÓN")
    """
    doc = Document(doc_path)

    # Buscar el párrafo que contiene el texto
    posicion = None
    for i, paragraph in enumerate(doc.paragraphs):
        if texto_buscar.upper() in paragraph.text.upper():
            posicion = i
            print(f"✓ Encontrado '{texto_buscar}' en el párrafo {i}")
            break

    # Si no se encuentra el texto, insertar al inicio
    if posicion is None:
        posicion = 0
        print(
            f"⚠️  No se encontró '{texto_buscar}'. Insertando al inicio del documento."
        )

    # Tabla de Contenido
    titulo_contenido = doc.paragraphs[posicion].insert_paragraph_before(
        "Tabla de Contenido"
    )
    titulo_contenido.style = "Heading 1"

    parrafo_toc = doc.paragraphs[posicion + 1].insert_paragraph_before()
    insertar_toc_en_parrafo(parrafo_toc, "contenido")

    doc.paragraphs[posicion + 2].insert_paragraph_before()

    # Índice de Tablas
    titulo_tablas = doc.paragraphs[posicion + 3].insert_paragraph_before(
        "Índice de Tablas"
    )
    titulo_tablas.style = "Heading 1"

    parrafo_tablas = doc.paragraphs[posicion + 4].insert_paragraph_before()
    insertar_toc_en_parrafo(parrafo_tablas, "tablas")

    doc.paragraphs[posicion + 5].insert_paragraph_before()

    # Índice de Figuras
    titulo_figuras = doc.paragraphs[posicion + 6].insert_paragraph_before(
        "Índice de Figuras"
    )
    titulo_figuras.style = "Heading 1"

    parrafo_figuras = doc.paragraphs[posicion + 7].insert_paragraph_before()
    insertar_toc_en_parrafo(parrafo_figuras, "figuras")

    doc.paragraphs[posicion + 8].insert_paragraph_before()

    # Salto de página antes de PRESENTACIÓN para que quede en la siguiente página
    salto_pagina = doc.paragraphs[posicion + 9].insert_paragraph_before()
    run_salto = salto_pagina.add_run()
    run_salto.add_break(WD_BREAK.PAGE)

    doc.save(output_path)
    print(
        f"✅ Todas las tablas de contenido insertadas antes de '{texto_buscar}' en: {output_path}"
    )
    print("\n⚠️  IMPORTANTE:")
    print("   - Abre el documento en Word")
    print("   - Haz clic derecho en cada tabla y selecciona 'Actualizar campos'")
    print("   - O presiona Ctrl+A y luego F9 para actualizar todos los campos")


def convertir_a_pdf(input_docx, output_pdf):
    """
    Convierte un archivo Word (.docx) a PDF conservando estilos.
    """
    try:
        output = pypandoc.convert_file(
            input_docx, "pdf", outputfile=output_pdf, extra_args=["--standalone"]
        )
        print(f"✅ Archivo convertido a PDF: {output_pdf}")
    except Exception as e:
        print(f"⚠️  Error al convertir a PDF: {e}")
        print("   Puedes abrir el archivo .docx en Word y guardar como PDF manualmente")


if __name__ == "__main__":
    # Configuración
    carpeta_documentos = "output"  # Carpeta con los archivos .docx a unir
    archivo_unificado = "documento_unificado.docx"
    archivo_final = "documento_final_con_toc.docx"
    archivo_pdf = "documento_final.pdf"

    # Texto antes del cual insertar las TOC
    TEXTO_REFERENCIA = "PRESENTACIÓN"

    print("=" * 60)
    print("UNIR DOCUMENTOS WORD Y CREAR TABLA DE CONTENIDO")
    print("=" * 60)

    # Paso 1: Unir todos los documentos
    resultado = unir_documentos_word(carpeta_documentos, archivo_unificado)

    if resultado:
        # Paso 2: Agregar tablas de contenido antes del texto especificado
        print("\n" + "=" * 60)
        print(
            f"📑 Buscando '{TEXTO_REFERENCIA}' e insertando tablas de contenido antes..."
        )
        agregar_todas_las_toc(archivo_unificado, archivo_final, TEXTO_REFERENCIA)

        # Paso 3: Convertir a PDF (opcional)
        print("\n" + "=" * 60)
        respuesta = input("\n¿Deseas convertir a PDF? (s/n): ").lower()
        if respuesta == "s":
            convertir_a_pdf(archivo_final, archivo_pdf)

        print("\n" + "=" * 60)
        print("📋 RESUMEN:")
        print(f"   • Documento unificado: {archivo_unificado}")
        print(f"   • Documento con TOC: {archivo_final}")
        print(f"   • TOC insertadas antes de: '{TEXTO_REFERENCIA}'")
        if respuesta == "s":
            print(f"   • Documento PDF: {archivo_pdf}")

        print("\n📝 PRÓXIMOS PASOS:")
        print("   1. Abre el documento en Microsoft Word")
        print("   2. Presiona Ctrl+A para seleccionar todo")
        print("   3. Presiona F9 para actualizar todos los campos")
        print("   4. Guarda el documento")
        print("=" * 60)
