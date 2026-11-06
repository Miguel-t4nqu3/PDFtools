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
from UI.descarga_pdf import descargas
from UI.estilos import (ESTILO_BOTON,ESTILO_ESTADO,ESTILO_TITULO,ESTILO_VENTANA)
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QMessageBox
from UI.selector_pdf import clase_selector_pdf
from UI.ventana_carga import ventana_carga
from UI.selector_pdf import clase_selector_pdf
from UI.confirmacion import confirmacion
from UI.descarga_pdf import descargas
import os



class extraer_txt_digital_ventana(QWidget):

    def __init__(self):
        super().__init__()

        self.selector_pdf = clase_selector_pdf(multiples= False)
        self.confirmacion = confirmacion("")
        self.confirmacion.hide()
        self.crear_layout()
        self.conexion_botones()

    def crear_layout(self):


        layout = QVBoxLayout()
        self.setStyleSheet(ESTILO_VENTANA)
        self.setWindowTitle("PDF Tools")
        self.setFixedSize(700, 500)
        self.setWindowIcon(QIcon("Assets/Icons/pdf_imagen.png"))

        layout.addWidget(self.selector_pdf)
        layout.addWidget(self.confirmacion)
        
        self.setLayout(layout)
        
        self.selector_pdf.archivos_cargados.connect(self.ventana_confirmacion)
        
    def ventana_confirmacion(self):
        
        if not self.selector_pdf.archivos:
            return
        
        nombre_archivo = os.path.basename(self.selector_pdf.archivos)
        
        
        self.confirmacion.info.setText(f"✅archivo cargado: {nombre_archivo}")
        
        self.selector_pdf.hide()
        self.confirmacion.show()
        
    def volver_selector(self):
        
        self.confirmacion.hide()
        
        self.selector_pdf.show()
        
    def conexion_botones(self):
        
        self.confirmacion.volver.clicked.connect(self.volver_selector)
        
        self.confirmacion.continuar.clicked.connect(self.procesamiento_pdf)
        
    def procesamiento_pdf(self):
        
        self.descarga = descargas(
        "se ha extraido el texto correctameente")
        
        ruta_salida = self.descarga.guardar_archivo()
        
        if not ruta_salida:
            return
        
        self.confirmacion.hide()
        
        self.ventana_carga = ventana_carga(
            "Procesando archivos...")
        
        self.ventana_carga.show()
        
        self.ruta_salida = ruta_salida
        
        QTimer.singleShot(
                2000,
                self.finalizar_proceso)
        
                
        
    def finalizar_proceso(self):
        

        
        self.ventana_carga.hide()
        
        self.descarga.show()
        
        self.close()




        
       
    

     




# def extraer_txt_digital_ventana():

#     archivo_seleccionado = None

#     def seleccionar_pdf():
#         nonlocal archivo_seleccionado

#         archivo, _ = QFileDialog.getOpenFileName(
#                 ventana,
#                 "Seleccionar PDF",
#                 "",
#                 "PDF Files (*.pdf)"
#                 )

#         if not archivo:
#             return

#         archivo_seleccionado = archivo
        
#         nombre = os.path.basename(
#             archivo_seleccionado
#         )

#         etiqueta.setText(f"Archivo seleccionado: {nombre}")

#     def extraer_texto_digital():
#         nonlocal archivo_seleccionado

#         if not archivo_seleccionado:
#             etiqueta.setText("No has seleccionado ningun archivo para extraer el texto digital")
#             etiqueta.show()
#             return

#         ruta_salida, _ = QFileDialog.getSaveFileName(
#             ventana,
#             "Guardar texto",
#             "texto_extraido.txt",
#             "Archivos de texto (*.txt)"
#         )

#         if not ruta_salida:
#             return

        
#         resultado = extraer_texto_pdf_backend(archivo_seleccionado, ruta_salida)

#         if resultado:
#             etiqueta.setText("Se ha extraido el texto digital correctamente")
#             etiqueta.show()



#     ventana = QWidget()
#     ventana.setStyleSheet(ESTILO_VENTANA)
#     ventana.setWindowTitle("PDF Tools")
#     ventana.setFixedSize(500,300)
#     ventana.setWindowIcon(QIcon("Assets/Icons/pdf_imagen.png"))
        
#     layout_principal = QVBoxLayout()
#     layout_botones = QHBoxLayout()

#     definimos los botones y dialogos 

#     titulo = QLabel("Bienvenido pdf tools",ventana)
#     titulo.setStyleSheet(ESTILO_TITULO)

#     etiqueta = QLabel("Selecciona el PDF del que quieres extraer el texto digital")
#     etiqueta.setStyleSheet(ESTILO_ESTADO)

#     etiqueta_descripcion = QLabel("Esta funcion solo permite extraer texto digital, no texto escaneado")
#     etiqueta_descripcion.setStyleSheet(ESTILO_ESTADO)

#     seleccionar = QPushButton ("Seleccionar PDF")
#     seleccionar.setStyleSheet(ESTILO_BOTON)

#     generar = QPushButton("Extraer texto digital")
#     generar.setStyleSheet(ESTILO_BOTON)

#     organizacion

#     layout_principal.addWidget(titulo)
#     layout_principal.addWidget(etiqueta)
#     layout_principal.addWidget(etiqueta_descripcion)

#     layout_botones.addWidget(seleccionar)
#     layout_botones.addWidget(generar)

#     coneccion con funciones

#     seleccionar.clicked.connect(seleccionar_pdf)
#     generar.clicked.connect(extraer_texto_digital)


#     ventana.setLayout(layout_principal)

#     layout_principal.addLayout(layout_botones)
    
#     return ventana
