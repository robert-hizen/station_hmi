import sys
import logging
from PIL import ImageFont
sys.path.append('..')
from config import config
class CycleTime:
    def __init__(self , conf : config.Configuration):
        self.config = conf
        dir = '/home/user-null/Documents/station_lcd/Font'
        self.font = ImageFont.truetype(f'{dir}/bold.otf')
    def cycle(self , cycle_txt):
        self.config.draw.rounded_rectangle(
            [
                (145 , 90),
                (200 , 119)
            ],
            radius=10,
            fill='#aaa69d',

        )
        self.config.draw.text(
            (155,100),
            text=f'{cycle_txt}',
            fill='#f5f6fa',
            font=self.font
        )