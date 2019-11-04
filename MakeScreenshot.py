import PIL


class MakeScreenshot:
    def __init__(self, XYpos_list):
        self.XYpos_list = XYpos_list
        self.imageGrab = PIL.ImageGrab

    def make_screensots(self):
        for idx, XYpos in enumerate(self.XYpos_list):
            pos_x = XYpos[0]
            pos_y = XYpos[1]
            my_bbox = self.make_bbox(pos_x, pos_y)
            print(pos_x, pos_y, my_bbox)
            temp_image = self.imageGrab.grab(
                bbox=(my_bbox[0], my_bbox[1], my_bbox[2], my_bbox[3]))
            temp_name = ".\\{}_{}_{}_{}_{}_screenshot.tiff".format(
                idx, my_bbox[0], my_bbox[1], my_bbox[2], my_bbox[3])
            temp_image.save(temp_name)

    def make_bbox(self, pos_x=0, pos_y=0):
        pos_x1 = pos_x2 = pos_x
        pos_y1 = pos_y2 = pos_y
        con_num = "0"
        EXPAND_VALUE  = 150
        MIN_X = MIN_Y = 0
        MAX_X         = 1920
        MAX_Y         = 1080
        #bottom right corner
        if (pos_x >= (MAX_X-EXPAND_VALUE) and pos_y >= (MAX_Y-EXPAND_VALUE)):
            pos_x1 = MAX_X - EXPAND_VALUE
            pos_y1 = MAX_Y - EXPAND_VALUE
            con_num += ";1"            
        # bottom left corner
        elif (pos_x <= (MIN_X+EXPAND_VALUE) and pos_y >= (MAX_Y-EXPAND_VALUE)):
            pos_x2 = pos_x + EXPAND_VALUE
            pos_y1 = pos_y - EXPAND_VALUE
            # pos_x1 = pos_x
            # pos_y2 = pos_y
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
