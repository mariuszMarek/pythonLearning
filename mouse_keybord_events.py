from pynput import mouse
from pynput import keyboard


def mouse_events(position_list = []):
    # def on_move(x, y):
    #     print('Pointer moved to {0}'.format( (x, y) ) )
    def on_click(x, y, button, pressed):
        # print('{0} at {1}'.format( 'Pressed' if pressed else 'Released', (x, y) ) )
        if pressed : position_list.append(tuple((x, y)))
        # if not pressed: ?
            # Stop listener
            # return False
     # def on_scroll(x, y, dx, dy):
        # print('Scrolled {0} at {1}'.format( 'down' if dy < 0 else 'up', (x, y) ) )

    # in a non-blocking fashion litener:
    listener1 = mouse.Listener( on_click=on_click )
    listener1.start()
    def on_press(key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))


    def on_release(key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False
    # ...or, in a non-blocking fashion:
    listener2 = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener2.start()
