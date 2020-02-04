from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
from MakeScreenshot import MakeScreenshot
from pynput import mouse
from pynput import keyboard
import time

class TypeEvents:
    def __init__(self, stop_button = keyboard.Key['shift']):
        self._stop_button = stop_button
        self._last_x      = 0.0
        self._last_y      = 0.0
        pass
    def on_click(self, x, y, button, pressed):
        self._last_x = x
        self._last_y = y
        return [x, y, button, pressed]
    def on_release(self, key): 
        if key == self._stop_button:
            print('{0} released, stopping recording'.format(key))
            return False
    def on_press(self, key):        
        if key == self._stop_button:
            print('{0} pressed, stopping recording'.format(key))
            return False
        return [key, self._last_x, self._last_y]


class ControllerEvents(TypeEvents): 
    def __init__(self, stop_key):
        super().__init__(keyboard.Key[stop_key])
        self.position_list      = position_list
        self.num_of_click       = 0
        self._SCREENSHOT_SIZE_X = SCREENSHOT_SIZE_X
        self._SCREENSHOT_SIZE_Y = SCREENSHOT_SIZE_Y
        self._MOUSE             = "M"
        self._KEY_PRESS         = "KP"
        self._KEY_RELEASE       = "KR"
        # self.ScreenShots        = MakeScreenshot(self._SCREENSHOT_SIZE_X, self._SCREENSHOT_SIZE_Y, sequence_num)
        
        self.start_recording() # this has to be last

    def on_click(self, x, y, button, pressed):
        results = super().on_click(x, y, button, pressed)        
        results.append(time.strftime("%H%M%S"))
        if pressed:
            self.position_list.append(
                tuple((x, y, button, self._MOUSE, time_of_click)))
            self.ScreenShots.make_screensots(
                x, y, self.num_of_click, time_of_click)
            self.num_of_click += 1

    def on_release(self, key):  # this is for the future
        time_of_click = time.strftime("%H%M%S")
        if key == keyboard.Key.shift:
            print('{0} released, stopping recording'.format(key))
            return False
        self.position_list.append(
            tuple((self._last_x, self._last_y, key, self._KEY_RELEASE, time_of_click)))

    def on_press(self, key):
        time_of_click = time.strftime("%H%M%S")
        if key == keyboard.Key.shift:
            print('{0} pressed, stopping recording'.format(key))
            return False
        self.position_list.append(
            tuple((self._last_x, self._last_y, key, self._KEY_PRESS, time_of_click)))


    def start_recording(self):
        with MouseListener(on_click=self.on_click) as listener:
            with KeyboardListener(on_press=self.on_press) as listener:
                listener.join()


class MouseKeyboard(ControllerEvents):
    ef __init__(self, stop_key, sequence_num=0, position_list=[], SCREENSHOT_SIZE_X=100, SCREENSHOT_SIZE_Y=100):
        super().__init__(sequence_num)
    

        
    

        
    
                


