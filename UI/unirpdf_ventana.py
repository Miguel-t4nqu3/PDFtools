from PyQt6.QtWidgets import (
QWidget,
QPushButton,
QLabel,
QFileDialog,
QVBoxLayout,
QHBoxLayout
)
from Services.unir_PDF import unir_PDFs

def ventana_unirpdf():

    archivos_seleccionados = []
    # de esta manera importamos de una manera mejor 
    ###########################################################################
    ###########################################################################
    def seleccionar_archivos():

        nonlocal archivos_seleccionados

        archivos, _ = QFileDialog.getOpenFileNames(
        ventana,
        "Seleccionar PDF",
        "",
        "PDF Files (*.pdf)"
        )

        if not archivos:
            return

        if len(archivos) < 2:

            etiqueta.setText("debes cargar al menos 2 archivos para poder unir ")
            return


        archivos_seleccionados = archivos
        

        print(archivos_seleccionados)
        etiqueta.setText(f"Archivos cargados: {len(archivos_seleccionados)}" )

    def procesando():

        if not archivos_seleccionados:

            etiqueta.setText(
                "Debes seleccionar al menos 2 PDFs"
            )

            return

        ruta_salida, _ = QFileDialog.getSaveFileName(
            ventana,
            "Guardar PDF",
            "PDF_Unido.pdf",
            "PDF Files (*.pdf)"
        )

        if not ruta_salida:
            return

        unir_PDFs(
            archivos_seleccionados,
            ruta_salida
        )

        etiqueta.setText("PDF listo")

    ###########################################################################
    #CONFIGURACION 

    ventana = QWidget()

    #crea una ventana 

    ventana.setWindowTitle("PDF Tools")
    ventana.resize(500, 300)

    layout_principal = QVBoxLayout()
    layout_botones = QHBoxLayout()

    #############################################################################
    #BOTONES Y TITULOS

    # titulo de la ventana 

    titulo = QLabel(
    "Bienvenido a PDF Tools",
    ventana
    )
    #titulo en pantalla buscar la forma de mejorar 

    selecciona = QPushButton("selecciona¡")
    # boton de unir pdf 

    unir_PDF = QPushButton("Unir PDFs")
    # boton de unir pdf 

    etiqueta = QLabel("elige los archivos que quieres unir :)")

    #############################################################################
    #CONFIGURACION DE BOTONES Y FUNCIONES

    layout_botones.addWidget(selecciona)
    layout_botones.addWidget(unir_PDF)

    layout_principal.addWidget(titulo)
    layout_principal.addWidget(etiqueta)


    # utilizamos layout con el fin de organizar mucho mejor los botones y textos en el entorno 

    selecciona.clicked.connect(seleccionar_archivos)
    # ejecutamos la funcion de unir pdf la cual selecciona y modifica el texto tambien 

    unir_PDF.clicked.connect(procesando)

    layout_principal.addLayout(layout_botones)

    ventana.setLayout(layout_principal)

    return ventana
    # muestra el layout hecho con QVBoxLayout y muestra la ventana creada

   

