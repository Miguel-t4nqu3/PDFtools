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
from UI.desbloqueo_ventana import desbloqueo_ventana
from UI.bloqueo_ventana import bloqueo_ventana

ventana_hija = None
ventana_hija2 = None
ventana_hija3 = None
ventana_hija4 = None

def abrir_unir():
    global ventana_hija

    ventana_hija = ventana_unirpdf()

    ventana_hija.show()

def abrir_dividir():
    global ventana_hija2

    ventana_hija2 = dividirpdf_ventana()

    ventana_hija2.show()

def abrir_desbloqueo():
    global ventana_hija3

    ventana_hija3 = desbloqueo_ventana()

    ventana_hija3.show()

def abrir_bloqueo():
    global ventana_hija4

    ventana_hija4 = bloqueo_ventana()

    ventana_hija4.show()


def menu_principal():

    ventana = QWidget()
    ventana.setWindowTitle("PDF Tools")

    layout = QVBoxLayout()

    btn_unir = QPushButton("Unir PDF")
    btn_dividir = QPushButton("Dividir PDF")
    btn_desbloqueo = QPushButton("desbloquear PDF")
    btn_bloqueo = QPushButton("bloquear PDF")

    btn_unir.clicked.connect(abrir_unir)
    btn_dividir.clicked.connect(abrir_dividir)
    btn_desbloqueo.clicked.connect(abrir_desbloqueo)
    btn_bloqueo.clicked.connect(abrir_bloqueo)

    layout.addWidget(btn_unir)
    layout.addWidget(btn_dividir)
    layout.addWidget(btn_desbloqueo)
    layout.addWidget(btn_bloqueo)
    ventana.setLayout(layout)

    return ventana



    
