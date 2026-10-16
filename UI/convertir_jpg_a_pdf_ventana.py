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
from pypdf import PdfReader
from Services.convertirpdf_jpg import convertir_jpg_pdf

def funcion_convertirJPG():

    archivos_seleccionados = None

    def seleccion_archivo():

        nonlocal archivos_seleccionados

        archivo, _ = QFileDialog.getOpenFileNames(
        ventana,
        "Selecciona JPG",
        "",
        "Files (*.jpg)")
         
        if not archivo:
            return 

        archivos_seleccionados = archivo

        cantidad = len(archivos_seleccionados)
            
        etiqueta.setText(f"archivos seleccionados: {cantidad}")

    def btn_convertir():

        nonlocal archivos_seleccionados

        if not archivos_seleccionados:

            etiqueta.setText("no has seleccionado ningun archivo para convertir")
            etiqueta.show()
            return

        ruta_salida, _ = QFileDialog.getSaveFileName(
            ventana,
            "Guardar PDF",
            "PDF_convertido.pdf",
            "PDF Files (*.pdf)")
                 
        if not ruta_salida:
            return

        convertir_jpg_pdf(archivos_seleccionados, ruta_salida)
        print("ejecutado satisfactoriamente")

        etiqueta.setText("se ha convertido el archivo correctamente")

        return


    #configuraciones inciales
    ventana = QWidget()

    layout_principal = QVBoxLayout()
    layout_botones = QHBoxLayout()
        

    ventana.setWindowTitle("PDF tools")
    ventana.resize(500 , 300)


    #botones

    titulo = QLabel("Bienvenido a PDF tools", ventana)

    etiqueta = QLabel("selecciona imagen o varias imagenes")

    selecciona = QPushButton("selecciona")

    convertir = QPushButton("convertir")


    #orden de vista 

    layout_principal.addWidget(titulo)
    layout_principal.addWidget(etiqueta)
    layout_botones.addWidget(selecciona)
    layout_botones.addWidget(convertir)

    selecciona.clicked.connect(seleccion_archivo)
    convertir.clicked.connect(btn_convertir)


    ventana.setLayout(layout_principal)
        
    layout_principal.addLayout(layout_botones)
            
    return ventana



