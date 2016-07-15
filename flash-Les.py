#!/usr/bin/env python

import time
import math
from microdotphat import clear, show, set_pixel, WIDTH, HEIGHT
from random import randint

t = 0.01
print WIDTH

while True:
    """
    rand_x1 = randint(0,45)
    rand_y1 = randint(0,6)
    rand_x2 = randint(0,45)
    rand_y2 = randint(0,6)
    rand_x3 = randint(0,45)
    rand_y3 = randint(0,6)
    rand_x4 = randint(0,45)
    rand_y4 = randint(0,6)
    rand_x5 = randint(0,45)
    rand_y5 = randint(0,6)
    rand_x6 = randint(0,45)
    rand_y6 = randint(0,6)
    rand_x7 = randint(0,45)
    rand_y7 = randint(0,6)
    rand_x8 = randint(0,45)
    rand_y8 = randint(0,6)
    """
    clear()
    show()
    time.sleep(t)
    for x in range(45):
        set_pixel(x,0,1)
        set_pixel(x,2,1)
        set_pixel(x,4,1)
        set_pixel(x,6,1)       
        show()
        """
        for y in range(6):
            set_pixel(rand_x1,rand_y1,1)
            set_pixel(rand_x2,rand_y2,1)
            set_pixel(rand_x3,rand_y3,1)
            set_pixel(rand_x4,rand_y4,1)
            set_pixel(rand_x5,rand_y5,1)
            set_pixel(rand_x6,rand_y6,1)
            set_pixel(rand_x7,rand_y7,1)
            set_pixel(rand_x8,rand_y8,1)
    show()
    """
    time.sleep(t)
