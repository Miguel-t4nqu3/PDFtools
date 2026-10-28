
from PyQt6.QtWidgets import (
QWidget,
QPushButton,
QLabel,
QVBoxLayout,
QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMovie
from PyQt6.QtWidgets import QLabel
from UI.estilos import ESTILO_BOTON, ESTILO_TARJETA


class tarjeta_categoria(QFrame):

    def __init__(self, titulo, ruta_gif):
        super().__init__()

        self.titulo = titulo
        self.ruta_gif = ruta_gif
        self.desplegado = False


        self.crear_widgets()
        self.crear_layout()
        self.conexion_boton()


    def crear_widgets(self):

        self.setStyleSheet(ESTILO_TARJETA)

        self.setFixedSize(280,250)

        self.gif_label = QLabel()

        self.movie = QMovie(self.ruta_gif)
        print(self.movie.isValid())

        self.gif_label.setMovie(self.movie)

        self.movie.start()

        self.boton_titulo = QPushButton(f"▶ {self.titulo}")

        self.boton_titulo.setStyleSheet(ESTILO_BOTON)

        self.contenedor_botones = QWidget()

        self.layout_botones = QVBoxLayout()

        self.contenedor_botones.setLayout(self.layout_botones)
        self.contenedor_botones.hide()

    def crear_layout(self):

        layout_principal = QVBoxLayout()

        layout_principal.addWidget(self.gif_label,alignment=Qt.AlignmentFlag.AlignCenter)

        layout_principal.addWidget(self.boton_titulo)

        layout_principal.addWidget(self.contenedor_botones)

        self.setLayout(layout_principal)

    def alternar(self):

        self.desplegado = not self.desplegado

        if self.desplegado:

            self.gif_label.hide()

            self.contenedor_botones.show()

            self.boton_titulo.setText(
                f"▼ {self.titulo}"
            )

        else:

            self.gif_label.show()

            self.contenedor_botones.hide()

            self.boton_titulo.setText(
                f"▶ {self.titulo}"
            )


    def conexion_boton(self):

        self.boton_titulo.clicked.connect(self.alternar)

        

    


    






