from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QGridLayout,
    QScrollArea,
    QHBoxLayout
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
import pymupdf
import os
from PyQt6.QtGui import QIcon

#from Services.extraer_paginas import dividir_PDFs
from UI.estilos import (ESTILO_BOTON,ESTILO_SELECCIONADO,QUITAR_SELECCION,LETRA_INFO,ESTILO_VENTANA_SUAVE)

def extraerpaginas_ventana():

    


    pdf_path = r"C:\Users\mcastiblancor\Downloads\DEVOLUCION EQUIPO JOSE ANDRES MEDINA MONCADA (1).pdf"
    nombre_archivo = os.path.basename(pdf_path)
    pdf = pymupdf.open(pdf_path)
    pagina = pdf[0]
    pix = pagina.get_pixmap()
    pix.save("pagina1.png")

    print("imagen creada")

    
    ventana = QWidget()
    ventana.setStyleSheet(ESTILO_VENTANA_SUAVE)
    ventana.setWindowIcon(QIcon("Assets/Icons/pdf_imagen.png"))
    ventana.setWindowTitle("PDF Tools")


    layout_principal = QVBoxLayout()
    layout_botones = QHBoxLayout()
    layout_info = QHBoxLayout()

    scroll = QScrollArea()
    scroll.setWidgetResizable(True)

    contenedor = QWidget()

    grid = QGridLayout(contenedor)

    tarjetas = []

##############################################
###################CLASE#####################
#############################################

    class tarjetapagina(QFrame):
    
            def __init__(self, numero):
                super().__init__()
    
                self.numero = numero
                self.seleccionada = False
    
                self.setStyleSheet(QUITAR_SELECCION)  ##########################-----> AQUI PODEMOS EDITAR COMO SE VE ANTES DE LA SELECCION
    
            def mousePressEvent(self, event):
    
                self.seleccionada = not self.seleccionada

                actualizar_contador()
    
                if self.seleccionada:
    
                    self.setStyleSheet(ESTILO_SELECCIONADO)##########################-----> ESTA ES LA VISTA SELECCIONADA
                else:
    
                    self.setStyleSheet(QUITAR_SELECCION) ##########################-----> ESTA ES LA CONTRAPARTE ES DECIR CUANDO NO ESTA SELECCIONADA

#########################################################
##################CREACION TARJETAS######################

    for i in range(10):

        ## creacion de la tarjeta donde ira la imagen 
    
        tarjeta = tarjetapagina(i + 1)
        tarjetas.append(tarjeta)
        tarjeta.setFixedSize(170, 270)


        layout_tarjeta = QVBoxLayout()

        ## imagen que ira en la tarjeta

        imagen = QLabel()
        imagen.setPixmap(QPixmap("pagina1.png"))
        imagen.setScaledContents(True)
        imagen.setMinimumHeight(100)
        imagen.setStyleSheet("""QLabel{
                            border:none;
                            background:white;}""") ##########################-----> ESTILO DE LA IMAGEN

        

        titulo = QLabel(f"Pagina {i+1}")
        titulo.setAlignment(Qt.AlignmentFlag.AlignLeft)
        titulo.setStyleSheet(LETRA_INFO)  ##########################-----> ESTILO DE LA LETRA PAGINA 1

        layout_tarjeta.addWidget(titulo)
        layout_tarjeta.addWidget(imagen)
        layout_tarjeta.setContentsMargins(2,2,2,2)

        tarjeta.setLayout(layout_tarjeta)

        fila = i // 3
        columna = i % 3

        grid.addWidget(tarjeta, fila, columna)

#################################################################
################funciones#######################################

    def seleccionar_todo_funcion():

        for tarjeta in tarjetas:

            tarjeta.seleccionada = True

            tarjeta.setStyleSheet(
            ESTILO_SELECCIONADO
        )

    def quitar_seleccion_funcion():

        for tarjeta in tarjetas:

            tarjeta.seleccionada = False

            tarjeta.setStyleSheet(
            QUITAR_SELECCION
        )

    def actualizar_contador():

        paginas = []

        for tarjeta in tarjetas:

            if tarjeta.seleccionada:

                paginas.append(tarjeta.numero)

        cantidad_paginas.setText(
            f"Seleccion: {len(paginas)} de {len(tarjetas)}"
        )



##############################################################
#############BOTONES########################################

    seleccionar_todo = QPushButton("Selecciona todo")
    seleccionar_todo.setStyleSheet(ESTILO_BOTON)
    

    desselecionar_todo = QPushButton("Quitar seleccion")
    desselecionar_todo.setStyleSheet(ESTILO_BOTON)
    

    generar_pdf = QPushButton("Generar PDF")
    generar_pdf.setStyleSheet(ESTILO_BOTON)

    nombre_archivo = QLabel(nombre_archivo)
    nombre_archivo.setStyleSheet(LETRA_INFO)
    
    cantidad_paginas = QLabel("")
    cantidad_paginas.setStyleSheet(LETRA_INFO)
  

    ##################################################################
    ############### ORDEN###########################################

    layout_info.addWidget(nombre_archivo)
    layout_info.addWidget(cantidad_paginas)

    layout_botones.addWidget(seleccionar_todo)
    layout_botones.addWidget(desselecionar_todo)
    layout_botones.addWidget(generar_pdf)


    ###################################################################
    ################# conexiones #####################################

    seleccionar_todo.clicked.connect(seleccionar_todo_funcion)
    desselecionar_todo.clicked.connect(quitar_seleccion_funcion)




    scroll.setWidget(contenedor)

    layout_principal.addLayout(layout_info)

    layout_principal.addWidget(scroll)

    layout_principal.addLayout(layout_botones)

    ventana.setLayout(layout_principal)

    
    return ventana










