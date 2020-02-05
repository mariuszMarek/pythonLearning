import time
from datetime        import datetime
from pynput.mouse    import Button, Controller as Mouse_Controller
from pynput.keyboard import Key, Controller as Keyboard_Controller 

#tutaj musze też przebudować prawie że od zera
#podzielić klasę na mniejsze kawałki by mogły dodatkowo porównywać screenshoty
class Parser:
    def __init__(self, list_of_steps = []):
        self.list_of_steps_raw      = list_of_steps
        self.list_of_steps_formated = {}
        self.list_of_steps_keyboard = []
        self.list_of_steps_mouse    = {}
        self.remove_redundancy      = {}
        self._KEYBOARD_PRESS        = "KP"
        self._KEYBOARD_RELEASE      = "KR"
        self._MOUSE                 = "M"
        self._MOUSE_CONTROLLER      = Mouse_Controller()
        self._KEYBOARD_CONTROLLER   = Keyboard_Controller()
        
    def execute_steps (self, print_debug = False):
        self.format_steps(print_debug)
        old_time           = datetime.today
        time_stamp         = old_time
        old_key            = ""
        was_control_button = False 
        for numberOfStep in self.list_of_steps_formated:
            currentSteps                                       = self.list_of_steps_formated[numberOfStep]
            event_type, x_pos, y_pos, function_key, time_taken = currentSteps
            current_step_time                                  = datetime.strptime(time_taken, "%H%M%S")
            
            if old_time != time_stamp:
                delta_time = current_step_time - old_time
                try:                    
                    time.sleep(delta_time.total_seconds()+3)
                except ValueError as identifier:
                    print (currentSteps)
                    print (delta_time.total_seconds()+2)
                    print (identifier)
                    pass
            
            if not print_debug:
                if event_type == self._MOUSE:                
                    self.handel_mouse(x_pos,y_pos,function_key)
                if event_type == self._KEYBOARD_PRESS:                                                
                    if len(function_key) > 1:
                        old_key = function_key
                        was_control_button = True
                        continue
                    self.handel_keyboard(function_key, was_control_button, old_key)
                    was_control_button = False
            old_time = current_step_time

    def handel_mouse(self, x_pos, y_pos, function_key): #this will be in another file in the future                            
        self._MOUSE_CONTROLLER.position = ( int(x_pos),int(y_pos) )
        self._MOUSE_CONTROLLER.click(Button[function_key])

    def handel_keyboard(self, function_key, was_special_key = False, special_key = ""): #this will be in another file/class in the future
        if was_special_key:
            with self._KEYBOARD_CONTROLLER.pressed(Key[special_key]):
                self._KEYBOARD_CONTROLLER.press(function_key)            
        else: 
            self._KEYBOARD_CONTROLLER.press(function_key)            
    def pars_keyboard (self):
        self.remove_redundancy = {}
        for steps in self.list_of_steps_raw:            
            if self._KEYBOARD_PRESS == steps[2]:
                key_pressed  = steps[3]
                key_pressed  = key_pressed.replace("Key.", "")
                key_pressed  = key_pressed.replace("'", "")
                value_arrays = [steps[2], steps[0], steps[1], key_pressed, steps[4]]                
                self.list_of_steps_keyboard.append(value_arrays)
    
    def pars_mouse (self):
        for index, steps in list(enumerate(self.list_of_steps_raw)):
            if self._MOUSE == steps[2]:
                mouse_button = steps[3]
                if steps[3] == "0": # for legacy
                    mouse_button = "Button.left"
                mouse_button = mouse_button.replace("Button.", "")
                self.list_of_steps_mouse[index] = [steps[2], steps[0], steps[1], mouse_button, steps[4]]

    def format_steps(self, print_debug):
        self.pars_keyboard()
        self.pars_mouse()
        keyboard_index = 0
        for org_index, steps in list(enumerate(self.list_of_steps_raw)):
            if print_debug: print (org_index)
            if print_debug: print (steps)
            step = ""
            if self._MOUSE == steps[2]:
                step = self.list_of_steps_mouse[org_index]
            elif self._KEYBOARD_PRESS == steps[2]:
                step = self.list_of_steps_keyboard[keyboard_index]
                keyboard_index += 1
            self.list_of_steps_formated[org_index] = step
