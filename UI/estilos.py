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
color: #E6D5FF;
"""

# =========================
# ESTILO NO SELECCIONADO
# =========================

QUITAR_SELECCION = """
QFrame{border:2px solid #cccccc; 
background:white;}"""

# =========================
# ESTILO SELECCIONADO
# =========================

ESTILO_SELECCIONADO = """
QFrame{background:white;
border:3px solid #7B68EE;
border-radius:10px;}"""

# =========================
# ESTILO LETRA INFO
# =========================

LETRA_INFO = """border:none;
font-size:14px;
font-weight:bold;
color:#E6D5FF;
padding-left:5px;"""

# =========================
# LABEL DE ESTADO
# =========================

ESTILO_ESTADO = """
font-size: 11pt;
font-weight: bold;
color: #D8B4FE;
"""
# =========================
# ESTILO VENTANA SUAVE 
# =========================

ESTILO_VENTANA_SUAVE = """
background:#020F3B;
"""
# =========================
# ESTILO NORMAL
# =========================

ESTILO_NORMAL = """
QFrame{
    background-color: #09173F;
    border: 3px dashed #8A7BFF;
    border-radius: 15px;
}
"""
# =========================
# ESTILO ACTIVO 
# =========================

ESTILO_ACTIVO = """
QFrame{
    background-color: #162561;
    border: 3px solid #B388FF;
    border-radius: 15px;
}
"""
# =========================
# ESTILO EXITO
# =========================
ESTILO_EXITO = """
color: #57D38C;
font-size: 16px;
font-weight: bold;
"""


# =========================
# ESTILO FALLO
# =========================
ESTILO_FALLO = """
color: #FF6B6B;
font-size: 16px;
font-weight: bold;
"""

# =========================
# ESTILO ADVERTENCIA
# =========================
ESTILO_ADVERTENCIA = """
color: #FFC857;
font-size: 16px;
font-weight: bold;
"""


##########################################################################
######### COMO USARLA ###################################################

#ventana.setStyleSheet(ESTILO_VENTANA)

#titulo.setStyleSheet(ESTILO_TITULO)

#descripcion.setStyleSheet(ESTILO_DESCRIPCION)

#btn_unir.setStyleSheet(ESTILO_BOTON)