import sys
from PIL import ImageFont
sys.path.append('..') 
from config import config
class Error:
    def __init__(self , error_code ,conf : config.Configuration):
        self.config = conf
        self.error = error_code
        self.error_font  = ImageFont.truetype('/home/user-null/Documents/station_lcd/Font/bold.otf' , size=22)
    def error_code(self):
        self.config.draw.text(
            (67,35),
            text='Error: ',
            fill='#f5f6fa',
            font=self.error_font
        )
        self.config.draw.text(
            (132,35),
            text=self.error,
            fill='#ff3838',
            font=self.error_font
        )