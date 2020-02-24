import time
from datetime        import datetime
from pynput.mouse    import Button, Controller as Mouse_Controller
from pynput.keyboard import Key, Controller as Keyboard_Controller
from mouse_keybord_events import KeysDef


class ParsKeyboarMouse(KeysDef):
    def __init__(self, list_of_steps = []):
        super().__init__()
        self.list_of_steps_raw      = list_of_steps
        self.list_of_steps_keyboard = []
        self.list_of_steps_mouse    = {}
    def pars_keyboard (self, print_debug = False):        
        for steps in self.list_of_steps_raw:
            new_steps    = steps
            type_of_step = steps[4]
            if self._KEY_PRESS == type_of_step:
                if print_debug: print("step pars_keyboard")
                if print_debug: print(steps)
                key_pressed  = steps[3]
                key_pressed  = key_pressed.replace("Key.", "")
                key_pressed  = key_pressed.replace("'", "")
                new_steps[3] = key_pressed
                value_arrays = [new_steps]
                self.list_of_steps_keyboard.append(value_arrays)
    def pars_mouse (self,print_debug = False):
        for index, steps in list(enumerate(self.list_of_steps_raw)):
            type_of_step = steps[4]
            if self._MOUSE == type_of_step:
                if print_debug: print("step pars_mouse")
                if print_debug: print(steps)
                mouse_button = steps[1]                
                mouse_button = mouse_button.replace("Button.", "")
                steps[1]     = mouse_button
                self.list_of_steps_mouse[index] = [steps]

class FormatSteps(ParsKeyboarMouse):
    def __init__(self, list_of_steps = []):
        super().__init__(list_of_steps)
        self.list_of_steps_formated = []        
    def format_steps(self, print_debug):
        self.pars_keyboard()
        self.pars_mouse()
        keyboard_index = 0
        for org_index, steps in list(enumerate(self.list_of_steps_raw)):
            if print_debug: print ("org_index")
            if print_debug: print (org_index)
            if print_debug: print ("steps")
            if print_debug: print (steps)
            step = ""
            type_of_step = steps[4]
            if self._MOUSE == type_of_step:
                step = self.list_of_steps_mouse[org_index]
            elif self._KEY_PRESS == type_of_step:
                step = self.list_of_steps_keyboard[keyboard_index]
                keyboard_index += 1
            if org_index in self.list_of_steps_formated: self.list_of_steps_formated.append(step)
            else : self.list_of_steps_formated.insert(org_index,step)

class ExecuteEvents(FormatSteps):
    def __init__(self,list_of_steps):
        super().__init__(list_of_steps)
        self._MOUSE_CONTROLLER    = Mouse_Controller()
        self._KEYBOARD_CONTROLLER = Keyboard_Controller()
    def handel_mouse(self, x_pos, y_pos, function_key): #this will be in another file in the future                            
        self._MOUSE_CONTROLLER.position = ( int(x_pos),int(y_pos))
        self._MOUSE_CONTROLLER.click(Button[function_key])
    def handel_keyboard(self, function_key, was_special_key = False, special_key = ""): #this will be in another file/class in the future
        if was_special_key:
            with self._KEYBOARD_CONTROLLER.pressed(Key[special_key]):
                self._KEYBOARD_CONTROLLER.press(function_key)            
        else: 
            self._KEYBOARD_CONTROLLER.press(function_key)            

class Parser(ExecuteEvents):
    def __init__(self, list_of_steps = [], extra_time = 2):
        super().__init__(list_of_steps)                 
        self.remove_redundancy = {}                
        self._EXTRA_TIME       = extra_time
    def execute_steps (self, print_debug = False):
        self.format_steps(print_debug)
        old_time           = datetime.today
        current_step_time  = old_time
        self.old_key       = ""
        
        for numberOfStep in self.list_of_steps_formated:
            if print_debug : 
                print("self.list_of_steps_formated")
                print(self.list_of_steps_formated)
                print("numberOfStep")
                print(numberOfStep[0])
            _, function_key, x_pos,y_pos, event_type, time_taken, *_  = numberOfStep[0]            
            self.check_time(current_step_time, old_time, print_debug) # make a time before executing the next step?
            current_step_time = datetime.strptime(time_taken, "%H%M%S")            
            if not print_debug: 
                if self.event_decider(event_type,function_key, x_pos,y_pos) : continue
            old_time = current_step_time
    def event_decider(self,event_type,function_key, x_pos,y_pos):
        if event_type == self._MOUSE:
            self.handel_mouse(x_pos,y_pos,function_key)
        if event_type == self._KEY_PRESS:            
            if len(function_key) > 3:
                self.old_key            = function_key
                self.was_control_button = True
                return True
            self.handel_keyboard(function_key, self.was_control_button, self.old_key)
            self.was_control_button = False
        return False
    def check_time(self,current_step_time, old_time, print_debug = False):
        if old_time != current_step_time:
            delta_time = current_step_time - old_time
            try:                    
                time.sleep(delta_time.total_seconds() + self._EXTRA_TIME)
            except ValueError as identifier:
                if print_debug :
                    print (delta_time.total_seconds() + self._EXTRA_TIME)
                    print (identifier)