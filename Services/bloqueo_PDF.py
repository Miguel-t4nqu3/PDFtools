from pypdf import PdfWriter # crear
from pypdf import PdfReader
import random
import string


def bloqueo_PDFs(archivo_seleccionado, contraseña, ruta_salida):
    #definimos las variables que nos dara el usuario

    reader = PdfReader(archivo_seleccionado)
    # leemos el archivo que seleccionaremos 
    print(archivo_seleccionado)

    writer = PdfWriter()
    #creamos la variable de creacion

    for pagina in reader.pages:
        writer.add_page(pagina)
    #leemos las paginas iteramos entre ellas y añadimos las paginas

    writer.encrypt(contraseña)
    print(contraseña)
        
    with open(ruta_salida, "wb") as salida:
        writer.write(salida)
        print("PDF generado correctamente")
        print(ruta_salida)

def generar_contraseñas():

    contraseña = ""

    for _ in range(12):
        contraseña += random.choice(
            string.ascii_letters +
            string.digits
        )

    print(contraseña)

    return contraseña