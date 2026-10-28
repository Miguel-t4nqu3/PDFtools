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

class descargas(QFrame):

    def __init__(self, mensaje):
        super().__init__()

        self.mensaje = mensaje
        self.ruta_salida = self.ruta_salida


        self.crear_widgets()
        self.crear_layout()
        self.conexion_botones()

    def crear_widgets(self):

        self.setStyleSheet(ESTILO_VENTANA)
        self.setWindowTitle("PDF Tools")
        self.setWindowIcon(QIcon("Assets/Icons/pdf_imagen.png"))

        self.titulo = QLabel("✅ Archivo listo ")
        self.titulo.setStyleSheet(ESTILO_TITULO)

        self.informacion = QLabel(self.mensaje)
        self.informacion.setStyleSheet(ESTILO_SUBTITULO)

        self.descargar_archivo = QPushButton("Guardar Archivo")
        self.descargar_archivo.setStyleSheet(ESTILO_BOTON)

        self.gif_descarga = QLabel()
        self.movie = QMovie("Assets/gifs/descarga_gif.gif")
        self.gif_descarga.setMovie(self.movie)
        self.movie.start()

    def crear_layout(self):

        layout_principal = QVBoxLayout()
        layout_botones = QHBoxLayout()

        layout_principal.addWidget(self.titulo,alignment=Qt.AlignmentFlag.AlignCenter)

        layout_principal.addWidget(self.informacion, alignment=Qt.AlignmentFlag.AlignCenter)

        layout_principal.addWidget(self.gif_descarga, alignment=Qt.AlignmentFlag.AlignCenter)

        layout_principal.addSpacing(20)

        layout_botones.addWidget(self.descargar_archivo, alignment=Qt.AlignmentFlag.AlignCenter)

        layout_principal.addLayout(layout_botones)

        self.setLayout(layout_principal)

    def guardar_archivo(self):

        selfruta_salida, _ = QFileDialog.getSaveFileName(
            self,
            "Guardar PDF",
            "pdf_edited",
            "PDF FILES(*.pdf)"
        )

    def conexion_botones(self):

        self.descargar_archivo.clicked.connect(self.guardar_archivo)












