import win32gui
import PIL
import os
import wmi
class ProcessFinder:
    def __init__(self):
        self._HWND           = win32gui.GetForegroundWindow()
        self._window_rect    = win32gui.GetWindowRect(self._HWND)
        self.process_name    = ""
        self.window_pos_XY   = [self._window_rect[0], self._window_rect[1]]
        self._window_size_WH = [self._window_rect[2] - self.window_pos_XY[0], self._window_rect[3] - self.window_pos_XY[1]]
        self._window_name    = win32gui.GetWindowText(self._HWND)
        self._wmi_process    = wmi.WMI()
        self._exe_path       = ""
        self._exe_name       = ""
    def update_window_info(self):
        if win32gui.GetForegroundWindow() != self._HWND:
            self._HWND           = win32gui.GetForegroundWindow()
            self._window_rect    = win32gui.GetWindowRect(self._HWND)
            self.process_name    = ""
            self.window_pos_XY   = [self._window_rect[0], self._window_rect[1]]
            self._window_size_WH = [self._window_rect[2] - self.window_pos_XY[0], self._window_rect[3] - self.window_pos_XY[1]]
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
        # timestamp, order_num, sequence_num
        self._imageGrab     = PIL.ImageGrab # for screenshots
        self._file_list     = []
        self._root_location = root_location
    def make_screensots(self, parameters):
        dirImages       = self._root_location
        if not os.path.exists(dirImages): # always check just in case
            os.mkdir(dirImages)
        
    #     pos_x      = int(x)
    #     pos_y      = int(y)
    #     my_bbox    = self.make_bbox(pos_x, pos_y)            
    #     temp_image = self.imageGrab.grab(
    #         bbox=( my_bbox[0], my_bbox[1], my_bbox[2], my_bbox[3] ))
    #     temp_name = ".\\{}\\{}_{}_{}_{}_{}_{}_{}_screenshot.png".format(dirImages, self.sequence_num,
    #                                                                     num_of_click, my_bbox[0], my_bbox[1], my_bbox[2], my_bbox[3], date_string)
    #     temp_image.save(temp_name)
    #     self.__file_list.append(temp_name)
    # def make_bbox(self, pos_x=0, pos_y=0):
    #     return (pos_x1, pos_y1, pos_x2, pos_y2, con_num)


