import time
import sys
import os
import logging
import spidev as SPI
import math
sys.path.append('..')

from lib import LCD_1inch28
from PIL import Image, ImageDraw, ImageFont
# Raspberry Pi pin configuration
RST = 27
DC = 25
BL = 18
BUS = 0 
DEVICE = 0

logging.basicConfig(level=logging.DEBUG)


# Initial Lines Data
CENTER_X = 120
CENTER_Y = 120
INNER_RADIUS = 80
OUTER_RADIUS = 118
class Configuration:
    def __init__(self):
        # Initialize display
        self.disp = LCD_1inch28.LCD_1inch28()
        self.width = self.disp.width
        self.height = self.disp.height
        self.image = Image.new("RGB", (self.width, self.height), "#2C3E50")
        self.draw = ImageDraw.Draw(self.image)

    def init_display(self):
        self.disp.Init()
        self.disp.clear()
        self.disp.bl_DutyCycle(50)

    def show_image(self):
        im_r = self.image.rotate(180)
        self.disp.ShowImage(im_r)
        time.sleep(1000)

    def module_die(self):
        self.disp.module_exit()
        logging.info("Quit.")

class Ui:
    def __init__(self, config: Configuration):
        self.config = config

    def draw_circle(self):
        logging.info("Draw Circle")
        inner_offset = 42
        for  i in range(3):
            p = inner_offset + i
            self.config.draw.arc(
                (p , p , self.config.width - p , self.config.height - p),
                0 , 360 , fill='#9B59B6'
            )
    def draw_button(self):
        self.font1 = ImageFont.truetype('../Font/Font00.ttf' , size=29)
        self.font2 = ImageFont.truetype('../Font/Font00.ttf' , size=20)
        font3 = ImageFont.truetype('../Font/Font02.ttf')
        # width , height = self.font1.getsize("Home")
        # print(width , height)
        self.config.draw.rectangle(
            [(3,105),(42,135)],
            'WHITE',
            None,
            1 
        )
        self.config.draw.text(([3,100]) , "<=" , fill="BLACK" , font=self.font1)
        self.config.draw.rectangle(
           [(241 , 105) , (195,135)],
           'WHITE',
           None,
           1 
        )
        self.config.draw.text(([200,100]) , "=>" , fill="BLACK" , font=self.font1)
    def partition_lines(self, center_x, center_y, inner_radius, outer_radius):
        degree = -135
        partition_id = 0

        self.center_x = center_x
        self.center_y = center_y
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius

        partition_actions = {
            0: self.action_partition_zero,
            # 1: self.action_partition_one,
            # 2: self.action_partition_two,
            # 3: self.action_partition_three
        }

        while degree <= 180:
            radian = math.radians(degree)

            start_x = center_x + inner_radius * math.cos(radian)
            start_y = center_y + inner_radius * math.sin(radian)
            end_x = center_x + outer_radius * math.cos(radian)
            end_y = center_y + outer_radius * math.sin(radian)

            # جلوگیری از خطوط روی دکمه‌ها
            if not self._is_near_button(start_x, start_y, end_x, end_y):
                self.config.draw.line([(start_x, start_y), (end_x, end_y)], fill='#ffffff', width=1)
                print(f'Degree: {degree} | Start: ({start_x:.2f}, {start_y:.2f}) | End: ({end_x:.2f}, {end_y:.2f})')

            # اجرای اکشن برای پارتیشن خاص
            if partition_id in partition_actions:
                partition_actions[partition_id](radian)

            degree += 45
            partition_id += 1

    def _is_near_button(self, start_x, start_y, end_x, end_y):
        near_left = abs(start_x - 40) < 5 and abs(start_y - 120) < 5
        near_right = abs(start_x - 200) < 5 and abs(start_y - 120) < 5
        return near_left or near_right
    def back_ground(self ,start_angle , end_angle , bg_color = None):
        if bg_color is None:
            raise ValueError("bg_color parametr has been required")
        try:
            self.config.draw.pieslice(
                (self.center_x - self.outer_radius, self.center_y - self.outer_radius,
                self.center_x + self.outer_radius, self.center_y + self.outer_radius),
                start_angle,
                end_angle,
                fill= bg_color
            )
            self.config.draw.pieslice(
                (self.center_x - self.inner_radius, self.center_y - self.inner_radius,
                self.center_x + self.inner_radius, self.center_y + self.inner_radius),
                start_angle,
                end_angle,
                fill='#2C3E50'  
            )
            self.implement_text(text='HIII' , fill='000000' , font=self.font2)
        except TypeError as e:
            if bg_color is None:
                logging.error("Error : Missing required argument.")
    def action_partition_zero(self, radian):
        middle_radius = (self.inner_radius + self.outer_radius) / 2
        self.middle_x = self.center_x + middle_radius * math.cos(radian)
        self.middle_y = self.center_y + middle_radius * math.sin(radian)

        self.back_ground(start_angle=-135 , end_angle=-90 , bg_color='#E53935')
        # w = int(abs(middle_x - self.center_x) * 2)
        # h = int(abs(middle_y - self.center_y) * 2)
        # self.image = Image.new("RGB", (w, h), "#427435")
        
        
    def implement_text(self, text , fill  , font):
        self.config.draw.text(
            (self.middle_x - 33, self.middle_y + 15),
            f"{text}",
            fill=f"#{fill}",
            font=font
        )


             
        
try:
    
    conf = Configuration()
    conf.init_display()

    ui = Ui(conf)
    ui.draw_circle()
    ui.draw_button()
    ui.partition_lines(CENTER_X , CENTER_Y , INNER_RADIUS , OUTER_RADIUS)
    conf.show_image()
    conf.module_die()

except (KeyboardInterrupt, IOError) as e:
    logging.error(e)
