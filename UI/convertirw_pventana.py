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
from Services.convertirpdf_word import convertir_pdf_a_word


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
            etiqueta.setText("no has seleccionado ningun archivo para convertir")
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
            etiqueta.setText("se ha convertido el archivo correctamente")

        else:
            etiqueta.setText("no se ha podido convertir el archivo correctamente")

            etiqueta.show()

        print("ejecutado satisfactoriamente")

    #configuraciones inciales
    ventana = QWidget()

    layout_principal = QVBoxLayout()
    layout_botones = QHBoxLayout()
        

    ventana.setWindowTitle("PDF tools")
    ventana.resize(500 , 300)

    titulo = QLabel("Bienvenido a PDF tools", ventana)

    etiqueta = QLabel("selecciona el archivo pdf que quieres convertir a word")

    etiqueta_nombre = QLabel()
    etiqueta_nombre.hide()

    seleccionar = QPushButton("selecciona")

    convertir = QPushButton("convertir")

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