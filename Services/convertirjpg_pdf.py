import pymupdf


def convertir_pdf_a_jpg(archivo_seleccionado, ruta_salida):
   
   try:
        pdf = pymupdf.open(archivo_seleccionado)

        for numero, pagina in enumerate(pdf):

            imagen = pagina.get_pixmap()

            imagen.save(f"{ruta_salida}/pagina_{numero + 1}.jpg")
        print("se ha convertido el archivo correctamente")
        return True

   
   except Exception as e:
       print(f"Error al convertir el archivo: {e}")
       return False

   