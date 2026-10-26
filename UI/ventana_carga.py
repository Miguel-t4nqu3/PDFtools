from pydoc import text

from PyQt6.QtWidgets import (
    QDialog,
    QLabel,
    QVBoxLayout
)

from PyQt6.QtGui import QMovie
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from UI.estilos import ESTILO_VENTANA, ESTILO_SUBTITULO
from PyQt6.QtCore import QSize

class ventana_carga(QDialog):

    def __init__(self, mensaje):

        super().__init__()

        self.mensaje = mensaje

        self.crear_widgets_carga()
        self.crear_layouts_carga()

    def crear_widgets_carga(self):

        self.setStyleSheet(ESTILO_VENTANA)
        self.setWindowTitle("PDF Tools Cargando ...")
        self.setWindowIcon(QIcon("Assets/Icons/pdf_imagen.png"))

        self.label_texto = QLabel(self.mensaje)
        self.label_info = QLabel("Estamos preparando todo")
        self.label_info.setStyleSheet(ESTILO_SUBTITULO)
        self.label_texto.setStyleSheet(ESTILO_SUBTITULO)

        self.label_gif = QLabel()
        self.movie = QMovie("Assets/gifs/carga_gif.gif")
        self.movie.setScaledSize(QSize(200, 200))

        self.label_gif.setMovie(self.movie)

        self.movie.start()

    def crear_layouts_carga(self):

        layout = QVBoxLayout()

        layout.addWidget(
        self.label_texto,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
        self.label_gif,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(self.label_info, 
        alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def cambiar_texton(self, texto):

        self.label_info.setText(texto)
