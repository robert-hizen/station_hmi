import sys
import logging
from PIL import ImageFont , Image , ImageDraw
sys.path.append('..')
from config import config
class CycleTime:
    def __init__(self , conf : config.Configuration):
        self.config = conf
        dir = '/home/user-null/Documents/station_lcd/Font'
        self.font = ImageFont.truetype(f'{dir}/bold.otf')
    def cycle(self , cycle_txt):
        temp_img = Image.new("RGBA" , (120,120) , (0,0,0,0))
        temp_draw = ImageDraw.Draw(temp_img)

        temp_draw.pieslice(
            [
                (30 , 80),
                (70 , 100)
            ],
            start=0,
            end=360,
            fill='#aaa69d',
            outline='#aaa69d'

        )
        temp_draw.text(
            (40,85),
            text=f'{cycle_txt}',
            fill='#f5f6fa',
            font=self.font
        )

        rotated_img = temp_img.rotate(45 , expand=True).convert("RGBA")

        y_top = -55
        self.config.image.paste(rotated_img , ( -70 , y_top) , rotated_img)