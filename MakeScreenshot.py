import PIL
import os

class MakeScreenshot:
    def __init__(self, EXPAND_VALUE):        
        self.imageGrab      = PIL.ImageGrab
        self.__file_list    = []
        self.__EXPAND_VALUE = EXPAND_VALUE
        self.__MAX_X        = int(PIL.ImageGrab.grab().size[0])
        self.__MAX_Y        = int(PIL.ImageGrab.grab().size[1])

    def make_screensots(self, XYpos_list, sequence_num):
        self.XYpos_list = XYpos_list
        dirImages       = ".\\images"
        if not os.path.exists(dirImages):
            os.mkdir(dirImages)
        for idx, XYpos in enumerate(self.XYpos_list):
            pos_x      = int(XYpos[0])
            pos_y      = int(XYpos[1])
            my_bbox    = self.make_bbox(pos_x, pos_y)            
            temp_image = self.imageGrab.grab(
                bbox=( my_bbox[0], my_bbox[1], my_bbox[2], my_bbox[3] ))
            temp_name = ".\\{}\\{}_{}_{}_{}_{}_{}_screenshot.png".format(dirImages, sequence_num,
                idx, my_bbox[0], my_bbox[1], my_bbox[2], my_bbox[3])
            temp_image.save(temp_name)
            self.__file_list.append(temp_name)
    def make_bbox(self, pos_x=0, pos_y=0):
        pos_x1 = pos_x2 = pos_x
        pos_y1 = pos_y2 = pos_y
        con_num       = "0" # for debuging
        EXPAND_VALUE  = self.__EXPAND_VALUE
        MIN_X         = MIN_Y = 0
        MAX_X         = self.__MAX_X
        MAX_Y         = self.__MAX_Y
        #bottom right corner
        if (pos_x >= (MAX_X-EXPAND_VALUE) and pos_y >= (MAX_Y-EXPAND_VALUE)):
            pos_x1 = MAX_X - EXPAND_VALUE
            pos_y1 = MAX_Y - EXPAND_VALUE
            con_num += ";1"            
        # bottom left corner
        elif (pos_x <= (MIN_X+EXPAND_VALUE) and pos_y >= (MAX_Y-EXPAND_VALUE)):
            pos_x2 = pos_x + EXPAND_VALUE
            pos_y1 = pos_y - EXPAND_VALUE
            con_num += ";2"
        # upper left corner
        elif (pos_x <= (MIN_X+EXPAND_VALUE) and pos_y <= (MIN_Y+EXPAND_VALUE)):
            pos_x1 = MIN_X
            pos_y1 = MIN_Y
            pos_x2 = pos_x + EXPAND_VALUE
            pos_y2 = pos_y + EXPAND_VALUE
            con_num += ";3"
        # upper right corner
        elif (pos_x >= (MAX_X-EXPAND_VALUE ) and pos_y <= (MIN_Y+EXPAND_VALUE)):
            pos_x1 = MAX_X - EXPAND_VALUE
            pos_y1 = MIN_Y
            pos_x2 = MAX_X
            pos_y2 = pos_y + EXPAND_VALUE
            con_num += ";4"        
        else:
            #not near edges and corners
            pos_x1 = pos_x - EXPAND_VALUE
            pos_y1 = pos_y - EXPAND_VALUE
            pos_x2 = pos_x + EXPAND_VALUE
            pos_y2 = pos_y + EXPAND_VALUE
            # if edges then overwrite some values
            # bottom edge
            if (pos_y >= (MAX_Y-EXPAND_VALUE)): 
                if(pos_y >= MAX_Y):
                    pos_y1 = MAX_Y - EXPAND_VALUE
                    pos_y2 = MAX_Y
                    con_num += ";5"
                else:
                    pos_y1 = pos_y - EXPAND_VALUE
                    pos_y2 = pos_y + (MAX_Y-pos_y)
                    con_num += ";6"
            # right edge
            elif (pos_x >= (MAX_X-EXPAND_VALUE)):
                if(pos_x >= MAX_X):
                    pos_x2 = MAX_X
                    con_num += ";7"
                else:
                    pos_x2 = pos_x + (MAX_X-pos_x)
                    con_num += ";8"
            # left edged
            elif (pos_x <= (MIN_X+EXPAND_VALUE)):
                pos_x1 = pos_x
                con_num += ";9"
            # upper edge
            elif (pos_y <= (MIN_Y+EXPAND_VALUE)):
                pos_y1 = MIN_Y
                pos_y2 = pos_y + EXPAND_VALUE
                con_num += ";10"
        return (pos_x1, pos_y1, pos_x2, pos_y2, con_num)
