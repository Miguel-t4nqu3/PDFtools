from ast import Return

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
from Services.bloquear_pdf import bloqueo_PDFs
from Services.bloquear_pdf import generar_contraseñas


def bloqueo_ventana():

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


        if reader.is_encrypted == 1:
            etiqueta2.setText("el archivo ya se encuentra bloqueado con una contraseña")
            etiqueta2.show()
            bloquear.hide()
            password.hide()
            genera.hide()
            etiqueta_contraseña.hide()
            return

        etiqueta2.setText("archivo seleccionado correctamente")
        etiqueta2.show()

        nombre = os.path.basename(archivo_seleccionado)
    
        etiqueta.setText(f"archivo seleccionado: {nombre}")

        etiqueta2.show()
        bloquear.show()
        password.show()
        genera.show()

    def generar_bloqueo():

        nonlocal archivo_seleccionado

        contraseña = password.text()
        print(contraseña)

        if not contraseña:
            etiqueta2.setText("no has ingresado ningun caracter en el campo contraseña")
            return
        

        ruta_salida, _ = QFileDialog.getSaveFileName(
        ventana,
        "Guardar PDF",
        "PDF_Desbloqueado.pdf",
        "PDF Files (*.pdf)")
         
        if not ruta_salida:
            return

        bloqueo_PDFs(archivo_seleccionado, contraseña, ruta_salida)

    def btn_genera_contraseñas():

        contraseña = generar_contraseñas()

        print(contraseña)

        etiqueta_contraseña.setText(f"contraseña generada correctamente guardala: {contraseña} ")

        password.setText(contraseña)

        etiqueta_contraseña.show()




    #creamos una ventana 

    ventana = QWidget()

    layout_principal = QVBoxLayout()
    layout_botones = QHBoxLayout()
    

    ventana.setWindowTitle("PDF tools")
    ventana.resize(500 , 300)

    titulo = QLabel(
            "Bienvenido pdf tools",
            ventana
            )
    
    etiqueta = QLabel("selcciona pdf a bloquear")

    etiqueta2 = QLabel("ingresa la contraseña que le colocaras al documento")

    seleccionar = QPushButton("selecciona")
    bloquear = QPushButton("bloquear")

    password = QLineEdit()

    genera = QPushButton("genera contraseña aleatoria")

    etiqueta_contraseña = QLabel("")

    password.setPlaceholderText("ingresar")

    password.setEchoMode(QLineEdit.EchoMode.Password)

    
    #organizacion

    layout_principal.addWidget(titulo)
    layout_principal.addWidget(etiqueta)
    layout_principal.addWidget(etiqueta2)
    layout_principal.addWidget(password)
    layout_principal.addWidget(genera)
    layout_principal.addWidget(etiqueta_contraseña)

    layout_botones.addWidget(seleccionar)
    layout_botones.addWidget(bloquear)

    etiqueta2.hide()
    bloquear.hide()
    password.hide()
    genera.hide()
    etiqueta_contraseña.hide()


    #conexion con funciones

    seleccionar.clicked.connect(seleccionar_pdf)
    bloquear.clicked.connect(generar_bloqueo)
    genera.clicked.connect(btn_genera_contraseñas)


    ventana.setLayout(layout_principal)
    
    layout_principal.addLayout(layout_botones)
        
    return ventana