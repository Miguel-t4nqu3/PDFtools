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
from Services.extraer_txt_pdf_digital import extraer_texto_pdf_backend


def extraer_txt_digital_ventana():

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

        etiqueta.setText(f"archivo seleccionado: {nombre}")

    def extraer_texto_digital():
        nonlocal archivo_seleccionado

        if not archivo_seleccionado:
            etiqueta.setText("no has seleccionado ningun archivo para extraer el texto digital")
            etiqueta.show()
            return

        ruta_salida, _ = QFileDialog.getSaveFileName(
            ventana,
            "Guardar texto",
            "texto_extraido.txt",
            "Archivos de texto (*.txt)"
        )

        if not ruta_salida:
            return

        
        resultado = extraer_texto_pdf_backend(archivo_seleccionado, ruta_salida)

        if resultado:
            etiqueta.setText("se ha extraido el texto digital correctamente")
            etiqueta.show()



    ventana = QWidget()
        
        #creamos una ventana 
        
    ventana.setWindowTitle("PDF Tools")
    ventana.resize(500, 300)
        
    layout_principal = QVBoxLayout()
    layout_botones = QHBoxLayout()

    # definimos los botones y dialogos 

    titulo = QLabel("Bienvenido pdf tools",ventana)

    etiqueta = QLabel("selecciona el PDF del que quieres extraer el texto digital¡")

    etiqueta_descripcion = QLabel("esta funciono solo permite extraer texto digital, no texto escaneado")


    seleccionar = QPushButton ("seleccionar PDF")
    generar = QPushButton("extraer texto digital")

    #organizacion

    layout_principal.addWidget(titulo)
    layout_principal.addWidget(etiqueta)
    layout_principal.addWidget(etiqueta_descripcion)

    layout_botones.addWidget(seleccionar)
    layout_botones.addWidget(generar)

    # coneccion con funciones

    seleccionar.clicked.connect(seleccionar_pdf)
    generar.clicked.connect(extraer_texto_digital)


    ventana.setLayout(layout_principal)

    layout_principal.addLayout(layout_botones)
    
    return ventana
