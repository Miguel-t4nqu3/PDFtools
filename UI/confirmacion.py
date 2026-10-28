from PyQt6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout
 
)
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from UI.estilos import ESTILO_VENTANA,ESTILO_SUBTITULO,ESTILO_BOTON
from PyQt6.QtGui import QMovie


class confirmacion(QFrame):

    def __init__(self, mensaje):
        super().__init__()

        self.mensaje = mensaje

        self.crear_widgets()
        self.crear_layout()
      


    def crear_widgets(self):

        self.setStyleSheet(ESTILO_VENTANA)
        self.setWindowTitle("PDF Tools")
        self.setWindowIcon(QIcon("Assets/Icons/pdf_imagen.png"))

        self.info = QLabel(self.mensaje)
        self.info.setStyleSheet(ESTILO_SUBTITULO)

        self.pregunta = QLabel("¿Deseas continuar?")
        self.pregunta.setStyleSheet(ESTILO_SUBTITULO)

        self.continuar = QPushButton("Continuar")
        self.continuar.setStyleSheet(ESTILO_BOTON)

        self.volver = QPushButton("Volver")
        self.volver.setStyleSheet(ESTILO_BOTON)

        self.gif = QLabel()
        self.movie = QMovie("Assets/gifs/siguiente_confirmacion.gif")
        self.gif.setMovie(self.movie)
        self.movie.start()

    def crear_layout(self):

        layout_principal = QVBoxLayout()
        layout_botones = QHBoxLayout()

        layout_principal.addWidget(self.info,alignment=Qt.AlignmentFlag.AlignCenter)

        layout_principal.addWidget(self.gif,alignment=Qt.AlignmentFlag.AlignCenter)

        layout_principal.addWidget(self.pregunta, alignment=Qt.AlignmentFlag.AlignCenter)

        layout_principal.addSpacing(20)

        layout_botones.addWidget(self.continuar)

        layout_botones.addWidget(self.volver)

        layout_principal.addLayout(layout_botones)
        
        self.setLayout(layout_principal)



    
    

        

