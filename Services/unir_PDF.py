from pypdf import PdfWriter


def unir_PDFs(pdfs, salida):

    create = PdfWriter()    
# la variable create ya puede generar archivos 

    for pdf in pdfs:
        create.append(pdf)

#este for esta rrecorriendo la lista que tenemos arriba
    create.write(salida)
# creacion del archivo de esta manera todo lo anterior  que estaba en RAM se vuelve real 

    create.close()
#cerramos el objeto buena practica

    print("PDF generado correctamente")














