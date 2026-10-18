import os 
import pymupdf



def comprimir_pdf_backend(archivo_seleccionado, ruta_salida):

    ruta_archivo = archivo_seleccionado
    ruta_guardado = ruta_salida

    try:
        peso_original = os.path.getsize(ruta_archivo)

        pdf = pymupdf.open(ruta_archivo)

        pdf.save(ruta_guardado, garbage=4, deflate=True)

        print(f"Archivo comprimido y guardado en: {ruta_guardado}")

        peso_comprimido = os.path.getsize(ruta_guardado)

        bytes_a_mb = peso_original / (1024 * 1024)

        print(f"El peso original del archivo es: {bytes_a_mb:.2f} MB")

        bytes_comprimidos_a_mb = peso_comprimido / (1024 * 1024)

        print(f"El peso comprimido del archivo es: {bytes_comprimidos_a_mb:.2f} MB")

        # calcular el porcentaje de compresión

        porcentaje_compresion = (peso_original - peso_comprimido) / peso_original * 100

        print(f"El porcentaje de compresión es: {porcentaje_compresion:.2f}%")

        return (True, bytes_a_mb, bytes_comprimidos_a_mb, porcentaje_compresion)

    except Exception as e:
        print(f"Error al comprimir el archivo: {e}")
        return (False, 0, 0, 0)

