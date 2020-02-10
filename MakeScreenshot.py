import win32gui
import os
import wmi
from PIL import Image, ImageGrab 
class ProcessFinder:
    def __init__(self):
        self._HWND           = win32gui.GetForegroundWindow()
        self._window_rect    = win32gui.GetWindowRect(self._HWND)
        self.window_pos_XY   = [self._window_rect[0], self._window_rect[1]]
        self.window_size_WH  = [self._window_rect[2] - self.window_pos_XY[0], self._window_rect[3] - self.window_pos_XY[1]]
        self._window_name    = win32gui.GetWindowText(self._HWND)
        self._wmi_process    = wmi.WMI()
        self._exe_path       = ""
        self._exe_name       = ""
    def update_window_info(self):
        if win32gui.GetForegroundWindow() != self._HWND:
            self._HWND           = win32gui.GetForegroundWindow()
            self._window_rect    = win32gui.GetWindowRect(self._HWND)            
            self.window_pos_XY   = [self._window_rect[0], self._window_rect[1]]
            self.window_size_WH  = [self._window_rect[2] - self.window_pos_XY[0], self._window_rect[3] - self.window_pos_XY[1]]
            self._window_name    = win32gui.GetWindowText(self._HWND)
            self._wmi_process    = wmi.WMI()
            self._exe_path       = ""
            self._exe_name       = ""
    def find_process(self): #a need to check if it can be one query in WMI
        try:
            _, pid = win32process.GetWindowThreadProcessId(self._HWND)
            for p in c.query('SELECT ExecutablePath FROM Win32_Process WHERE ProcessId = %s' % str(pid)):
                self._exe_path = p.ExecutablePath                 
                return self._exe_path
        except:
            return False
    def find_proc_name(self):        
        try:
            _, pid = win32process.GetWindowThreadProcessId(self._HWND)
            for p in c.query('SELECT Name FROM Win32_Process WHERE ProcessId = %s' % str(pid)):
                self._exe_name = p.Name
                return self._exe_name
        except:
            return False
class MakeScreenshot(ProcessFinder):
    def __init__(self, root_location = ".\\images"):
        super().__init__()
        
        self._imageGrab     = ImageGrab # for screenshots
        self._file_list     = []
        self._root_location = root_location
    def make_screensots(self, parameters):
        super().update_window_info()        
        time_stamp, order_num, sequence_num = parameters
        
        dirImage  = self._root_location + "\\{}\\".format(sequence_num)

        if not os.path.exists(dirImage): # always check just in case
            os.mkdir(dirImage)
        my_bbox    = self._window_rect
        temp_image = self._imageGrab.grab(bbox =( my_bbox ))
        temp_name  = "{}_{}_{}_{}_{}_screenshot.png".format(sequence_num, order_num, time_stamp, super().find_proc_name(), self._window_name)
        temp_image.save(dirImage + temp_name)    


