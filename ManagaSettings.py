import copy
import os, sys
from pynput import keyboard
from pathlib import Path

from mouse_keybord_events import MouseKeyboardEvents
from MakeScreenshot import MakeScreenshot

class ManageSettings:    
    def __init__(self,config_path = ".\\settings\\"):        
        self.ini_path        = config_path # sciezka gdzie bedzie zapisany plik z ustawieniami, ciekawe czy tak mozna
        self.ini_file_name   = "_position_settings.ini"
        self.config_file     = ""
        self.position_list   = {}
        path_to_save         = Path(config_path)
        path_to_save.mkdir(exist_ok=True)

    def record_settings(self,sequence=0,stop_key = keyboard.Key['shift']):
        if stop_key != keyboard.Key['shift']:
            try:
                if len(stop_key) > 1: stop_key = keyboard.Key[stop_key]
            except:                
                pass
        self.config_file   = self.ini_path + str(sequence) + self.ini_file_name
        self.position_list = {}  # need to clear the list
        #need to overwrite the settings so if we are missing the ini file it will start recording              
        MouseKeyboardEvents(MakeScreenshot(),sequence, self.position_list,stop_key)
        if self.position_list:
            self.save_settings(sequence)
            # return self.position_list # do I need this?

    def settings_loader(self, load_all_or_one=False, sequence=0):
        #potrzebuje zerowanie listy
        self.config_file   = self.ini_path + str(sequence) + self.ini_file_name               
        if not Path(self.config_file).is_file() : self.record_settings(sequence)        
        return self.load_settings(load_all_or_one, sequence)

    def save_settings(self, sequence = 0):        
        with open(self.config_file, 'w') as file_writter:
            for multipleElements in self.position_list:                
                joined_line      = ";".join(map(str,self.position_list[multipleElements][0]))                
                file_writter.write("{}\n".format(joined_line))

    def load_settings(self, return_all_or_one = False, return_sequence = 0):
        sequence_dict = {}
        for files in reversed(os.listdir(self.ini_path)):
            if(files.endswith(".ini")):
                with open(self.ini_path + files, 'r') as file_reader:
                    for line_XY in file_reader:
                        elements_line = line_XY.strip().split(";")
                        sequence_num  = elements_line[7]                        
                        if not sequence_num in sequence_dict:
                            sequence_dict[sequence_num] = [elements_line] 
                        else:
                            sequence_dict[sequence_num].append(elements_line)
        if return_all_or_one: return sequence_dict        
        return sequence_dict[str(return_sequence)] if str(return_sequence) in sequence_dict else ["missing given sequence for num",return_sequence]