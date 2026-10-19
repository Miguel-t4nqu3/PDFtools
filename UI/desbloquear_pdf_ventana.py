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
from Services.desbloquear_pdf import desbloquear_PDFs
from UI.estilos import (ESTILO_BOTON,ESTILO_DESCRIPCION,ESTILO_ESTADO,ESTILO_INFO,ESTILO_SUBTITULO,ESTILO_TITULO,ESTILO_VENTANA)
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox

def desbloqueo_ventana():

    archivo_seleccionado = None 

    def seleccionar_pdf():

        nonlocal archivo_seleccionado
    
        archivo, _ = QFileDialog.getOpenFileName(
            ventana,
            "Seleccionar PDF",
            "",
            "PDF Files (*.pdf)")
    
        if not archivo:
                return
    
        archivo_seleccionado = archivo
        reader = PdfReader(archivo_seleccionado)


        if not reader.is_encrypted:
            etiqueta2.setText("El archivo seleccionado no tiene contraseña")
            etiqueta2.show()

            desbloquear.hide()
            password.hide()

            return

        etiqueta2.setText("has seleccionado un archivo con contraseña correctamente")
            
        nombre = os.path.basename(
            archivo_seleccionado)
    
        etiqueta.setText(f"archivo seleccionado: {nombre}")

        etiqueta2.show()
        desbloquear.show()
        password.show()

    def generar_desbloqueo():

        nonlocal archivo_seleccionado

        contraseña = password.text()
        print(contraseña)

        reader = PdfReader(archivo_seleccionado)

        if reader.decrypt(contraseña) == 0:
            print("contraseña incorrecta")
            etiqueta2.setText("la contraseña no es correcta, vuelve a intentar")
            return

        ruta_salida, _ = QFileDialog.getSaveFileName(
        ventana,
        "Guardar PDF",
        "PDF_desbloqueado.pdf",
        "PDF Files (*.pdf)")
         
        if not ruta_salida:
            return

        desbloquear_PDFs(archivo_seleccionado, contraseña, ruta_salida)

        etiqueta2.setText("PDF desbloqueado")

    #creamos una ventana 

    ventana = QWidget()
    ventana.setStyleSheet(ESTILO_VENTANA)
    ventana.setWindowTitle("PDF Tools")
    ventana.setFixedSize(500,300)
    ventana.setWindowIcon(QIcon("Assets/Icons/pdf_imagen.png"))

    layout_principal = QVBoxLayout()
    layout_botones = QHBoxLayout()
    

    titulo = QLabel("Bienvenido pdf tools",ventana)
    titulo.setStyleSheet(ESTILO_TITULO)
    
    etiqueta = QLabel("selcciona pdf a desbloquear")
    etiqueta.setStyleSheet(ESTILO_ESTADO)

    etiqueta2 = QLabel("ingresa la contraseña del documento")
    etiqueta2.setStyleSheet(ESTILO_ESTADO)

    seleccionar = QPushButton("selecciona")
    seleccionar.setStyleSheet(ESTILO_BOTON)

    desbloquear = QPushButton("desbloquear")
    desbloquear.setStyleSheet(ESTILO_BOTON)

    password = QLineEdit()
    password.setStyleSheet(ESTILO_BOTON)

    password.setPlaceholderText("ingresar la contraseña")
    

    password.setEchoMode(QLineEdit.EchoMode.Password)

    
    #organizacion

    layout_principal.addWidget(titulo)
    layout_principal.addWidget(etiqueta)
    layout_principal.addWidget(etiqueta2)
    layout_principal.addWidget(password)

    layout_botones.addWidget(seleccionar)
    layout_botones.addWidget(desbloquear)

    etiqueta2.hide()
    desbloquear.hide()
    password.hide()


    #conexion con funciones

    seleccionar.clicked.connect(seleccionar_pdf)
    desbloquear.clicked.connect(generar_desbloqueo)

    ventana.setLayout(layout_principal)
    
    layout_principal.addLayout(layout_botones)
        
    return ventana

