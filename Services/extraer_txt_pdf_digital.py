import pymupdf

def extraer_texto_pdf_backend(archivo_seleccionado, ruta_salida):

    try:
        pdf = pymupdf.open(archivo_seleccionado)

        texto_total = ""

        for pagina in pdf:
            texto_total += pagina.get_text()
                
        print(texto_total)

        with open(ruta_salida, "w", encoding="utf-8") as archivo_salida:
            archivo_salida.write(texto_total)
            print("Texto extraído del PDF correctamente")

        return True
    
        
    except Exception as e:
        print(f"Error al extraer texto del PDF: {e}")
        return False

    



