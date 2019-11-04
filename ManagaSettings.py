import pyautogui
import pynput
import PIL
from mouse_keybord_events import MouseEvents


class ManageSettings:    
    def __init__(self, record_or_not = False):
        self.to_record     = record_or_not
        self.autogui       = pyautogui
        self.checkinput    = pynput
        self.ini_path      = ".\\position_settings.ini" # sciezka gdzie bedzie zapisany plik z ustawieniami, ciekawe czy tak mozna        
        self.position_list = []
    def save_or_load (self):
            if(self.to_record):            
                MouseEvents(self.position_list)
                if self.position_list: self.save_settings()                               
            else:
                self.load_settings()                
    def save_settings(self):
        with open(self.ini_path, 'w') as file_writter:
            for posXY in self.position_list:
                file_writter.write("{};{}\n".format(posXY[0], posXY[1]))
    def load_settings(self):
        with open(self.ini_path, 'r') as file_reader:
            for line_XY in file_reader:
                posX, posY = line_XY.split(";")
                self.position_list.append( tuple ( (posX,posY) ) )
    @property
    def position_list(self):
        return self.__position_list
    @position_list.setter
    def position_list(self, position_list):
        self.__position_list = position_list

    
# simple unit test
# testKlas = ManageSettings()
# testKlas.save_or_load()
# for posXY in testKlas.position_list:
#     print("pozycja x->{} y->{}".format(posXY[0],posXY[1]), end="")
    


