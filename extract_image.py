from PIL import Image
import pytesseract

def extract_from_image(path):
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    return text
