import sys
from PyQt6.QtWidgets import (
QWidget,
QPushButton,
QLabel,
QVBoxLayout,
QHBoxLayout,
QGridLayout
)
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox

# importamos las librerias necesarias 
from UI.unir_pdf_ventana import ventana_unirpdf
from UI.extraer_paginas_ventana import extraerpaginas_ventana
from UI.desbloquear_pdf_ventana import desbloqueo_ventana
from UI.bloquear_pdf_ventana import bloqueo_ventana
from UI.convertir_jpg_a_pdf_ventana import funcion_convertirJPG
from UI.convertir_word_a_pdf_ventana import convertirword_ventana
from UI.convertir_pdf_a_word_ventana import convertirword_pdf_ventana
from UI.convertir_pdf_a_jpg_ventana import ventana_convertirPDF_a_JPG
from UI.extraer_txt_pdf_digital_ventana import extraer_txt_digital_ventana
from UI.comprimir_pdf_ventana import ventana_compresion_pdf
from UI.estilos import (ESTILO_VENTANA,ESTILO_BOTON,ESTILO_TITULO)
from UI.tarjeta_menuprincipal import tarjeta_categoria


class menu_principal(QWidget):

    def __init__(self):
        super().__init__()

        self.crear_widgets()
        self.crear_layout()
        self.conectar_eventos()

    def mostrar_info(self):

        QMessageBox.information(
                None,
                "Acerca de PDF Tools",
                """
        PDF Tools v1.0

        Desarrollado por:

        Miguel Angel Castiblanco Ramirez

        Aplicación para gestión y conversión de archivos PDF.

        Repositorio:
        github.com/Miguel-t4nqu3/PDFtools""")


    def crear_widgets(self):


        self.setStyleSheet(ESTILO_VENTANA)

        
        self.setWindowTitle("PDF Tools")
        
    

        self.setWindowIcon(
        QIcon("Assets/Icons/pdf_imagen.png"))

        self.setFixedSize(1000,550)
        

        self.titulo = QLabel("PDF Tools")

        self.titulo.setStyleSheet(ESTILO_TITULO)

        self.logo = QLabel()

        self.logo.setPixmap(
            QPixmap("Assets/Icons/pdf_imagen.png").scaled(220,220))

        self.btn_info = QPushButton("💡")
        
        self.btn_info.setStyleSheet(ESTILO_BOTON)
        
        
        self.btn_unir = QPushButton("Unir PDF")
        self.btn_unir.setStyleSheet(ESTILO_BOTON)

        self.btn_extraer_paginas = QPushButton("extraer paginas")
        self.btn_extraer_paginas.setStyleSheet(ESTILO_BOTON)

        self.btn_desbloqueo = QPushButton("Desbloquear PDF")
        self.btn_desbloqueo.setStyleSheet(ESTILO_BOTON)

        self.btn_bloqueo = QPushButton("Bloquear PDF")
        self.btn_bloqueo.setStyleSheet(ESTILO_BOTON)

        self.btn_convertir = QPushButton("Convierte JPG a PDF")
        self.btn_convertir.setStyleSheet(ESTILO_BOTON)

        self.btn_convertir_pdf_a_jpg = QPushButton("Convierte PDF a JPG")
        self.btn_convertir_pdf_a_jpg.setStyleSheet(ESTILO_BOTON)

        self.btn_convertirword = QPushButton("Convertir PDF a Word")
        self.btn_convertirword.setStyleSheet(ESTILO_BOTON)

        self.btn_convertirw_p = QPushButton("Convertir Word a PDF")
        self.btn_convertirw_p.setStyleSheet(ESTILO_BOTON)
      
        self.btn_extraer_txt_digital = QPushButton("Extraer texto de PDF digital")
        self.btn_extraer_txt_digital.setStyleSheet(ESTILO_BOTON)

        self.btn_comprimir_pdf = QPushButton("Comprimir PDF")
        self.btn_comprimir_pdf.setStyleSheet(ESTILO_BOTON)
        


    def crear_layout(self):

        grid = QGridLayout()

        self.layout_izquierdo = QVBoxLayout()

        self.tarjeta_pdf = tarjeta_categoria("📄 Gestión PDF", "Assets/gifs/gestion_pdf.gif")
        self.tarjeta_seguridad = tarjeta_categoria("🔒 Seguridad", "Assets/gifs/seguridad_pdf.gif")
        self.tarjeta_conversion = tarjeta_categoria("🔄 Conversión", "Assets/gifs/convertir_pdf.gif")
        self.tarjeta_texto = tarjeta_categoria("📝 Extracción", "Assets/gifs/texto_gif.gif")


        grid.addWidget(self.tarjeta_pdf,0, 0)

        grid.addWidget(self.tarjeta_seguridad,0, 1)

        grid.addWidget(self.tarjeta_conversion,1, 0)

        grid.addWidget(self.tarjeta_texto,1, 1)

        ### tarjeta pdf

        self.tarjeta_pdf.layout_botones.addWidget(self.btn_unir)

        self.tarjeta_pdf.layout_botones.addWidget(self.btn_extraer_paginas)

        self.tarjeta_pdf.layout_botones.addWidget(self.btn_comprimir_pdf)

        ### seguridad pdf

        self.tarjeta_seguridad.layout_botones.addWidget(self.btn_bloqueo)

        self.tarjeta_seguridad.layout_botones.addWidget(self.btn_desbloqueo)

        #### conversion pdf

        self.tarjeta_conversion.layout_botones.addWidget(self.btn_convertir)

        self.tarjeta_conversion.layout_botones.addWidget(self.btn_convertir_pdf_a_jpg)

        self.tarjeta_conversion.layout_botones.addWidget(self.btn_convertirword)

        self.tarjeta_conversion.layout_botones.addWidget(self.btn_convertirw_p)

        ### extraccion pdf

        self.tarjeta_texto.layout_botones.addWidget(self.btn_extraer_txt_digital)
        
        
        self.layout_izquierdo.addStretch()
            
        self.layout_izquierdo.addWidget(
            self.logo,
            alignment=Qt.AlignmentFlag.AlignCenter
            )
            
        self.layout_izquierdo.addWidget(
            self.titulo,
            alignment=Qt.AlignmentFlag.AlignCenter
            )

        self.layout_izquierdo.addWidget(self.btn_info, 
        alignment=Qt.AlignmentFlag.AlignCenter)
            
        self.layout_izquierdo.addStretch()
        

        layout_principal = QHBoxLayout()

        layout_principal.addLayout(self.layout_izquierdo)
        layout_principal.addLayout(grid)
      

        self.setLayout(layout_principal)

        return self

    def conectar_eventos(self):

        self.btn_unir.clicked.connect(lambda: self.abrir_ventana(ventana_unirpdf))
        self.btn_extraer_paginas.clicked.connect(lambda: self.abrir_ventana(extraerpaginas_ventana))
        self.btn_desbloqueo.clicked.connect(lambda: self.abrir_ventana(desbloqueo_ventana))
        self.btn_bloqueo.clicked.connect(lambda: self.abrir_ventana(bloqueo_ventana))
        self.btn_convertir.clicked.connect(lambda: self.abrir_ventana(funcion_convertirJPG))
        self.btn_convertirword.clicked.connect(lambda: self.abrir_ventana(convertirword_ventana))
        self.btn_convertirw_p.clicked.connect(lambda: self.abrir_ventana(convertirword_pdf_ventana))
        self.btn_convertir_pdf_a_jpg.clicked.connect(lambda: self.abrir_ventana(ventana_convertirPDF_a_JPG))
        self.btn_extraer_txt_digital.clicked.connect(lambda: self.abrir_ventana(extraer_txt_digital_ventana))
        self.btn_comprimir_pdf.clicked.connect(lambda: self.abrir_ventana(ventana_compresion_pdf))
        self.btn_info.clicked.connect(self.mostrar_info)


    def abrir_ventana(self, clase):

        self.ventana_hija = clase()

        self.ventana_hija.show()





    
