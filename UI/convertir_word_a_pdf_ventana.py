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
from Services.convertir_word_a_pdf import convertir_word_a_pdf
from UI.estilos import (ESTILO_BOTON,ESTILO_ESTADO,ESTILO_TITULO,ESTILO_VENTANA)
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox


def convertirword_ventana():

    archivo_seleccionado = None


    def seleccionar_pdf():
        nonlocal archivo_seleccionado

        archivo, _ = QFileDialog.getOpenFileName(
                ventana,
                "Seleccionar archivo Docx",
                "",
                "Archivos docx (*.docx)"
            )
        archivo_seleccionado = archivo

        if not archivo:
            return

        nombre = os.path.basename(
            archivo_seleccionado
        )
        etiqueta_nombre.setText(f"Archivo seleccionado: {nombre}")
        etiqueta_nombre.show()


    def generar_word():
        nonlocal archivo_seleccionado

        if not archivo_seleccionado:
            etiqueta.setText("No has seleccionado ningun archivo para convertir")
            etiqueta.show()
            return

        ruta_salida, _ = QFileDialog.getSaveFileName(
            ventana,
            "Guradae PDF",
            "PDF_convertido.pdf",
            "Archivos PDF (*.pdf)"
        )

        if not ruta_salida:
            return
        
        convertir_word_a_pdf(archivo_seleccionado, ruta_salida)

        print("Ejecutado satisfactoriamente")

        etiqueta.setText("Se ha convertido el archivo correctamente")


    #configuraciones inciales

    layout_principal = QVBoxLayout()
    layout_botones = QHBoxLayout()
        

    ventana = QWidget()
    ventana.setStyleSheet(ESTILO_VENTANA)
    ventana.setWindowTitle("PDF Tools")
    ventana.setFixedSize(500,300)
    ventana.setWindowIcon(QIcon("Assets/Icons/pdf_imagen.png"))

    titulo = QLabel("Bienvenido a PDF tools", ventana)
    titulo.setStyleSheet(ESTILO_TITULO)

    etiqueta = QLabel("Selecciona el archivo word que quieres convertir a pdf")
    etiqueta.setStyleSheet(ESTILO_ESTADO)

    selecciona = QPushButton("selecciona")
    selecciona.setStyleSheet(ESTILO_BOTON)

    convertir = QPushButton("convertir")
    convertir.setStyleSheet(ESTILO_BOTON)

    etiqueta_nombre = QLabel("")
    etiqueta_nombre.setStyleSheet(ESTILO_ESTADO)

    #organizacion

    layout_principal.addWidget(titulo)
    layout_principal.addWidget(etiqueta)
    layout_principal.addWidget(etiqueta_nombre)

    layout_botones.addWidget(selecciona)
    layout_botones.addWidget(convertir)

    #funciones de los botones

    selecciona.clicked.connect(seleccionar_pdf)
    convertir.clicked.connect(generar_word)


    ventana.setLayout(layout_principal)
        
    layout_principal.addLayout(layout_botones)
            
    return ventana




        







