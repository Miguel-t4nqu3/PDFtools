# PDF Tools

Aplicación de escritorio desarrollada en Python y PyQt6 para la gestión de archivos PDF.

## Funciones disponibles

- Unir archivos PDF
- Dividir archivos PDF
- Seleccionar ubicación de guardado

## Próximas funciones

- Extraer páginas
- Rotar PDF
- Convertir imágenes a PDF

## Tecnologías utilizadas

- Python
- PyQt6
- PyPDF2

## cambios realizados

Implementación del módulo Dividir PDF.
Selección individual de archivos PDF.
Visualización de la cantidad de páginas del documento.
Entrada de rango mediante QLineEdit.
Validación de campos vacíos.
Validación de entrada numérica.
Validación de página inicial mayor que cero.
Validación de página inicial menor o igual a página final.
Validación de páginas fuera del rango del documento.
Corrección del manejo de cancelación en QFileDialog.
Corrección de pérdida de selección al cancelar la carga de archivos.
Migración de variables de estado de global a nonlocal.
Corrección de generación de PDFs vacíos en el módulo Unir PDF.
Mejora de mensajes de error mostrados al usuario.

## Autor

Miguel Ángel Castiblanco