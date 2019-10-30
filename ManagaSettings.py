import pyautogui
import pynput

class ManageSettings:    
    def __init__(self, record_or_not):
        self.to_record  = record_or_not
        self.autogui    = pyautogui
        self.checkinput = pynput
        self.ini_path   = "" # sciezka gdzie bedzie zapisany plik z ustawieniami
        if(record_or_not):
            self.position_list = []
    def save_or_load (self):
        if(self.to_record):
            # jeżeli bedzie klik to zapisac miejsce w którym to zostalo to zapisane
            # generalnie bedzie to nadpisywanie, kolejnym krokiem moze byc dodanie nazwy w parametrach by zapisywac pod konkretną aplikację ?
        else:
            # tutaj będzie odbywał się odczyt zawartości pliku, jak czysty string bez żadnych konwersji
        