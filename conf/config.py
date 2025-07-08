import time
import os
import sys
import logging
import spidev as SPI
import math
sys.path.append('../')
from lib import LCD_1inch28
from PIL import Image , ImageDraw ,  ImageFont
#Raspberry pi pin configuration
RST = 27
DC = 25
BL = 18
BUS = 0
DEVICE = 0
logging.basicConfig(level=logging.DEBUG)

class Configuration:
    def __init__(self):
        self.disp = LCD_1inch28.LCD_1inch28()
        self.width = self.disp.width
        self.height = self.disp.height
        self.image = Image.new('RGB', (self.width , self.height) , "#2C3E50")
        self.draw = ImageDraw.Draw(self.image)
        font_dir = '/home/user-null/Documents/station_lcd/Font/'        
        self.font1 = ImageFont.truetype(font_dir + 'Font00.ttf' , size=12)
        self.font2 = ImageFont.truetype(font_dir + 'Font01.ttf' , size=12)
        self.font3 = ImageFont.truetype(font_dir + 'Font02.ttf' , size=12)
    def init_display(self):
        self.disp.Init()
        self.disp.clear()
        self.disp.bl_DutyCycle(50)
    def show_image(self):
        im_r = self.image.rotate(180)
        self.disp.ShowImage(im_r)
        time.sleep(3)
    def module_die(self):
        self.disp.module_exit()
        logging.info("Quit.")

