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

        temp_draw.rounded_rectangle(
            [
                (16 , 80),
                (57, 110)
            ],
            radius=30,
            fill='#aaa69d',

        )
        temp_draw.pieslice(
            [(15,105),(60,125)],
            start=180,
            end=360,
            fill= '#535c68'
        )
        temp_draw.text(
            (24,90),
            text=f'{cycle_txt}',
            fill='#f5f6fa',
            font=self.font
        )

        rotated_img = temp_img.rotate(59 , expand=True).convert("RGBA")

        y_top = -60
        self.config.image.paste(rotated_img , ( -70 , y_top) , rotated_img)