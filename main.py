from UI.menuPrincipal import menu_principal
import sys
from PyQt6.QtWidgets import (
QApplication
)

# desde aca orquestamos todo el flujo de la aplicacion 
if __name__ == "__main__":

    app = QApplication(sys.argv)
    
    ventana_principal = menu_principal()
    # creamos el objeto y lo utilizamos en esta variable 
    ventana_principal.show()
    # importante el show es para vcer los objetos 

    sys.exit(app.exec())
    