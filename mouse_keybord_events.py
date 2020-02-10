from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
from MakeScreenshot import MakeScreenshot
from pynput import mouse
from pynput import keyboard
import time

class TypeEvents:
    def __init__(self, stop_button = keyboard.Key['shift']):
        self._MOUSE       = "M"
        self._KEY_PRESS   = "KP"
        self._KEY_RELEASE = "KR"
        self._stop_button = stop_button
        self._last_x      = 0.0
        self._last_y      = 0.0
        pass
    def on_click(self, x, y, button, pressed):
        self._last_x = x
        self._last_y = y
        if pressed : return[pressed, button, x, y, self._MOUSE]
    def on_release(self, key): 
        if key == self._stop_button:
            print('{0} released, stopping recording'.format(key))
            return [False]
        return [True,key, self._last_x, self._last_y, self._KEY_RELEASE]
    def on_press(self, key):        
        if key == self._stop_button:
            print('{0} pressed, stopping recording'.format(key))
            return [False]
        return [True,key, self._last_x, self._last_y, self._KEY_PRESS]

class ControllerEvents(TypeEvents): 
    def __init__(self, stop_key=keyboard.Key['shift']):
        super().__init__(stop_key)
        self.num_of_click = 0        
    def on_click(self, x, y, button, pressed):
        if pressed:            
            results = super().on_click(x, y, button, pressed)            
            results.append(self.get_time_stamp(), self.order_num())            
            return results
    def on_release(self, key):  # this is for the future        
        results = super().on_release(key)
        if not results[0]: return [results[0]]            
        else : return results.append(self.get_time_stamp(),self.order_num())
    def on_press(self, key):
        results = super().on_press(key)
        if not results[0]: return [results[0]]
        return results.append(self.get_time_stamp(), self.order_num())        
    def get_time_stamp(self):
        return time.strftime("%H%M%S")
    def order_num(self):        
        self.num_of_click += 1
        return self.num_of_click

class MouseKeyboardEvents(ControllerEvents): #this class is responsible for recording and running the "screenshot" class
    def __init__(self, screen_shot_class: MakeScreenshot , sequence_num=0, events_list={}, stop_key=keyboard.Key['shift']):
        super().__init__(stop_key)
        self.ScreenShots         = screen_shot_class        
        self._list_of_steps      = events_list
        self._sequence_num       = sequence_num
        self.start_recording()
    def on_click(self, x, y, button, pressed):
        results = super().on_click(x,y,button,pressed)        
        if results[0]:            
            self.add_do_dictionary(results)
    def on_press(self,key):
        results = super().on_press(key)
        if results[0]:            
            self.add_do_dictionary(results)
    def add_do_dictionary(self, results):
            dict_key = str(results)
            # 0           1     2    3      4               5          6         7
            #true/false, key, pos_x,pos_y,pressedName, timestamp, order_num, sequence_num
            if dict_key not in self._list_of_steps:
                print(results)
                self._list_of_steps[dict_key] = results.append(self._sequence_num)
                if results[4] == self._MOUSE:
                    parameters_for_screenshot = results[5:7:1]                    
                    self.ScreenShots.make_screenshots(parameters_for_screenshot)
    def start_recording(self):
        with MouseListener(on_click=self.on_click) as listener:
            with KeyboardListener(on_press=self.on_press) as listener:
                listener.join()
from MakeScreenshot import MakeScreenshot
steps    = {}
sequence = 0
stopKey = keyboard.Key['shift']
test = MouseKeyboardEvents(MakeScreenshot(),sequence,steps,stopKey)
