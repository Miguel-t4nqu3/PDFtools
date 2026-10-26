import sys
from PyQt6.QtWidgets import (
QWidget,
QPushButton,
QLabel,
QVBoxLayout,
QHBoxLayout,
QFrame
)
from PyQt6.QtGui import QIcon
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QTimer
from UI.estilos import ESTILO_BOTON, ESTILO_SUBTITULO, ESTILO_TARJETA


class tarjeta_categoria(QFrame):

    def __init__(self, titulo):
        super().__init__()

        self.titulo = titulo
        self.desplegado = False
        self.crear_widgets()
        self.crear_layout()
        self.conexion_boton()


    def crear_widgets(self):

        self.setStyleSheet(ESTILO_TARJETA)

        self.setFixedSize(280,250)

        self.boton_titulo = QPushButton(f"▶ {self.titulo}")

        self.boton_titulo.setStyleSheet(ESTILO_BOTON)

        self.contenedor_botones = QWidget()

        self.layout_botones = QVBoxLayout()

        self.contenedor_botones.setLayout(self.layout_botones)
        self.contenedor_botones.hide()

    def crear_layout(self):

        layout_principal = QVBoxLayout()

        layout_principal.addWidget(self.boton_titulo)

        layout_principal.addWidget(self.contenedor_botones)

        layout_principal.addLayout(self.layout_botones)

        self.setLayout(layout_principal)

    def alternar(self):

        self.desplegado = not self.desplegado

        if self.desplegado:

            self.contenedor_botones.hide()

            self.boton_titulo.setText(f"▶ {self.titulo}")    

        else:


            self.boton_titulo.setText(f"▼ {self.titulo}")

            self.contenedor_botones.show()


    def conexion_boton(self):

        self.boton_titulo.clicked.connect(self.alternar)

        

    


    






