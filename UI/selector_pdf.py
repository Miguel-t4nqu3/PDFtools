from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QGridLayout,
    QScrollArea,
    QHBoxLayout
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
import pymupdf
import os
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFileDialog
import os
from UI.estilos import ESTILO_NORMAL,ESTILO_ACTIVO,ESTILO_VENTANA,ESTILO_SUBTITULO,LETRA_INFO,ESTILO_FALLO,ESTILO_EXITO,ESTILO_ADVERTENCIA
from PyQt6.QtGui import QMovie


class clase_selector_pdf(QFrame):
    
            def __init__(self ):
                super().__init__()

                self.ruta_pdf = ""
                self.archivo_cargado = False
                self.activo = False
                self.gif_label = QLabel()

                
                self.setAcceptDrops(True)
                self.crear_widgets()
                self.crear_layout()
                

            def seleccionar_pdf(self):
                archivo, _ = QFileDialog.getOpenFileName(
                        self,
                        "Seleccionar PDF",
                        "",
                        "PDF (*.pdf)")

                if archivo:
                    self.ruta_pdf = archivo
                    nombre = os.path.basename(archivo)
                    self.mostrar_exito(f"✅ {nombre}")
                    print("funcionando carga ")
                        
                  

            def crear_widgets(self):

                self.setStyleSheet(ESTILO_VENTANA)
                self.setWindowTitle("PDF Tools")
                self.setWindowIcon(QIcon("Assets/Icons/pdf_imagen.png"))

                self.drop_area = QFrame()
                self.drop_area.setStyleSheet(ESTILO_NORMAL)

                self.drop_area.mousePressEvent = self.mousePressEventDrop

                self.label_titulo = QLabel("Arrastra un PDF o seleccionalo")
                self.label_titulo.setStyleSheet(ESTILO_SUBTITULO)
                
                self.label_archivo = QLabel("Ningun archivo seleccionado")
                self.label_archivo.setStyleSheet(ESTILO_SUBTITULO)               

                self.gif_label = QLabel()
                self.movie = QMovie("Assets/Gifs/subir_archivo.gif")
                self.gif_label.setMovie(self.movie)
                self.movie.start()
                   

            def crear_layout(self):

                layout_drop = QVBoxLayout()

                layout_drop.addWidget(
                    self.label_titulo,
                    alignment=Qt.AlignmentFlag.AlignCenter
                )

                layout_drop.addWidget(
                    self.gif_label,
                    alignment=Qt.AlignmentFlag.AlignCenter
                )

                layout_drop.addWidget(
                    self.label_archivo,
                    alignment=Qt.AlignmentFlag.AlignCenter
                )

                self.drop_area.setLayout(layout_drop)

                layout_principal = QVBoxLayout()

                layout_principal.addWidget(self.drop_area)

                self.setLayout(layout_principal)


            def mousePressEventDrop(self, event):

                self.seleccionar_pdf()

                #########################################
                # nos permite arrastrar archivos dentro de la ventana 

            def dragEnterEvent(self, event):

                if event.mimeData().hasUrls():

                    self.drop_area.setStyleSheet(ESTILO_ACTIVO)

                    event.acceptProposedAction()


            def dragEnterEvent(self, event):

                if event.mimeData().hasUrls():

                    self.drop_area.setStyleSheet(
                        ESTILO_ACTIVO
                    )

                    event.acceptProposedAction()

            def mostrar_error(self, mensaje):

                self.label_archivo.setText(mensaje)
                self.label_archivo.setStyleSheet(ESTILO_FALLO)
                print("paso a estilo fallo")

            def mostrar_exito(self, mensaje):

                self.label_archivo.setText(mensaje)
                self.label_archivo.setStyleSheet(ESTILO_EXITO)
                print("paso a estilo exito")
                

            def mostrar_advertencia(self, mensaje):

                self.label_archivo.setText(mensaje)
                self.label_archivo.setStyleSheet(ESTILO_ADVERTENCIA)
                print("paso a estilo advertencia")
                

            def dragLeaveEvent(self, event):

                self.drop_area.setStyleSheet(
                    ESTILO_NORMAL
                )

            def dropEvent(self, event):

                self.drop_area.setStyleSheet(ESTILO_NORMAL)

                archivos = event.mimeData().urls()
                if  len(archivos) > 1:

                    self.mostrar_advertencia("⚠️ solo es posible cargar un documento")
                    return

                archivo = archivos[0].toLocalFile()
                     
                if archivo.lower().endswith(".pdf"):

                    self.ruta_pdf = archivo
                    self.drop_area.setStyleSheet(ESTILO_NORMAL)
                    nombre = os.path.basename(archivo)
                    self.mostrar_exito(f"✅ {nombre}")

                    print(archivo)

                    
                    
                else:
                    self.mostrar_error("❌ No es un archivo PDF")
                    

            

                
                  