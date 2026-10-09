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
from Services.dividir_PDF import dividir_PDFs

def dividirpdf_ventana():


    def seleccionar_pdf():
        global archivo_seleccionado

        archivo_seleccionado, _ = QFileDialog.getOpenFileName(
                ventana,
                "Seleccionar PDF",
                "",
                "PDF Files (*.pdf)"
                )
        nombre = os.path.basename(
            archivo_seleccionado
        )

        etiqueta.setText(f"archivo seleccionado: {nombre}")

    def escoje_rango():

        etiqueta2.setText("escoje el rango")

        desde = QLineEdit()
        hasta = QLineEdit()
        
        desde.setPlaceholderText("Desde")
        hasta.setPlaceholderText("Hasta")

        layout_principal.addWidget(desde)
        layout_principal.addWidget(hasta)


    




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
    
    #desde = QLineEdit()
    #hasta = QLineEdit()

    #desde.setPlaceholderText("Desde")
    #hasta.setPlaceholderText("Hasta")

    

    seleccionar = QPushButton ("seleccionar PDF")
    generar = QPushButton("generar PDF")


    #organizacion 

    layout_principal.addWidget(titulo)
    layout_principal.addWidget(etiqueta)
    layout_principal.addWidget(etiqueta2)

    #layout_principal.addWidget(desde)
    #layout_principal.addWidget(hasta)
    layout_botones.addWidget(seleccionar)
    layout_botones.addWidget(generar)

    # coneccion con funciones

    seleccionar.clicked.connect(seleccionar_pdf)
    seleccionar.clicked.connect(escoje_rango)

    ventana.setLayout(layout_principal)

    layout_principal.addLayout(layout_botones)
    
    return ventana









