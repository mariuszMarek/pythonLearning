import os
import copy

from pathlib import Path
from mouse_keybord_events import MouseEvents

class ManageSettings:    
    def __init__(self, record_or_not = False,config_path = ".\\settings\\"):
        self.to_record       = record_or_not
        self.ini_path        = config_path # sciezka gdzie bedzie zapisany plik z ustawieniami, ciekawe czy tak mozna
        self.ini_file_name   = "_position_settings.ini"
        self.config_file     = ""
        self.__position_list = []
        path_to_save         = Path(config_path)
        path_to_save.mkdir(exist_ok=True)

    def save_or_load (self, sequence = 0):
            if(self.to_record):            
                MouseEvents(self.position_list)
                if self.position_list: self.save_settings(sequence)                                           
            return self.load_settings(sequence)

    def save_settings(self, sequence = 0):
        self.config_file = self.ini_path + str(sequence) + self.ini_file_name
        with open(self.config_file, 'w') as file_writter:
            for posXY in self.position_list:
                file_writter.write("{};{};{}\n".format(sequence, posXY[0], posXY[1]))

    def load_settings(self, return_sequence = 0):
        with open(self.config_file, 'r') as file_reader:
            sequence_dict = {}            
            for line_XY in file_reader:
                sequence, posX, posY = line_XY.strip().split(";")
                XYposList = [posX, posY]                
                if not sequence in sequence_dict:                    
                    sequence_dict[sequence] = [XYposList]
                else:        
                    sequence_dict[sequence].append(XYposList)                                                                                         
            return sequence_dict[str(return_sequence)] if str(return_sequence) in sequence_dict else ["missing given sequence for num",return_sequence]
    @property
    def position_list(self):
        return self.__position_list
    @position_list.setter
    def position_list(self, position_list):
        self.__position_list = position_list

    

# testKlas = ManageSettings(False)
# for posXY in testKlas.save_or_load(0):
#     print(posXY)
