from PyQt6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QFileDialog
 
)
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from UI.estilos import ESTILO_VENTANA,ESTILO_SUBTITULO,ESTILO_BOTON,ESTILO_TITULO
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import QSize
import os

class descargas(QFrame):

    def __init__(self, mensaje):
        super().__init__()

        self.mensaje = mensaje
        self.ruta_salida = None


        self.crear_widgets()
        self.crear_layout()
        self.conexion_botones()

    def crear_widgets(self):

        self.setStyleSheet(ESTILO_VENTANA)
        self.setWindowTitle("PDF Tools")
        self.setWindowIcon(QIcon("Assets/Icons/pdf_imagen.png"))
        self.setFixedSize(700,500)

        self.titulo = QLabel("✅ Archivo listo ")
        self.titulo.setStyleSheet(ESTILO_TITULO)

        self.informacion = QLabel(self.mensaje)
        self.informacion.setStyleSheet(ESTILO_SUBTITULO)

        self.gif_descarga = QLabel()
        self.movie = QMovie("Assets/gifs/descarga_gif.gif")
        self.movie.setScaledSize(QSize(300, 300))
        self.gif_descarga.setMovie(self.movie)
        self.movie.start()

        self.abrir_carpeta = QPushButton("Abrir archivo")
        self.abrir_carpeta.setStyleSheet(ESTILO_BOTON)

        self.crear_otro_pdf = QPushButton("Crear otro archivo")
        self.crear_otro_pdf.setStyleSheet(ESTILO_BOTON)


    def crear_layout(self):

        layout_principal = QVBoxLayout()
        layout_botones = QHBoxLayout()

        layout_principal.addWidget(self.titulo,alignment=Qt.AlignmentFlag.AlignCenter)

        layout_principal.addWidget(self.informacion, alignment=Qt.AlignmentFlag.AlignCenter)

        layout_principal.addWidget(self.gif_descarga, alignment=Qt.AlignmentFlag.AlignCenter)

        layout_principal.addSpacing(20)

        layout_botones.addWidget(self.abrir_carpeta)
        layout_botones.addWidget(self.crear_otro_pdf)

        layout_principal.addLayout(layout_botones)


        self.setLayout(layout_principal)

    def guardar_archivo(self):

        self.ruta_salida, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar PDF",
            "pdf_edited",
            "PDF FILES(*.pdf)"
        )
        return self.ruta_salida

    def conexion_botones(self):

        self.abrir_carpeta.clicked.connect(self.abrir_archivo)
        self.crear_otro_pdf.clicked.connect(self.volver_menu_principal)


    def abrir_archivo(self):

        if self.ruta_salida:

            os.startfile(self.ruta_salida)
            
    def volver_menu_principal(self):

        self.close()














