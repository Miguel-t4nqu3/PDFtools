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
from UI.estilos import (ESTILO_BOTON,ESTILO_ESTADO,ESTILO_TITULO,ESTILO_VENTANA)
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox


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

        etiqueta.setText(f"Archivo seleccionado: {nombre}")

    def extraer_texto_digital():
        nonlocal archivo_seleccionado

        if not archivo_seleccionado:
            etiqueta.setText("No has seleccionado ningun archivo para extraer el texto digital")
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
            etiqueta.setText("Se ha extraido el texto digital correctamente")
            etiqueta.show()



    ventana = QWidget()
    ventana.setStyleSheet(ESTILO_VENTANA)
    ventana.setWindowTitle("PDF Tools")
    ventana.setFixedSize(500,300)
    ventana.setWindowIcon(QIcon("Assets/Icons/pdf_imagen.png"))
        
    layout_principal = QVBoxLayout()
    layout_botones = QHBoxLayout()

    # definimos los botones y dialogos 

    titulo = QLabel("Bienvenido pdf tools",ventana)
    titulo.setStyleSheet(ESTILO_TITULO)

    etiqueta = QLabel("Selecciona el PDF del que quieres extraer el texto digital")
    etiqueta.setStyleSheet(ESTILO_ESTADO)

    etiqueta_descripcion = QLabel("Esta funcion solo permite extraer texto digital, no texto escaneado")
    etiqueta_descripcion.setStyleSheet(ESTILO_ESTADO)

    seleccionar = QPushButton ("Seleccionar PDF")
    seleccionar.setStyleSheet(ESTILO_BOTON)

    generar = QPushButton("Extraer texto digital")
    generar.setStyleSheet(ESTILO_BOTON)

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
