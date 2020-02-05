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
        return [True,button, x, y, pressed, self._MOUSE]
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
            results.append(time.strftime("%H%M%S"), self.num_of_click)            
            self.num_of_click += 1
            return results
    def on_release(self, key):  # this is for the future        
        results = super().on_release(key)
        if not results[0]: return [results[0]]            
        else : return results.append(self.get_time_stamp())            
    def on_press(self, key):
        results = super().on_press(key)
        if not results[0]: return [results[0]]
        return results.append(self.get_time_stamp())
    def get_time_stamp(self):
        return time.strftime("%H%M%S")
class MouseKeyboardEvents(ControllerEvents): #tutaj bede nagrywal
    def __init__(self, stop_key,screen_shot_class, sequence_num=0, events_list=[], SCREENSHOT_SIZE_X=100, SCREENSHOT_SIZE_Y=100):
        super().__init__(stop_key)
        self.ScreenShots = screen_shot_class(SCREENSHOT_SIZE_X, SCREENSHOT_SIZE_Y, sequence_num)
        # self.ScreenShots        = MakeScreenshot(self._SCREENSHOT_SIZE_X, self._SCREENSHOT_SIZE_Y, sequence_num)
        super().__init__(sequence_num)        
        #self.ScreenShots.make_screensots(x, y, self.num_of_click, time_of_click)        
    def start_recording(self):
        with MouseListener(on_click=self.on_click) as listener:
            with KeyboardListener(on_press=self.on_press) as listener:
                listener.join()
    

        
    

        
    
                


