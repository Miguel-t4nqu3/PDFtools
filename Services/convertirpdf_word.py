from pdf2docx import Converter


def convertir_pdf_a_word(archivo_seleccionado, ruta_salida):

    try:
        cv = Converter(archivo_seleccionado)
        cv.convert(ruta_salida)
        cv.close()
        print("PDF convertido a Word correctamente")

        return True

    except Exception as e:
        print(f"Error al convertir PDF a Word: {e}")
        return False