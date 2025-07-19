import sys
from PIL import ImageFont , Image , ImageDraw
sys.path.append('..') 
from config import config
class Error:
    def __init__(self , error_code ,conf : config.Configuration):
        self.config = conf
        self.error = error_code
        self.error_font  = ImageFont.truetype('/home/user-null/Documents/station_lcd/Font/bold.otf' , size=14)
    def error_code(self):
    
        temp_img = Image.new("RGBA" , (130 , 170 ) , (0,0,0,0))
        temp_draw = ImageDraw.Draw(temp_img)
        # we use a rounded rectangle for draw a rectangle
        temp_draw.rounded_rectangle(
                [  
                    # first cordinate for move x horizontally and second cordinate use to move rectangle vertically
                   (19 , 130),
                   (114 , 170)
                ],

                radius=30,
                fill='#aaa69d',
        )
        # using for create indented rounded rectangle
        temp_draw.pieslice(
            [
                (20,160),
                (110,180)
            ],
            start=180,
            end=360,
            fill='#535c68'
        )
        temp_draw.text(
            (34,135),
            text='MFE:2131',
            fill='#f5f6fa',
            font=self.error_font
        )
        print(temp_img.size)
        rotated_img = temp_img.rotate(-69 , expand=True).convert("RGBA")
        y_top = -34
        self.config.image.paste(rotated_img , (170 , y_top) , rotated_img)
        print(rotated_img.size)
        self.config.image.save("Output.png")