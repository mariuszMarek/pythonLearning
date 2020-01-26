from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
from MakeScreenshot import MakeScreenshot
from pynput import mouse
from pynput import keyboard
import time


class MouseEvents: #mozliwosc rozbudowy i zrobienia tego bardziej robust/generalnym
    def __init__(self, sequence_num, position_list=[], SCREENSHOT_SIZE=100):
        self.position_list    = position_list
        self._last_x          = 0.0
        self._last_y          = 0.0
        self.num_of_click     = 0
        self._SCREENSHOT_SIZE = SCREENSHOT_SIZE
        self.ScreenShots      = MakeScreenshot(self._SCREENSHOT_SIZE, sequence_num)
        
        self.start_recording() # this has to be last
        
    def on_click(self,x, y, button, pressed):
        # print('{0} at {1}'.format( 'Pressed' if pressed else 'Released', (x, y) ) )
        self._last_x = x
        self._last_y = y
        time_of_click = time.strftime("%H%M%S")
        if pressed :             
            self.position_list.append(tuple((x, y, "0","M", time_of_click)))
            self.ScreenShots.make_screensots(x, y, self.num_of_click, time_of_click)
            self.num_of_click += 1
    
    def on_release(self, key):
        time_of_click = time.strftime("%H%M%S")
        if key == keyboard.Key.shift:
            print('{0} released, stopping recording'.format( key ) )
            return False
        self.position_list.append(tuple((self._last_x, self._last_y, key, "K", time_of_click)))
    def start_recording(self):
        with MouseListener(on_click=self.on_click) as listener:
            with KeyboardListener(on_release=self.on_release) as listener:
                listener.join()

#a simple "unit" test
# test = MouseEvents([])

        
    

        
    
                


