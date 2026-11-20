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
from Services.extraer_txt_ocr import extraer_texto_pdf_backend
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
        
        ###### falta la funcion de extraer texto digital
        
        self.ventana_carga.hide()
        
        self.descarga.show()
        
        self.close()

  
       
    

     



