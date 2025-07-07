import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_1inch28
from PIL import Image,ImageDraw,ImageFont
import math
# Raspberry Pi pin configuration:
# RST = 27
# DC = 25
# BL = 18
# bus = 0 
# device = 0 
logging.basicConfig(level=logging.DEBUG)
class Watch:
    # Raspberry Pi pin configuration:
    RST = 27
    DC = 25
    BL = 18
    bus = 0 
    device = 0 
    logging.basicConfig(level=logging.DEBUG)
    def __init__(self , center_x , center_y , second_radius , minute_radius , hour_radius):
        self.center_x = center_x
        self.center_y = center_y
        self.second_radius = second_radius
        self.minute_radius = minute_radius
        self.hour_radius = hour_radius
        # Initialize library.
        self.disp = LCD_1inch28.LCD_1inch28()
        # Create blank image for drawing.
        # get a tuple size 
        self.image1 = Image.new("RGB", (self.disp.width, self.disp.height), "BLACK") 
        # create a obj to create own draw
        self.draw = ImageDraw.Draw(self.image1)
    def init_display(self):
        self.disp.Init()
        # Clear display.
        self.disp.clear()
        #Set the backlight to 50
        self.disp.bl_DutyCycle(50)        
    def draw_circle(self):
         #logging.info("draw point")
        #draw.rectangle((Xstart,Ystart,Xend,Yend), fill = "color")
        logging.info("draw circle")
        # param 1 cordinate rectabgle 
        # param 2 start cordinate degree and end cordinate degree
        # param 3 fill = color arc we use it actully blue
        self.draw.arc((1,1,239,239),0, 360, fill =(0,0,255))
        self.draw.arc((2,2,238,238),0, 360, fill =(0,0,255))
        self.draw.arc((3,3,237,237),0, 360, fill =(0,0,255))
    def draw_dial_line(self):
        logging.info("draw dial line")
        self.draw.line([(120, 1),(120, 12)], fill = (128,255,128),width = 4)
        self.draw.line([(120, 227),(120, 239)], fill = (128,255,128),width = 4)
        self.draw.line([(1,120),(12,120)], fill = (128,255,128),width = 4)
        self.draw.line([(227,120),(239,120)], fill = (128,255,128),width = 4)
    def draw_text(self):
        logging.info("draw text")
        # Create a font object to use into a text param
        Font1 = ImageFont.truetype("../Font/Font01.ttf",25)
        Font2 = ImageFont.truetype("../Font/Font01.ttf",50)
        Font3 = ImageFont.truetype("../Font/Font02.ttf",32)

        # create a text
        self.draw.text((60, 40), 'Watch', fill = (128,255,128),font=Font2)
        # create unicode text
        text= u"Written By Mehdi"
        self.draw.text((30, 150),text, fill = "WHITE",font=Font3)
    def time(self):
        logging.info("draw second line")
        logging.info("Draw Minute line ")
        while True:
            current_second = time.localtime().tm_sec
            current_minute = time.localtime().tm_min
            current_hour = time.localtime().tm_hour
            angle_second = (current_second * 6) - 90
            angle_minute = (current_minute * 6) - 90
            angle_hour = (current_hour * 30) + (current_minute * 0.5) - 90
            angle_rad_second = math.radians(angle_second)
            angle_rad_minute = math.radians(angle_minute)
            angle_rad_hours = math.radians(angle_hour)
            # end second
            end_x_second = self.center_x + self.second_radius * math.cos(angle_rad_second)
            end_y_second = self.center_y + self.second_radius * math.sin(angle_rad_second)
            # end minute
            end_x_minute = self.center_x + self.minute_radius * math.cos(angle_rad_minute)
            end_y_minute = self.center_y + self.minute_radius * math.sin(angle_rad_minute)
            # end hour
            end_x_hour = self.center_x + self.hour_radius * math.cos(angle_rad_hours)
            end_y_hour = self.center_y + self.hour_radius * math.sin(angle_rad_hours)
            img = self.image1.copy()  # کپی تصویر پایه
            draw = ImageDraw.Draw(img)
            # second
            draw.line([(self.center_x, self.center_y),(end_x_second, end_y_second)], fill = "YELLOW",width = 3)
            # minute
            draw.line([(self.center_x, self.center_y),(end_x_minute, end_y_minute)], fill = "RED",width = 3)
            # hour
            draw.line([(self.center_x, self.center_y),(end_x_hour, end_y_hour)], fill = "BLUE",width = 3)
            im_r = img.rotate(180)
            self.disp.ShowImage(im_r)
        
            time.sleep(1)
    def exit_module(self):
        self.disp.module_exit()
        logging.info("quit:")
            # except IOError as e:
            #     logging.info(e)    
            # except KeyboardInterrupt:
            #     self.disp.module_exit()
            # logging.info("quit:")
            # exit()
            
watch = Watch(120,120,105,100,80)
watch.init_display()
watch.draw_circle()
watch.draw_text()
watch.draw_dial_line()
try:
    watch.time()
except KeyboardInterrupt:
    watch.exit_module()
    exit()