import sys
import logging
from PIL import Image , ImageFont
sys.path.append('..')
from config import config
class Feed:
    def __init__(self , state, conf : config.Configuration):
        self.config = conf
        self.state = state
    def feed_state(self):
        feed_font = ImageFont.truetype('/home/user-null/Documents/station_lcd/Font/bold.otf' , size=35)
        if self.state == 'on':
            self.config.draw.text(
                (150 , 20),
                text="F",
                fill= '#2ecc71',
                font= feed_font
            )
        elif self.state == 'off':
            self.config.draw.text(
                (150,20),
                text='F',
                fill='#e74c3c',
                font=feed_font
            )
        circle_bounds = (142, 13, 180, 56) # (left , top , right , bottom)
        self.config.draw.arc(
            circle_bounds,
            start=0,
            end=360,
            fill='#7f8c8d',
            width=3
        )
        # img = Image.open(f'template/picture/Powers/power-{self.state}.jpg') 
        # self.config.image.paste(img , (185 , 63))