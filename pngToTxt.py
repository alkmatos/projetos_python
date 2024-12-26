import pytesseract
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
image_path="C:\\Users\\Andre.matos\\Desktop\\DOCS\\ordem_layout_medallia.png"
img=Image.open(image_path)
text=pytesseract.image_to_string(img)
print(text)