import copy
import os, sys

from pathlib import Path
from mouse_keybord_events import MouseEvents


class ManageSettings:    
    def __init__(self,config_path = ".\\settings\\"):        
        self.ini_path        = config_path # sciezka gdzie bedzie zapisany plik z ustawieniami, ciekawe czy tak mozna
        self.ini_file_name   = "_position_settings.ini"
        self.config_file     = ""
        self.__position_list = []
        path_to_save         = Path(config_path)
        path_to_save.mkdir(exist_ok=True)

    def record_settings(self,sequence=0):        
        self.config_file = self.ini_path + str(sequence) + self.ini_file_name
        self.position_list = []  # need to clear the list
        #need to overwrite the settings so if we are missing the ini file it will start recording        
        MouseEvents(sequence, self.position_list)
        if self.position_list:
            self.save_settings(sequence)
            return self.position_list

    def settings_loader(self, load_all_or_one=False, sequence=0):
        #potrzebuje zerowanie listy
        self.config_file   = self.ini_path + str(sequence) + self.ini_file_name               
        if not Path(self.config_file).is_file() : self.record_settings(sequence)        
        return self.load_settings(load_all_or_one, sequence)

    def save_settings(self, sequence = 0):        
        with open(self.config_file, 'w') as file_writter:
            for posXY in self.position_list:
                file_writter.write("{};{};{};{};{};{}\n".format(
                    sequence, posXY[0], posXY[1], posXY[2], posXY[3], posXY[4]))

    def load_settings(self, return_all_or_one = False, return_sequence = 0):        
        sequence_dict = {}
        for files in reversed(os.listdir(self.ini_path)):            
            if(files.endswith(".ini")):                
                with open(self.ini_path + files, 'r') as file_reader:                        
                    for line_XY in file_reader:                        
                        sequence, posX, posY, eventValue, eventType, date_time = line_XY.strip().split(";")
                        XYposList = [posX, posY, eventType,eventValue, date_time]                        
                        if not sequence in sequence_dict:                                                
                            sequence_dict[sequence] = [XYposList]
                        else:                                    
                            sequence_dict[sequence].append(XYposList)                                                                                                 
        if return_all_or_one: return sequence_dict
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
