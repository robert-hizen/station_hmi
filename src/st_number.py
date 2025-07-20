import sys
import logging
from PIL import Image , ImageFont
sys.path.append('..')
from config import config
class StationNumber:
    # One Digit text handler
    ONE_DIGIT_TEXT_CORDINATE = (85,25)
    TEXT_COLOR = '#ffffff'
    TWO_DIGIT_TEXT_CORDINATE = (67,30)

    # Power image handler
    POWER_IMAGE_RESIZE = (20,20)
    POWER_IMAGE_CORDINATE = (79,7)
    def __init__(self , conf : config.Configuration):
        self.config = conf
        dir = '/home/user-null/Documents/station_lcd/Font'
        self.font_one_digit = ImageFont.truetype(f'{dir}/bold.otf' , size=115)
        self.font_two_digit = ImageFont.truetype(f'{dir}/bold.otf' , size=100)
    def st_number(self , num , state):
        # i didnt use loops for time complexity
        if 1<= num <= 9:
            self.config.draw.text(
                StationNumber.ONE_DIGIT_TEXT_CORDINATE,
                text=f'{num}',
                font=self.font_one_digit,
                fill= StationNumber.TEXT_COLOR,
            )
        elif 9 < num <= 20:
            self.config.draw.text(
                StationNumber.TWO_DIGIT_TEXT_CORDINATE,
                text=f'{num}',
                font=self.font_two_digit,
                fill=StationNumber.TEXT_COLOR
            )
        try:
            power_image = Image.open(f'template/picture/Powers/power-{state}.jpg')
            power_resized = power_image.resize(StationNumber.POWER_IMAGE_RESIZE)
            self.config.image.paste(power_resized , StationNumber.POWER_IMAGE_CORDINATE )
        except Exception as e:
            logging.error(f"Error loading image: {e}")
            self.config.module_die()
        
          