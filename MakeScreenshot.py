from win32gui import GetWindowText, GetForegroundWindow
import win32gui
import PIL
import os

# print("#" + GetWindowText(GetForegroundWindow()))


# while True:
#     HWND = GetForegroundWindow()
#     rect = win32gui.GetWindowRect(HWND)
#     x = rect[0]
#     y = rect[1]
#     w = rect[2] - x
#     h = rect[3] - y
#     print("Window %s:" % win32gui.GetWindowText(HWND))
#     print("test {}".format(HWND))
#     print("\tLocation: (%d, %d)" % (x, y))
#     print("\t    Size: (%d, %d)" % (w, h))
#     time.sleep(5)
class FindProcess:
    def __init__(self):
        pass



class MakeScreenshot:
    def __init__(self, EXPAND_VALUE, sequence_num):
        self.imageGrab      = PIL.ImageGrab
        self.__file_list    = []
        self.__EXPAND_VALUE = EXPAND_VALUE
        self.__MAX_X        = int(PIL.ImageGrab.grab().size[0])
        self.__MAX_Y        = int(PIL.ImageGrab.grab().size[1])
        self.sequence_num   = sequence_num

    def make_screensots(self, x, y, num_of_click, date_string = ""):
        dirImages       = ".\\images"
        if not os.path.exists(dirImages):
            os.mkdir(dirImages)
        
        pos_x      = int(x)
        pos_y      = int(y)
        my_bbox    = self.make_bbox(pos_x, pos_y)            
        temp_image = self.imageGrab.grab(
            bbox=( my_bbox[0], my_bbox[1], my_bbox[2], my_bbox[3] ))
        temp_name = ".\\{}\\{}_{}_{}_{}_{}_{}_{}_screenshot.png".format(dirImages, self.sequence_num,
                                                                        num_of_click, my_bbox[0], my_bbox[1], my_bbox[2], my_bbox[3], date_string)
        temp_image.save(temp_name)
        self.__file_list.append(temp_name)
    def make_bbox(self, pos_x=0, pos_y=0):
        return (pos_x1, pos_y1, pos_x2, pos_y2, con_num)


