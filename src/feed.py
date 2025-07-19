import sys
import logging
from PIL import ImageFont
sys.path.append('..')
from config import config
class Feed:
    # ON / OFF TEXT
    TEXT_ON_CORDINATE  , TEXT_OFF_CORDINATE= (140,5) , (140,5)
    COLOR_OFF , COLOR_ON = '#e74c3c' , '#2ecc71'

    # Arc Init variables
    ARC_COLOR = '#7f8c8d'
    ARC_WIDTH = 2
    def __init__(self , state, conf : config.Configuration):
        self.config = conf
        self.state = state
    def feed_state(self):
        feed_font = ImageFont.truetype('/home/user-null/Documents/station_lcd/Font/bold.otf' , size=30)
        circle_bound = (135 , 4 , 162 , 30) # (left , top , right , bottom)
        try:
            if self.state == 'on':
                self.config.draw.text(
                    Feed.TEXT_ON_CORDINATE,
                    text="F",
                    fill= Feed.COLOR_ON,
                    font= feed_font
                )
            elif self.state in 'off':
                self.config.draw.text(
                    Feed.TEXT_OFF_CORDINATE,
                    text='F',
                    fill= Feed.COLOR_OFF,
                    font=feed_font                    
                )
            else:
                raise ValueError(f'Invalid state: {self.state}')
            self.config.draw.arc(
                circle_bound,
                start=0,
                end=360,
                fill= Feed.ARC_COLOR,
                width= Feed.ARC_WIDTH
            )
        except ValueError as e:
            logging.error(f'Undifiend state : {e}')
            self.config.module_die()
