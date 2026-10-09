from pypdf import PdfWriter # crear
from pypdf import PdfReader
# exportamos la librerias correspondinetes 

def dividir_PDFs(
archivo,
inicio,
fin,
ruta_salida
):

    reader = PdfReader(archivo)

    writer = PdfWriter()

    # Ajuste porque Python empieza en 0
    inicio = inicio - 1
    fin = fin - 1

    # Validaciones
    if inicio > fin:
        print("La página inicial no puede ser mayor que la final")
        return

    if fin >= len(reader.pages):
        print("La página final excede el número de páginas del PDF")
        return

    for pagina in range(inicio, fin + 1):

        writer.add_page(
        reader.pages[pagina]
        )

    with open(ruta_salida, "wb") as salida:
        writer.write(salida)
        print("PDF generado correctamente")

