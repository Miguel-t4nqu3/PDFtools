import pymupdf
from pathlib import Path
from docx import Document
from paddleocr import PaddleOCR

class OCRword:

    def __init__(self, pdf, salida):
        self.pdf = pdf
        self.salida = salida
        self.imagenes = []
        self.lineas_detectadas = []
        self.bloques = []   
        self.path = Path("temp")
        self.path.mkdir(exist_ok=True)
        self.ocr = PaddleOCR(
        use_angle_cls=True,
        lang="es")
        

    def pdf_a_imagenes(self):

        with pymupdf.open(self.pdf) as pdf:
            for numero_pagina, pagina in enumerate(pdf):
                pix = pagina.get_pixmap(matrix=pymupdf.Matrix(2,2))
                nombre_imagen = self.path / f"pagina_{numero_pagina + 1}.png"
                pix.save(str(nombre_imagen))
                self.imagenes.append(nombre_imagen)

            return self.imagenes     

    def ejecutar_ocr(self):

        for imagen in self.imagenes:

            resultado = self.ocr.ocr(
                str(imagen),
                cls=True
            )

            for linea in resultado[0]:

                caja = linea[0]
                texto = linea[1][0]

                x = caja[0][0]
                y = caja[0][1]

                ancho = caja[1][0] - caja[0][0]
                alto = caja[2][1] - caja[0][1]

                self.lineas_detectadas.append({
                    "texto": texto,
                    "x": x,
                    "y": y,
                    "ancho": ancho,
                    "alto": alto
                })

            print(f"Total lineas detectadas: {len(self.lineas_detectadas)}")

            for linea in self.lineas_detectadas[:10]:
                print(linea)
        

    def analizar_bloques(self):

        lineas_ordenadas = sorted(
            self.lineas_detectadas,
            key=lambda x: x["y"]
        )

        filas = []

        fila_actual = []

        y_referencia = None

        for linea in lineas_ordenadas:

            y = linea["y"]

            if y_referencia is None:

                fila_actual.append(linea)
                y_referencia = y
            else:

                distancia = abs(y - y_referencia)

                if distancia < 15:
                    
                    fila_actual.append(linea)
                else:

                    filas.append(fila_actual)
                    fila_actual = [linea]
                    y_referencia = y

        if fila_actual:
            filas.append(fila_actual)


            for fila in filas:

                fila.sort(key=lambda x: x["x"])

                texto_fila = " | ".join(item["texto"] for item in fila)

                alto_max = max(item["alto"] for item in fila)

                # FILTRO DE BASURA OCR
                if len(texto_fila.split()) > 8:

                    palabras_malas = sum(1
                        for palabra in texto_fila.split()
                        if len(palabra) >10)

                    if palabras_malas > 5:
                        continue

                    # CLASIFICACION DEL BLOQUE

                if (len(fila) == 1
                    and texto_fila
                    and len(texto_fila)< 50
                    and(texto_fila.isupper()
                        or texto_fila.startswith("1. ")
                        or texto_fila.startswith("2. ")
                        or texto_fila.startswith("3. ")
                        or texto_fila.startswith("4. "))):
                        tipo = "titulo"

                elif len(fila) >= 3:
                        tipo = "tabla"

                elif len(fila) == 2:
                    tipo = "formulario"

                else:
                    tipo = "parrafo"

                bloque = {"texto": texto_fila,
                                     "columnas": len(fila),
                                     "celdas": [item["texto"]for item in fila],
                                     "alto": alto_max,
                                     "tipo": tipo}
                if "ouensn" in texto_fila:
                    continue
                    

                self.bloques.append(bloque)

                print(
                    bloque["tipo"],
                    bloque["texto"])

                


            print("\nBLOQUES DETECTADOS\n")

            for bloque in self.bloques:
                print(bloque)

    def crear_word(self):

        documento = Document()

        tabla_actual = None

        print(
            "TABLA:",
            len(bloque["celdas"]),
            bloque["texto"]
                            )

        for bloque in self.bloques:
            if bloque["tipo"] == "titulo":
                tabla_actual = None

                documento.add_heading(bloque["texto"], level = 2)

            elif bloque["tipo"] == "formulario":
                tabla_actual = None
                tabla = documento.add_table(rows=1,
                    cols=len(bloque["celdas"]))

                tabla.style = "Table Grid"

                fila = tabla.rows[0].cells

                for i, celda in enumerate(
                    bloque["celdas"]
                ):
                    fila[i].text = celda.strip()

            elif bloque["tipo"] == "tabla":

                if tabla_actual is None:

                    tabla_actual = documento.add_table(
                        rows=0,
                        cols=len(bloque["celdas"])
                    )

                    tabla_actual.style = "Table Grid"

                fila = tabla_actual.add_row().cells

                for i, celda in enumerate(
                    bloque["celdas"]
                ):

                    fila[i].text = celda.strip()

            else:
                tabla_actual = None

                documento.add_paragraph(bloque["texto"])

        documento.save(self.salida)

        

        print(f"✅ El archivo Word se ha creado correctamente en: {self.salida}")

        return True

    def limpiar_temporales(self):

        for imagen in self.imagenes:
            if imagen.exists():
                imagen.unlink()


    def procesar(self):
        self.pdf_a_imagenes()
        self.ejecutar_ocr()
        self.analizar_bloques()
        self.crear_word()
        self.limpiar_temporales()

    



