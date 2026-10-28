from PyQt6.QtWidgets import (
    QLabel,
    QVBoxLayout,
 
)

from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
import os
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QFileDialog
import os
from UI.estilos import ESTILO_NORMAL,ESTILO_ACTIVO,ESTILO_VENTANA,ESTILO_SUBTITULO,LETRA_INFO,ESTILO_FALLO,ESTILO_EXITO,ESTILO_ADVERTENCIA
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import pyqtSignal


class clase_selector_pdf(QFrame):

            archivos_cargados = pyqtSignal()
    
            def __init__(self, multiples = False ):
                super().__init__()

                self.multiples = multiples
                self.archivos = []
                self.archivo_cargado = False
                self.activo = False
                self.gif_label = QLabel()
                

                
                self.setAcceptDrops(True)
                self.crear_widgets()
                self.crear_layout()
                

            def seleccionar_pdf(self):

                if self.multiples: 

                    archivos, _ = QFileDialog.getOpenFileNames(
                        self,
                        "Seleccionar PDFs",
                        "",
                        "PDF (*.pdf)")

                    if not archivos:
                        return

                    if len(archivos) == 1:

                        self.mostrar_advertencia("⚠️ Debes cargar almenos 2 archivos")
                        return
                        
                    self.archivos = archivos
                    self.mostrar_exito(f"✅ {len(self.archivos)} archivos cargados")
                    self.archivos_cargados.emit()
                    print("funcionando carga ")

                else:
                    archivo, _ = QFileDialog.getOpenFileName(
                            self,
                            "Seleccionar PDF",
                            "",
                            "PDF (*.pdf)")

                    if not archivo:
                        return

                    if archivo:
                        self.archivos = [archivo]
                        nombre = os.path.basename(archivo)
                        self.mostrar_exito(f"✅ {nombre}")
                        self.archivos_cargados.emit()
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

                if self.multiples:

                    self.archivos = []

                    for archivo in archivos:

                        ruta = archivo.toLocalFile()

                        if not ruta.lower().endswith(".pdf"):

                            self.mostrar_error("❌ No es un archivo PDF")
                            return

                        self.archivos.append(ruta)

                    if len(archivos) <2:
                                                                        
                        self.mostrar_advertencia("⚠️ Debes cargar almenos 2 archivos")
                        return

                    self.mostrar_exito(f"✅ {len(self.archivos)} archivos cargados")
                    self.archivos_cargados.emit()

                    print(self.archivos)

                    return
                        
                
                            
                else:

                    archivos = event.mimeData().urls()
                    if  len(archivos) > 1:

                        self.mostrar_advertencia("⚠️ solo es posible cargar un documento")
                        return

                archivo = archivos[0].toLocalFile()
                     
                if archivo.lower().endswith(".pdf"):

                    self.archivos = archivo
                    self.drop_area.setStyleSheet(ESTILO_NORMAL)
                    nombre = os.path.basename(archivo)
                    self.mostrar_exito(f"✅ {nombre}")
                    self.archivos_cargados.emit()

                    print(archivo)      
                    
                else:
                    self.mostrar_error("❌ No es un archivo PDF")


                    

            

                
                  