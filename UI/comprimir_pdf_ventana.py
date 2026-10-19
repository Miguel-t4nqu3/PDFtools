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
from Services.comprimir_pdf import comprimir_pdf_backend
from UI.estilos import (ESTILO_BOTON,ESTILO_DESCRIPCION,ESTILO_ESTADO,ESTILO_INFO,ESTILO_SUBTITULO,ESTILO_TITULO,ESTILO_VENTANA)
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox


def ventana_compresion_pdf():

        archivo_seleccionado = None

        def seleccion_archivo():

            nonlocal archivo_seleccionado

            archivo, _ = QFileDialog.getOpenFileName(
            ventana,
            "Selecciona PDF",
            "",
            "Files (*.pdf)")
             
            if not archivo:
                return 

            archivo_seleccionado = archivo

            etiqueta_nombre.setText(f"Archivo seleccionado: {os.path.basename(archivo_seleccionado)}")
            etiqueta_nombre.show()

        def btn_comprimir():
             
            nonlocal archivo_seleccionado

            if not archivo_seleccionado:

                etiqueta.setText("no has seleccionado ningun archivo para comprimir")
                etiqueta.show()
                return

            ruta_salida, _ = QFileDialog.getSaveFileName(
                ventana,
                "Guardar PDF",
                "PDF_comprimido.pdf",
                "PDF Files (*.pdf)")
                     
            if not ruta_salida:
                return

            etiqueta.setText("Comprimiendo archivo, por favor espera...")
            etiqueta.repaint()  # Actualiza la etiqueta antes de la compresión

            resultado = comprimir_pdf_backend(archivo_seleccionado, ruta_salida)

            if resultado[0]:
                etiqueta.setText(f"Archivo comprimido correctamente\nPeso original: {resultado[1]:.2f} MB\nPeso comprimido: {resultado[2]:.2f} MB\nPorcentaje de compresión: {resultado[3]:.2f}%")
            else:
                etiqueta.setText("Error al comprimir el archivo")

    #configuraciones inciales

        layout_principal = QVBoxLayout()
        layout_botones = QHBoxLayout()
            

        ventana = QWidget()
        ventana.setStyleSheet(ESTILO_VENTANA)
        ventana.setWindowTitle("PDF Tools")
        ventana.setFixedSize(500,300)
        ventana.setWindowIcon(QIcon("Assets/Icons/pdf_imagen.png"))


        #botones

        titulo = QLabel("Bienvenido a PDF tools", ventana)
        titulo.setStyleSheet(ESTILO_TITULO)

        etiqueta = QLabel("selecciona un archivo PDF para comprimir")
        etiqueta.setStyleSheet(ESTILO_ESTADO)

        etiqueta_nombre = QLabel("")
        etiqueta_nombre.setStyleSheet(ESTILO_ESTADO)
        etiqueta_nombre.hide()

        selecciona = QPushButton("selecciona")
        selecciona.setStyleSheet(ESTILO_BOTON)

        comprimir = QPushButton("comprimir")
        comprimir.setStyleSheet(ESTILO_BOTON)

        # organizacion de botones

        layout_principal.addWidget(titulo)
        layout_principal.addWidget(etiqueta)
        layout_principal.addWidget(etiqueta_nombre)

        layout_botones.addWidget(selecciona)
        layout_botones.addWidget(comprimir)

        #funciones de botones

        selecciona.clicked.connect(seleccion_archivo)
        comprimir.clicked.connect(btn_comprimir)

        ventana.setLayout(layout_principal)
                
        layout_principal.addLayout(layout_botones)
                    
        return ventana
