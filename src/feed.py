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
        feed_font = ImageFont.truetype('/home/user-null/Documents/station_lcd/Font/bold.otf' , size=40)
        circle_bound = (148 , 15 , 187 , 60)         # (left , top , right , bottom)
        try:
            if self.state == 'on':
                self.config.draw.text(
                    (155 , 20),
                    text="F",
                    fill= '#2ecc71',
                    font= feed_font
                )
            elif self.state in 'off':
                self.config.draw.text(
                    (155,20),
                    text='F',
                    fill='#e74c3c',
                    font=feed_font                    
                )
            else:
                raise ValueError(f'Invalid state: {self.state}')
            self.config.draw.arc(
                circle_bound,
                start=0,
                end=360,
                fill='#7f8c8d',
                width=2
            )
        except ValueError as e:
            logging.error(f'Undifiend state : {e}')
            self.config.module_die()


        # img = Image.open(f'template/picture/Powers/power-{self.state}.jpg') 
        # self.config.image.paste(img , (185 , 63))