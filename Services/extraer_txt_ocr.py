import pymupdf
from pathlib import Path
from docx import Document
from paddleocr import PaddleOCR

class OCRword:

    def __init__(self, pdf, salida):
        self.pdf = pdf
        self.salida = salida
        self.imagenes = []
        self.resultados_ocr = []
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
                texto = linea[1][0]

                if texto.strip():

                    self.resultados_ocr.append(texto)

        return self.resultados_ocr


    def crear_word(self):

        documento = Document()

        for texto in self.resultados_ocr:
            documento.add_paragraph(texto)

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
        self.crear_word()
        self.limpiar_temporales()

    



