from paddleocr import PaddleOCR
from Services.extraer_txt_ocr import OCRword

ocr = PaddleOCR(
    use_angle_cls=True,
    lang="es"
)

resultado = OCRword(r"C:\Users\mcastiblancor\Downloads\escaneo_mcastiblancor_2026-11-05-11-00-42.pdf", 
                    r"C:\Users\mcastiblancor\Downloads\escaneo_mcastiblancor_2026-11-05-11-00-42.txt")

