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
    def __init__(self , conf : config.Configuration , station_number , station_status):
        self.config = conf
        self.station_number = station_number
        self.station_status = station_status
        dir = '/home/user-null/Documents/station_lcd/Font'
        self.font_one_digit = ImageFont.truetype(f'{dir}/bold.otf' , size=115)
        self.font_two_digit = ImageFont.truetype(f'{dir}/bold.otf' , size=100)
    def st_number(self):
        # i didnt use loops for time complexity
        if 1<= self.station_number <= 9:
            self.config.draw.text(
                StationNumber.ONE_DIGIT_TEXT_CORDINATE,
                text=f'{self.station_number}',
                font=self.font_one_digit,
                fill= StationNumber.TEXT_COLOR,
            )
        elif 9 < self.station_number <= 20:
            self.config.draw.text(
                StationNumber.TWO_DIGIT_TEXT_CORDINATE,
                text=f'{self.station_number}',
                font=self.font_two_digit,
                fill=StationNumber.TEXT_COLOR
            )
        try:
            power_image = Image.open(f'template/picture/Powers/power-{self.station_status}.jpg')
            power_resized = power_image.resize(StationNumber.POWER_IMAGE_RESIZE)
            self.config.image.paste(power_resized , StationNumber.POWER_IMAGE_CORDINATE )
        except Exception as e:
            logging.error(f"Error loading image: {e}")
            self.config.module_die()
        
          