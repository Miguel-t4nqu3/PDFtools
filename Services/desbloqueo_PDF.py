from pypdf import PdfWriter # crear
from pypdf import PdfReader


def desbloquear_PDFs(archivo_seleccionado, contraseña, ruta_salida):
    #definimos las variables que nos dara el usuario

    reader = PdfReader(archivo_seleccionado)
    # leemos el archivo que seleccionaremos 

    reader.decrypt(contraseña)
    # colocamos la contraseña
    print(contraseña)

    writer = PdfWriter()
    #creamos la variable de creacion

    for pagina in reader.pages:
        writer.add_page(pagina)
    #leemos las paginas iteramos entre ellas y añadimos las paginas
        
    with open(ruta_salida, "wb") as salida:
        writer.write(salida)
        print("PDF generado correctamente")

    


    

