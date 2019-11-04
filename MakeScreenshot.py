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
            temp_name = ".\\{}_screenshot.jpg".format(idx)
            temp_image.save(temp_name)

    def make_bbox(self, pos_x=0, pos_y=0):
        pos_x1 = pos_x2 = pos_x
        pos_y1 = pos_y2 = pos_y
        EXPAND_VALUE = 150
        MIN_X = MIN_Y = 0
        MAX_X = 1920
        MAX_Y = 1080

        pos_x1 -= EXPAND_VALUE
        pos_y1 -= EXPAND_VALUE
        #bottom right corner
        if (pos_x >= (MAX_X-EXPAND_VALUE) and pos_y >= (MAX_Y-EXPAND_VALUE)):
            pos_y1 -= EXPAND_VALUE
            pos_x1 -= EXPAND_VALUE
            pos_x2 = pos_x
            pos_y2 = pos_y
        # upper left corner
        if(pos_x == MIN_X and pos_y == MIN_Y):
            pos_x2 += EXPAND_VALUE
            pos_y2 += EXPAND_VALUE
        # bottom left corner
        # if(pos_x == MIN_X and pos_y >= (MAX_X-EXPAND_VALUE)):
        #     pos_x2 += EXPAND_VALUE

        #bottom edge
        if (pos_y >= (MAX_Y-EXPAND_VALUE)): 
            if(pos_y >= MAX_Y):
                pos_y2 = MAX_Y
            else:
                pos_y2 = pos_y + (MAX_Y-pos_y)
        # right edge
        if (pos_x >= (MAX_X-EXPAND_VALUE)):
            if(pos_x >= MAX_X):
                pos_x2 = MAX_X
            else:
                pos_x2 = pos_x + (MAX_X-pos_x)

        # left edged
        if (pos_x <= (MIN_X+EXPAND_VALUE)):
            pos_x1 = pos_x
        # upper edge
        if (pos_y <= (MIN_Y+EXPAND_VALUE)):
            pos_y1 = pos_y

        return (pos_x1, pos_y1, pos_x2, pos_y2)
    # def make_screensots(self):
    #     # tutaj zrobic screenshoty do tego ? to juz moze oddzielna klasa/funkcja
    #     pass
    #     for position_
    #     # PIL.ImageGrab.grab
