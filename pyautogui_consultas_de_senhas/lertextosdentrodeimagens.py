import pytesseract
import cv2

# Ler imagem

imagem = cv2.imread("imagem2.png")

caminho = r'C:\Users\rfborges\AppData\Local\Tesseract-OCR'

# Extrair texto da imagem

pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

texto = pytesseract.image_to_string(imagem, lang="por")

print(texto)