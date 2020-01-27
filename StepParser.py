from pynput.mouse    import Button, Controller
from pynput.keyboard import Key, Controller

class Parser:
    def __init__(self, list_of_steps = []):
        self.list_of_steps_raw      = list_of_steps
        self.list_of_steps_formated = {}
        self.list_of_steps_keyboard = []
        self.list_of_steps_mouse    = []
        self._KEYBOARD              = "K"
        self._MOUSE                 = "M"
    def execute_steps (self):
        pass
    def pars_keyboard (self):
        for steps in reversed(self.list_of_steps_raw):
            if self._KEYBOARD == steps[2]:
                self.list_of_steps_keyboard.append([steps[2], steps[3]])
    def pars_mouse (self):
        for index, steps in list(enumerate(self.list_of_steps_raw)):
            if self._MOUSE == steps[2]:
                mouse_button = steps[3]
                if steps[3] == "0": # for legacy
                    mouse_button = "Button.Left"
                self.list_of_steps_keyboard[index] = [steps[2], steps[0], steps[1], mouse_button]
    def format_steps(self):        
        keyboard_index = 0
        for org_index, steps in list(enumerate(self.list_of_steps_raw)):
            step = ""
            if self._MOUSE == steps[2]:
                step = self.list_of_steps_mouse[org_index]
            elif self._KEYBOARD == steps[2]:
                step = self.list_of_steps_keyboard[keyboard_index]
                keyboard_index += 1
            self.list_of_steps_formated[org_index] = step

        
