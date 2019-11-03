from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener
from pynput import mouse
from pynput import keyboard


class MouseEvents: #mozliwosc rozbudowy i zrobienia tego bardziej robust/generalnym
    def __init__(self, position_list = []):
        self.position_list = position_list
        self.start_recording()
    def on_click(self,x, y, button, pressed):
        print('{0} at {1}'.format( 'Pressed' if pressed else 'Released', (x, y) ) )
        if pressed : self.position_list.append(tuple((x, y)))
    
    def on_release(self, key):
        if key == keyboard.Key.esc:
            print('{0} released, stipping recording'.format( key ) )
            return False        
    def start_recording(self):
        with MouseListener(on_click=self.on_click) as listener:
            with KeyboardListener(on_release=self.on_release) as listener:
                listener.join()

#a simple "unit" test
# test = MouseEvents([])

        
    

        
    
                


