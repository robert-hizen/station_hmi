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
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)
try:
    # display with hardware SPI:
    ''' Warning!!!Don't  creation of multiple displayer objects!!! '''
    #disp = LCD_1inch28.LCD_1inch28(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
    disp = LCD_1inch28.LCD_1inch28()
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()
    #Set the backlight to 50
    disp.bl_DutyCycle(50)

    # Create blank image for drawing.
    # get a tuple size
    image1 = Image.new("RGB", (disp.width, disp.height), "BLACK")
    # create a obj to create own draw
    draw = ImageDraw.Draw(image1)

    #logging.info("draw point")
    #draw.rectangle((Xstart,Ystart,Xend,Yend), fill = "color")
    logging.info("draw circle")
    # param 1 cordinate rectabgle 
    # param 2 start cordinate degree and end cordinate degree
    # param 3 fill = color arc we use it actully blue
    draw.arc((1,1,239,239),0, 360, fill =(0,0,255))
    draw.arc((2,2,238,238),0, 360, fill =(0,0,255))
    draw.arc((3,3,237,237),0, 360, fill =(0,0,255))
    
    logging.info("draw dial line")

    draw.line([(120, 1),(120, 12)], fill = (128,255,128),width = 4)
    draw.line([(120, 227),(120, 239)], fill = (128,255,128),width = 4)
    draw.line([(1,120),(12,120)], fill = (128,255,128),width = 4)
    draw.line([(227,120),(239,120)], fill = (128,255,128),width = 4)
    
    logging.info("draw text")
    # Create a font object to use into a text param
    Font1 = ImageFont.truetype("../Font/Font01.ttf",25)
    Font2 = ImageFont.truetype("../Font/Font01.ttf",50)
    Font3 = ImageFont.truetype("../Font/Font02.ttf",32)

    # create a text
    draw.text((60, 40), 'Watch', fill = (128,255,128),font=Font2)
    # create unicode text
    text= u"Mehdi Written"
    draw.text((50, 150),text, fill = "WHITE",font=Font3)
    # crate a line
    def second(center_x , center_y , second_radius = 120 , minute_radius = 100 , hour_radius = 80):
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
            end_x_second = center_x + second_radius * math.cos(angle_rad_second)
            end_y_second = center_y + second_radius * math.sin(angle_rad_second)
            # end minute
            end_x_minute = center_x + minute_radius * math.cos(angle_rad_minute)
            end_y_minute = center_y + minute_radius * math.sin(angle_rad_minute)
            # end hour
            end_x_hour = center_x + hour_radius * math.cos(angle_rad_hours)
            end_y_hour = center_y + hour_radius * math.sin(angle_rad_hours)
            img = image1.copy()  # کپی تصویر پایه
            draw = ImageDraw.Draw(img)
            # second
            draw.line([(center_x, center_y),(end_x_second, end_y_second)], fill = "YELLOW",width = 3)
            # minute
            draw.line([(center_x, center_y),(end_x_minute, end_y_minute)], fill = "RED",width = 3)
            # hour
            draw.line([(center_x, center_y),(end_x_hour, end_y_hour)], fill = "BLUE",width = 3)
            im_r = img.rotate(180)
            disp.ShowImage(im_r)
        
            time.sleep(1)
    second(120,120,105 , 100 , 80)

    # draw.line([(120, 120),(176, 64)], fill = "BLUE",width = 3)
    # draw.line([(120, 120),(120 ,210)], fill = "RED",width = 3)   
    
    # im_r=image1.rotate(180)
    # disp.ShowImage(im_r)
    # time.sleep(10)
    # logging.info("show image")
    # image = Image.open('../pic/LCD_1inch28_2.jpg')	
    # im_r=image.rotate(180)
    # disp.ShowImage(im_r)
    # time.sleep(10)
    disp.module_exit()
    logging.info("quit:")
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()
