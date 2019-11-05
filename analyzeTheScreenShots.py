#this will be for the futre as i'm not sure i'll need this and proper config will take to much time
from PIL import Image
import pytesseract

class ReadText:
    def __init__(self):
        self.__path_to_teseract = pytesseract.pytesseract.tesseract_cmd = r"F:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    def read_to_string(self, image_file):
        return pytesseract.image_to_string(Image.open(image_file), lang='pol')
    def read_to_data(self, image_file):
        return pytesseract.image_to_data(Image.open(image_file))
        
test = ReadText()
print(test.read_to_string("F:\\python\\automateWork\\images\\images.jpg"))
# print(test.read_to_data("F:\\python\\automateWork\\images\\0_0_0_200_200_screenshot.tiff"))
