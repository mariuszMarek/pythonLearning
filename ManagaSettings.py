import pyautogui
import pynput
import PIL
from mouse_keybord_events import MouseEvents


class ManageSettings:    
    def __init__(self, record_or_not):
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
        with open(self.ini_path, 'w') as file_settings:
            for posXY in self.position_list:
                file_settings.write("{};{}".fo  rmat( posXY[0], posXY[1] ))        
        pass
    def load_settings(self):
        #tutaj trzeba odczytac utawienia
        pass
    @property
    def position_list(self):
        return self.position_list
    def make_screensots(self):    
        # tutaj zrobic screenshoty do tego ? to juz moze oddzielna klasa/funkcja
        pass
        # for position_
        # PIL.ImageGrab.grab
    
#simple unit test
# testKlas = ManageSettings(True)
# testKlas.save_or_load()
# for posXY in testKlas.position_list:
#     print("pozycja x->{} y->{}".format(posXY[0],posXY[1]))
    


