# =========================
# ESTILO GENERAL VENTANAS
# =========================

ESTILO_VENTANA = """
QWidget{
    background-color: #06122B;
    color: white;
}
"""

# =========================
# BOTONES PRINCIPALES
# =========================

ESTILO_BOTON = """
QPushButton{
    background-color: #8B5CF6;
    color: white;
    border-radius: 10px;
    padding: 10px;
    font-size: 11pt;
    font-weight: bold;
}

QPushButton:hover{
    background-color: #A855F7;
    border: 2px solid #D8B4FE;
}
"""

# =========================
# TITULO PRINCIPAL
# =========================

ESTILO_TITULO = """
font-size: 40px;
font-weight: bold;
color: #A855F7;
"""

# =========================
# SUBTITULOS
# =========================

ESTILO_SUBTITULO = """
font-size: 18px;
font-weight: bold;
color: #D8B4FE;
"""

# =========================
# TEXTO DESCRIPTIVO
# =========================

ESTILO_DESCRIPCION = """
font-size: 10pt;
color: #9CA3AF;
"""

# =========================
# LABEL DE ESTADO
# =========================

ESTILO_ESTADO = """
font-size: 11pt;
font-weight: bold;
color: #D8B4FE;
"""

# =========================
# BOTON INFORMACION
# =========================

ESTILO_INFO = """
QPushButton{
    background-color: #8B5CF6;
    color: white;
    border-radius: 15px;
    padding: 8px;
    font-size: 16pt;
    font-weight: bold;
}

QPushButton:hover{
    background-color: #A855F7;
    border: 2px solid #D8B4FE;
}
"""

##########################################################################
######### COMO USARLA ###################################################

#ventana.setStyleSheet(ESTILO_VENTANA)

#titulo.setStyleSheet(ESTILO_TITULO)

#descripcion.setStyleSheet(ESTILO_DESCRIPCION)

#btn_unir.setStyleSheet(ESTILO_BOTON)