import os
from pypdf import PdfWriter
from pypdf import PdfReader


def unir_PDFs(pdfs, salida):

    create = PdfWriter()    
# la variable create ya puede generar archivos 

    for pdf in pdfs:

        reader = PdfReader(pdf)

        if reader.is_encrypted:

            return False, (
                f"El archivo "
                f"{os.path.basename(pdf)} "
                "está protegido"
            )

        create.append(pdf)
        

#este for esta rrecorriendo la lista que tenemos arriba
    create.write(salida)
# creacion del archivo de esta manera todo lo anterior  que estaba en RAM se vuelve real 

    create.close()
#cerramos el objeto buena practica

    print("PDF generado correctamente")














