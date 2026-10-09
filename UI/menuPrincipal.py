import sys
from PyQt6.QtWidgets import (
QApplication,
QWidget,
QPushButton,
QLabel,
QFileDialog,
QVBoxLayout,
QHBoxLayout
)

# importamos las librerias necesarias 
from UI.unirpdf_ventana import ventana_unirpdf
from UI.dividirpdf_ventana import dividirpdf_ventana

ventana_hija = None
ventana_hija2 = None

def abrir_unir():
    global ventana_hija

    ventana_hija = ventana_unirpdf()

    ventana_hija.show()

def abrir_dividir():
    global ventana_hija2

    ventana_hija2 = dividirpdf_ventana()

    ventana_hija2.show()

def menu_principal():

    ventana = QWidget()
    ventana.setWindowTitle("PDF Tools")

    layout = QVBoxLayout()

    btn_unir = QPushButton("Unir PDF")
    btn_dividir = QPushButton("Dividir PDF")

    btn_unir.clicked.connect(abrir_unir)
    btn_dividir.clicked.connect(abrir_dividir)

    layout.addWidget(btn_unir)
    layout.addWidget(btn_dividir)
    ventana.setLayout(layout)

    return ventana



    
