from PIL import Image

def convertir_jpg_pdf(archivos_seleccionados, ruta_salida):

    imagenes = []

    for archivo in archivos_seleccionados:
        imagen = Image.open(archivo)
        imagen = imagen.convert("RGB")
        imagenes.append(imagen)

        print("se ha realizado de manera correcta")

    imagenes[0].save(
        ruta_salida,
        save_all=True,
        append_images=imagenes[1:]
        )

