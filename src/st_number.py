import sys
import logging
from PIL import Image , ImageFont
sys.path.append('..')
from config import config
class StationNumber:
    def __init__(self , conf : config.Configuration):
        self.config = conf
        dir = '/home/user-null/Documents/station_lcd/Font'
        self.font_one_digit = ImageFont.truetype(f'{dir}/bold.otf' , size=115)
        self.font_two_digit = ImageFont.truetype(f'{dir}/bold.otf' , size=100)
    def st_number(self , num , state):
        # i didnt use loops for time complexity
        if 1<= num <= 9:
            self.config.draw.text(
                (85,25),
                text=f'{num}',
                font=self.font_one_digit,
                fill='#FFFFFF'
            )
        elif 9 < num <= 20:
            self.config.draw.text(
                (67,30),
                text=f'{num}',
                font=self.font_two_digit,
                fill='#ffffff'
            )
        try:
        #     # img = Image.open(f'template/picture/{num}-solid.jpg').convert("RGB")
            power_image = Image.open(f'template/picture/Powers/power-{state}.jpg')
        #     # img_resized = img.resize((80 ,80))
            power_resized = power_image.resize((20,20))
        #     # self.config.image.paste(img_resized , (80,35))
            self.config.image.paste(power_resized , (79,7) )
        except Exception as e:
            logging.error(f"Error loading image: {e}")
            self.config.module_die()
        
          