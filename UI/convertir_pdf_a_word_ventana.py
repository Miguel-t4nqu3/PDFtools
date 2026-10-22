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
from Services.convertir_pdf_a_word import convertir_pdf_a_word
from UI.estilos import (ESTILO_BOTON,ESTILO_ESTADO,ESTILO_TITULO,ESTILO_VENTANA)
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox

def convertirword_pdf_ventana():

    archivo_seleccionado = None

    def seleccionar_pdf():
        nonlocal archivo_seleccionado

        archivo, _ = QFileDialog.getOpenFileName(
                ventana,
                "Seleccionar archivo PDF",
                "",
                "Archivos PDF (*.pdf)"
            )
        archivo_seleccionado = archivo

        if not archivo:
            return

        nombre = os.path.basename(
            archivo_seleccionado
        )
        etiqueta_nombre.setText(f"Archivo seleccionado: {nombre}")
        etiqueta_nombre.show()


    def convertir_pdf():
        nonlocal archivo_seleccionado

        if not archivo_seleccionado:
            etiqueta.setText("No has seleccionado ningun archivo para convertir")
            etiqueta.show()
            return

        ruta_salida, _ = QFileDialog.getSaveFileName(
            ventana,
            "Guardar Word",
            "Word_convertido.docx",
            "Archivos Word (*.docx)"
        )

        if not ruta_salida:
            return

        resultado = convertir_pdf_a_word(archivo_seleccionado, ruta_salida)

        if resultado:
            etiqueta.setText("Se ha convertido el archivo correctamente")

        else:
            etiqueta.setText("No se ha podido convertir el archivo correctamente")

            etiqueta.show()

        print("Ejecutado satisfactoriamente")


    layout_principal = QVBoxLayout()
    layout_botones = QHBoxLayout()
        

    ventana = QWidget()
    ventana.setStyleSheet(ESTILO_VENTANA)
    ventana.setWindowTitle("PDF Tools")
    ventana.setFixedSize(500,300)
    ventana.setWindowIcon(QIcon("Assets/Icons/pdf_imagen.png"))

    titulo = QLabel("Bienvenido a PDF tools", ventana)
    titulo.setStyleSheet(ESTILO_TITULO)

    etiqueta = QLabel("selecciona el archivo pdf que quieres convertir a word")
    etiqueta.setStyleSheet(ESTILO_ESTADO)

    etiqueta_nombre = QLabel()
    etiqueta_nombre.setStyleSheet(ESTILO_ESTADO)
    etiqueta_nombre.hide()

    seleccionar = QPushButton("selecciona")
    seleccionar.setStyleSheet(ESTILO_BOTON)

    convertir = QPushButton("convertir")
    convertir.setStyleSheet(ESTILO_BOTON)

    #organizacion


    layout_principal.addWidget(titulo)
    layout_principal.addWidget(etiqueta)
    layout_principal.addWidget(etiqueta_nombre)

    layout_botones.addWidget(seleccionar)
    layout_botones.addWidget(convertir)

    #funciones de los botones

    seleccionar.clicked.connect(seleccionar_pdf)
    convertir.clicked.connect(convertir_pdf)

    ventana.setLayout(layout_principal)
        
    layout_principal.addLayout(layout_botones)
            
    return ventana