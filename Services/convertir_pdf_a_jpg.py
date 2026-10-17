import pymupdf
import os




def convertir_pdf_a_jpg_backend(archivo_seleccionado, ruta_salida):
   
   try:
        pdf = pymupdf.open(archivo_seleccionado)

        for numero, pagina in enumerate(pdf):

            imagen = pagina.get_pixmap()

            nombre_base = os.path.splitext(ruta_salida)[0]  # Obtener el nombre base sin extensión

            imagen.save(f"{nombre_base}_{numero + 1}.jpg")
        print("se ha convertido el archivo correctamente")
        return True

   
   except Exception as e:
       print(f"Error al convertir el archivo: {e}")
       return False

   