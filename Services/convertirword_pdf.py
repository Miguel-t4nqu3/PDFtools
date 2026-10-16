from docx2pdf import convert

def convertir_word_a_pdf(archivo_seleccionado, ruta_salida):
    
    try:
        convert(archivo_seleccionado, ruta_salida)
        print("Word convertido a PDF correctamente")
        return True

        
    except Exception as e:
        print(f"Error al convertir Word a PDF: {e}")
        return False
        

    

