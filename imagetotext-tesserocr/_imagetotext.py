from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\nen9ten10\\AppData\\Local\\Tesseract-OCR\\tesseract'

i = Image.open('india.png')

text = pytesseract.image_to_string(i)

print (text)