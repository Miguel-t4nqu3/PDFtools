from PyQt6.QtWidgets import (
QWidget,
QPushButton,
QLabel,
QFileDialog,
QVBoxLayout,
QHBoxLayout
)
from Services.unir_PDF import unir_PDFs
from UI.estilos import (ESTILO_BOTON,ESTILO_SUBTITULO,ESTILO_TITULO,ESTILO_VENTANA)
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox
from UI.selector_pdf import clase_selector_pdf
from UI.confirmacion import confirmacion
from Services.unir_PDF import unir_PDFs



class ventana_unirpdf(QWidget):

    def __init__(self):
        super().__init__()

        self.selector_pdf = clase_selector_pdf(multiples= True)

        self.confirmacion = confirmacion("")
        self.confirmacion.hide()

        self.crear_layout()
        self.conexion_botones()


    def crear_layout(self):

        layout = QVBoxLayout()
        self.setStyleSheet(ESTILO_VENTANA)  
        self.setWindowTitle("PDF Tools")
        self.setFixedSize(700,500)
        self.setWindowIcon(QIcon("Assets/Icons/pdf_imagen.png"))

        layout.addWidget(self.selector_pdf)
        layout.addWidget(self.confirmacion)

        self.setLayout(layout)

        self.selector_pdf.archivos_cargados.connect(self.ventana_confirmacion)

    def ventana_confirmacion(self):

        if not self.selector_pdf.archivos:
            return

        cantidad = len(self.selector_pdf.archivos)

        self.confirmacion.info.setText(f"✅ {cantidad} archivos cargados")

        self.selector_pdf.hide()
        self.confirmacion.show()

    def volver_selector(self):

        self.confirmacion.hide()

        self.selector_pdf.show()

    def conexion_botones(self):

        self.confirmacion.volver.clicked.connect(self.volver_selector)

        self.confirmacion.continuar.clicked.connect(self.procesamiento_pdf)

    def procesamiento_pdf(self):

        self.procesar = unir_PDFs(self.selector_pdf.archivos, ruta_salida)







    





    










      





    

    

   

