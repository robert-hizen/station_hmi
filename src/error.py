import sys
from PIL import ImageFont , Image , ImageDraw
sys.path.append('..') 
from config import config
class Error:
    def __init__(self , error_code ,conf : config.Configuration):
        self.config = conf
        self.error = error_code
        self.error_font  = ImageFont.truetype('/home/user-null/Documents/station_lcd/Font/bold.otf' , size=11)
    def error_code(self):
        # self.config.draw.text(
        #     (132,35),
        #     text=self.error,
        #     fill='#ff3838',
        #     font=self.error_font
        # )
        temp_img = Image.new("RGBA" , (120 , 120 ) , (0,0,0,0))
        temp_draw = ImageDraw.Draw(temp_img)
        temp_draw.rounded_rectangle(
            [
                (25 , 90),
                (130 , 119)
            ],
            radius=10,
            fill='#aaa69d',

        )
        temp_draw.text(
            (30,100),
            text='MFE:2131',
            fill='#f5f6fa',
            font=self.error_font
        )
        rotated_img = temp_img.rotate(-69 , expand=True).convert("RGBA")
        y_top = -24
        self.config.image.paste(rotated_img , (177 , y_top) , rotated_img)