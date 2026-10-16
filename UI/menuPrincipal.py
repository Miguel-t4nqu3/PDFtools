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
from UI.convertirjpg_ventana import funcion_convertirJPG
from UI.convertirword_ventana import convertirword_ventana

ventana_hija = None
ventana_hija2 = None
ventana_hija3 = None
ventana_hija4 = None
ventana_hija5 = None
ventana_hija6 = None

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

def abrir_convertir():
    global ventana_hija5

    ventana_hija5 = funcion_convertirJPG()

    ventana_hija5.show()

def abrir_convertirword():
    global ventana_hija6

    ventana_hija6 = convertirword_ventana()

    ventana_hija6.show()


def menu_principal():

    ventana = QWidget()
    ventana.setWindowTitle("PDF Tools")

    layout = QVBoxLayout()

    btn_unir = QPushButton("Unir PDF")
    btn_dividir = QPushButton("Dividir PDF")
    btn_desbloqueo = QPushButton("desbloquear PDF")
    btn_bloqueo = QPushButton("bloquear PDF")
    btn_convertir = QPushButton("convierte JPG->PDF")
    btn_convertirword = QPushButton("convertir PDF a Word")


    btn_unir.clicked.connect(abrir_unir)
    btn_dividir.clicked.connect(abrir_dividir)
    btn_desbloqueo.clicked.connect(abrir_desbloqueo)
    btn_bloqueo.clicked.connect(abrir_bloqueo)
    btn_convertir.clicked.connect(abrir_convertir)
    btn_convertirword.clicked.connect(abrir_convertirword)

    layout.addWidget(btn_unir)
    layout.addWidget(btn_dividir)
    layout.addWidget(btn_desbloqueo)
    layout.addWidget(btn_bloqueo)
    layout.addWidget(btn_convertir)
    layout.addWidget(btn_convertirword)
    ventana.setLayout(layout)

    return ventana



    
