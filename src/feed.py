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
        feed_font = ImageFont.truetype('/home/user-null/Documents/station_lcd/Font/bold.otf' , size=20)
        self.config.draw.text(
            (125 , 63),
            text="Feed: ",
            fill= '#f7f1e3',
            font= feed_font
        )
        img = Image.open(f'template/picture/Powers/power-{self.state}.jpg') 
        self.config.image.paste(img , (185 , 63))