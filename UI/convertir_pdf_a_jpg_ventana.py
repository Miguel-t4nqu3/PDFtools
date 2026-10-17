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
from Services.convertir_pdf_a_jpg import convertir_pdf_a_jpg_backend

def ventana_convertirPDF_a_JPG():
    archivo_seleccionado = None

    def seleccionar_pdf():
        nonlocal archivo_seleccionado

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

        etiqueta_nombre.setText(f"archivo seleccionado: {nombre}")
        etiqueta_nombre.show()

    def convertir_pdf_a_jpg_funcion():
        nonlocal archivo_seleccionado

        if not archivo_seleccionado:
            etiqueta.setText("no has seleccionado ningun archivo para convertir")
            etiqueta.show()
            return

        ruta_salida, _ = QFileDialog.getSaveFileName(
            ventana,
            "Guardar imágenes",
            "",
            "Archivos JPG (*.jpg)"
        )

        if not ruta_salida:
            return

        resultado = convertir_pdf_a_jpg_backend(archivo_seleccionado, ruta_salida)

        if resultado:
            etiqueta.setText("se ha convertido el archivo correctamente")
            etiqueta.show()

        else:
            etiqueta.setText("no se ha podido convertir el archivo correctamente")
            etiqueta.show()

#configuraciones inciales
    ventana = QWidget()

    layout_principal = QVBoxLayout()
    layout_botones = QHBoxLayout()
        

    ventana.setWindowTitle("PDF tools")
    ventana.resize(500 , 300)


    titulo = QLabel("Bienvenido a PDF tools", ventana)

    etiqueta = QLabel("selecciona el archivo pdf que quieres convertir a JPG")

    selecciona = QPushButton("selecciona")
    convertir = QPushButton("convertir")

    etiqueta_nombre = QLabel("")


    #organizacion de la ventana

    layout_principal.addWidget(titulo)
    layout_principal.addWidget(etiqueta)
    layout_principal.addWidget(etiqueta_nombre)


    layout_botones.addWidget(selecciona)
    layout_botones.addWidget(convertir)


    #funciones de los botones

    selecciona.clicked.connect(seleccionar_pdf)
    convertir.clicked.connect(convertir_pdf_a_jpg_funcion)


    ventana.setLayout(layout_principal)
        
    layout_principal.addLayout(layout_botones)
            
    return ventana