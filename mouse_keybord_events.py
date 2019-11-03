from pynput import mouse
from pynput import keyboard


def mouse_events(position_list = []):
    def on_click(x, y, button, pressed):
        # print('{0} at {1}'.format( 'Pressed' if pressed else 'Released', (x, y) ) )
        if pressed : position_list.append(tuple((x, y)))
    
    def on_release(key):
        if key == keyboard.Key.esc:
            print('{0} released, stipping recording'.format( key ) )
            listener1.stop()
            listener2.stop()
            return False
            
    # in a non-blocking fashion:
    listener1 = mouse.Listener   ( on_click=on_click )    
    listener2 = keyboard.Listener( on_release=on_release )
    listener1.start()
    listener2.start()
