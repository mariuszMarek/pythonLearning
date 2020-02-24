import win32process
import win32gui
import psutil
import os
import re
from PIL import Image, ImageGrab 
from root_files_to_save import RootLocation
class ProcessFinder(RootLocation):
    def __init__(self):
        super().__init__()
        self._HWND           = win32gui.GetForegroundWindow()
        self._window_rect    = win32gui.GetWindowRect(self._HWND)
        self._window_name    = win32gui.GetWindowText(self._HWND)
        self._proc_meta_data = []
        self.get_proc_meta()
    def update_window_info(self):
        if (win32gui.GetForegroundWindow() != self._HWND) or (self._window_rect != win32gui.GetWindowRect(self._HWND)):
            self._HWND           = win32gui.GetForegroundWindow()
            self._window_rect    = win32gui.GetWindowRect(self._HWND)
            self._window_name    = win32gui.GetWindowText(self._HWND)
            self._proc_meta_data = []
            self.get_proc_meta()
    def get_proc_meta(self):
        try:
            _, pid = win32process.GetWindowThreadProcessId(self._HWND)
            process_info = psutil.Process(pid)
            with process_info.oneshot():
                self._proc_meta_data.append( process_info.name() )
                self._proc_meta_data.append( process_info.exe() )
                self._proc_meta_data.append( self._window_name )
        except NameError as error_short:
            print(error_short)
            return False
class MakeScreenshot(ProcessFinder):
    def __init__(self, root_location = ".\\images\\"):
        super().__init__()
        root_location = self._script_location + "\\images\\" if root_location == ".\\images\\" else root_location + "\\images\\"
        self._imageGrab     = ImageGrab # for screenshots
        self._file_list     = []
        self._root_location = str(root_location)
    def make_screensots(self, parameters = [],save_image = 1):
        super().update_window_info()
        if save_image == 1 : 
            time_stamp, order_num, sequence_num = parameters
            dirImage  = self._root_location + "\\{}\\".format(sequence_num)
            temp_name = "{}_{}_{}_{}_screenshot.png".format( sequence_num, order_num, time_stamp, self._proc_meta_data[0])
            if not os.path.exists(dirImage): # always check just in case
                os.mkdir(dirImage)
            self.save_image(dirImage + temp_name, self.grab_image())
        else: return self.grab_image()
        parameters.clear()
        parameters += self._proc_meta_data
    def grab_image(self):
        return self._imageGrab.grab(bbox =( self._window_rect ))
    def save_image(self,image_location, temp_image):
        temp_image.save(image_location)