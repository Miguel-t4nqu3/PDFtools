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
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox
# importamos las librerias necesarias 
from UI.unir_pdf_ventana import ventana_unirpdf
from UI.dividir_pdf_ventana import dividirpdf_ventana
from UI.desbloquear_pdf_ventana import desbloqueo_ventana
from UI.bloquear_pdf_ventana import bloqueo_ventana
from UI.convertir_jpg_a_pdf_ventana import funcion_convertirJPG
from UI.convertir_word_a_pdf_ventana import convertirword_ventana
from UI.convertir_pdf_a_word_ventana import convertirword_pdf_ventana
from UI.convertir_pdf_a_jpg_ventana import ventana_convertirPDF_a_JPG
from UI.extraer_txt_pdf_digital_ventana import extraer_txt_digital_ventana
from UI.comprimir_pdf_ventana import ventana_compresion_pdf
from UI.estilos import (ESTILO_VENTANA,ESTILO_BOTON,ESTILO_DESCRIPCION,ESTILO_ESTADO,
                        ESTILO_INFO,ESTILO_SUBTITULO,ESTILO_TITULO)


ventana_hija = None
ventana_hija2 = None
ventana_hija3 = None
ventana_hija4 = None
ventana_hija5 = None
ventana_hija6 = None
ventana_hija7 = None
ventana_hija8 = None
ventana_hija9 = None
ventana_hija10 = None


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

def abrir_convertirw_p():
    global ventana_hija7

    ventana_hija7 = convertirword_pdf_ventana()

    ventana_hija7.show()

def abrir_convertir_pdf_a_jpg():

    global ventana_hija8

    ventana_hija8 = ventana_convertirPDF_a_JPG()

    ventana_hija8.show()

def abrir_extraer_txt_digital():
    global ventana_hija9

    ventana_hija9 = extraer_txt_digital_ventana()

    ventana_hija9.show()

def abrir_comprimir_pdf():
    global ventana_hija10

    ventana_hija10 = ventana_compresion_pdf()

    ventana_hija10.show()

def mostrar_info():

    QMessageBox.information(
            None,
            "Acerca de PDF Tools",
            """
    PDF Tools v1.0

    Desarrollado por:

    Miguel Angel Castiblanco Ramirez

    Aplicación para gestión y conversión de archivos PDF.

    Repositorio:
    github.com/Miguel-t4nqu3/PDFtools""")


def menu_principal_ventana():

      # modelaje visual

    ventana = QWidget()

    ventana.setStyleSheet(ESTILO_VENTANA)

    
    ventana.setWindowTitle("PDF Tools v1.0")
    ventana.setFixedSize(700, 600)
  

    ventana.setWindowIcon(
    QIcon("Assets/Icons/pdf_imagen.png"))


    layout_derecho = QVBoxLayout()

    layout_izquierdo = QVBoxLayout()

    titulo = QLabel("PDF Tools v1.0")

    titulo.setStyleSheet(ESTILO_TITULO)

    logo = QLabel()

    logo.setPixmap(
        QPixmap("Assets/Icons/pdf_imagen.png").scaled(160,160))

    btn_info = QPushButton("ⓘ")
    btn_info.setStyleSheet(ESTILO_BOTON)
    
    
    btn_unir = QPushButton("Unir PDF")
    btn_unir.setStyleSheet(ESTILO_BOTON)
    btn_unir.setIcon(QIcon("Assets/Icons/unir_imagen.png"))

    btn_dividir = QPushButton("Dividir PDF")
    btn_dividir.setIcon(QIcon("Assets/Icons/dividir_imagen.png"))
    btn_dividir.setStyleSheet(ESTILO_BOTON)

    btn_desbloqueo = QPushButton("Desbloquear PDF")
    btn_desbloqueo.setStyleSheet(ESTILO_BOTON)
    btn_desbloqueo.setIcon(QIcon("Assets/Icons/desbloqueo_imagen.png"))


    btn_bloqueo = QPushButton("Bloquear PDF")
    btn_bloqueo.setStyleSheet(ESTILO_BOTON)
    btn_bloqueo.setIcon(QIcon("Assets/Icons/bloqueo_imagen.png"))

    btn_convertir = QPushButton("Convierte JPG a PDF")
    btn_convertir.setStyleSheet(ESTILO_BOTON)
    btn_convertir.setIcon(QIcon("Assets/Icons/imagen_imagen.png"))


    btn_convertir_pdf_a_jpg = QPushButton("Convierte PDF a JPG")
    btn_convertir_pdf_a_jpg.setStyleSheet(ESTILO_BOTON)
    btn_convertir_pdf_a_jpg.setIcon(QIcon("Assets/Icons/convertir_imagen.png"))

    btn_convertirword = QPushButton("Convertir PDF a Word")
    btn_convertirword.setStyleSheet(ESTILO_BOTON)
    btn_convertirword.setIcon(QIcon("Assets/Icons/word_imagen.png"))

    btn_convertirw_p = QPushButton("Convertir Word a PDF")
    btn_convertirw_p.setStyleSheet(ESTILO_BOTON)
    btn_convertirw_p.setIcon(QIcon("Assets/Icons/convertir_imagen.png"))

    btn_extraer_txt_digital = QPushButton("Extraer texto de PDF digital")
    btn_extraer_txt_digital.setStyleSheet(ESTILO_BOTON)
    btn_extraer_txt_digital.setIcon(QIcon("Assets/Icons/text_imagen.png"))

    btn_comprimir_pdf = QPushButton("Comprimir PDF")
    btn_comprimir_pdf.setStyleSheet(ESTILO_BOTON)
    btn_comprimir_pdf.setIcon(QIcon("Assets/Icons/compresion_imagen.png"))



    btn_unir.clicked.connect(abrir_unir)
    btn_dividir.clicked.connect(abrir_dividir)
    btn_desbloqueo.clicked.connect(abrir_desbloqueo)
    btn_bloqueo.clicked.connect(abrir_bloqueo)
    btn_convertir.clicked.connect(abrir_convertir)
    btn_convertirword.clicked.connect(abrir_convertirw_p)
    btn_convertirw_p.clicked.connect(abrir_convertirword)
    btn_convertir_pdf_a_jpg.clicked.connect(abrir_convertir_pdf_a_jpg)
    btn_extraer_txt_digital.clicked.connect(abrir_extraer_txt_digital)
    btn_comprimir_pdf.clicked.connect(abrir_comprimir_pdf)
    btn_info.clicked.connect(mostrar_info)


    layout_derecho.addWidget(btn_unir)
    layout_derecho.addWidget(btn_dividir)
    layout_derecho.addWidget(btn_desbloqueo)
    layout_derecho.addWidget(btn_bloqueo)
    layout_derecho.addWidget(btn_convertir)
    layout_derecho.addWidget(btn_convertirword)
    layout_derecho.addWidget(btn_convertirw_p)
    layout_derecho.addWidget(btn_convertir_pdf_a_jpg)
    layout_derecho.addWidget(btn_extraer_txt_digital)
    layout_derecho.addWidget(btn_comprimir_pdf)

    
    layout_izquierdo.addStretch()
        
    layout_izquierdo.addWidget(
        logo,
        alignment=Qt.AlignmentFlag.AlignCenter
        )
        
    layout_izquierdo.addWidget(
        titulo,
        alignment=Qt.AlignmentFlag.AlignCenter
        )

    layout_izquierdo.addWidget(btn_info, 
    alignment=Qt.AlignmentFlag.AlignCenter)
        
    layout_izquierdo.addStretch()
    

    layout_principal = QHBoxLayout()

    layout_principal.addLayout(layout_izquierdo)
    layout_principal.addLayout(layout_derecho)

    ventana.setLayout(layout_principal)

    return ventana



    
