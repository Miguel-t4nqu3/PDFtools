from PyQt6.QtWidgets import (
QWidget,
QPushButton,
QLabel,
QFileDialog,
QVBoxLayout,
QHBoxLayout,
QLineEdit
)
import os
from pypdf import PdfWriter # crear
from pypdf import PdfReader
from Services.dividir_PDF import dividir_PDFs

def dividirpdf_ventana():
    


    def seleccionar_pdf():
        global archivo_seleccionado
        

        archivo, _ = QFileDialog.getOpenFileName(
                ventana,
                "Seleccionar PDF",
                "",
                "PDF Files (*.pdf)"
                )

        if not archivo:
            return

        archivo_seleccionado = archivo
        
        nombre = os.path.basename(
            archivo_seleccionado
        )

        etiqueta.setText(f"archivo seleccionado: {nombre}")

        escoje_rango()

    def escoje_rango():
        global cantidad_paginas

        etiqueta2.setText("escoje el rango")

        desde.show()
        hasta.show()
        generar.show()

        reader = PdfReader(archivo_seleccionado)
        if not archivo_seleccionado:
            return

        cantidad_paginas = len(reader.pages)

        etiqueta3.setText(f"el archivo contiene: {cantidad_paginas} paginas")

    def generar_pdf():
        

        texto_incio =  desde.text()
        texto_fin = hasta.text()

        if not texto_incio or not texto_fin:
            etiqueta2.setText("debes ingresar un rango valido")
            return

        if not texto_incio.isdigit():
            etiqueta2.setText("el rango de incio debe ser numerico")
            return

        if not texto_fin.isdigit():
            etiqueta2.setText("el rango final debe ser numerico ")
            return

        inicio = int(desde.text())
        fin = int(hasta.text())

        print (inicio)
        print(fin)

        if inicio <= 0:
            etiqueta2.setText("el primer valor tiene que ser mayor a 0 ")
            return

        if inicio > fin:
            etiqueta2.setText("La página inicial no puede ser mayor que la final")
            return
                
        if fin >= cantidad_paginas:
            etiqueta2.setText(f"el pdf solo contiene {cantidad_paginas} de paginas ")
            return

        #################################################################
        #conexion con el backend
        

        ruta_salida, _ = QFileDialog.getSaveFileName(
            ventana,
            "Guardar PDF",
            "PDF_Dividido.pdf",
            "PDF Files (*.pdf)"
                )

        if not ruta_salida:
            return
        if not archivo_seleccionado:

            etiqueta2.setText("debes seleccionar un PDF  ")

            return

        print("PDF:", archivo_seleccionado)
        print("Salida:", ruta_salida)


        dividir_PDFs(archivo_seleccionado,inicio, fin, ruta_salida)
        print("archivo guardado OKI ")

        

    ventana = QWidget()
    
    #creamos una ventana 
    
    ventana.setWindowTitle("PDF Tools")
    ventana.resize(500, 300)
    
    layout_principal = QVBoxLayout()
    layout_botones = QHBoxLayout()

    # definimos los botones y dialogos 

    titulo = QLabel(
        "Bienvenido pdf tools",
        ventana
        )

    etiqueta = QLabel("selecciona el PDF que quieres dividir¡")

    etiqueta2 = QLabel("")
    etiqueta3 = QLabel("")
    
    desde = QLineEdit()
    hasta = QLineEdit()

    desde.setPlaceholderText("Desde")
    hasta.setPlaceholderText("Hasta")

    

    seleccionar = QPushButton ("seleccionar PDF")
    generar = QPushButton("dividir PDF")


    #organizacion 

    layout_principal.addWidget(titulo)
    layout_principal.addWidget(etiqueta)
    layout_principal.addWidget(etiqueta2)
    layout_principal.addWidget(etiqueta3)

    layout_principal.addWidget(desde)
    layout_principal.addWidget(hasta)
    layout_botones.addWidget(seleccionar)
    layout_botones.addWidget(generar)

    desde.hide()
    hasta.hide()
    generar.hide()


    # coneccion con funciones

    seleccionar.clicked.connect(seleccionar_pdf)
    generar.clicked.connect(generar_pdf)

    ventana.setLayout(layout_principal)

    layout_principal.addLayout(layout_botones)
    
    return ventana










