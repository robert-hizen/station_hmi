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
        
        temp_draw.rounded_rectangle(
                [  (20 , 40),
                   (120 , 170)
                ],  
                radius=10,
                fill='#aaa69d',
        )
        temp_draw.pieslice(
            [
                (20,160),
                (130,180)
            ],
            start=180,
            end=360,
            fill='#535c68'
        )
        temp_draw.text(
            (30,140),
            text='MFE:2131',
            fill='#f5f6fa',
            font=self.error_font
        )
        # -69
        print(temp_img.size)
        rotated_img = temp_img.rotate(-69 , expand=True).convert("RGBA")
        y_top = -34
        self.config.image.paste(rotated_img , (177 , y_top) , rotated_img)
        print(rotated_img.size)
        self.config.image.save("Output.png")
    # def create_pieslice(self):
    #     if self.config.image is None:
    #         print("It is a none value.")
    #     temp_img = Image.new("RGBA" , (320 , 240 ) , (0,0,0,0))
    #     temp_draw = ImageDraw.Draw(temp_img)
    #     temp_draw.pieslice(
    #         [(100,60),(200  ,140)],
    #         start=180,
    #         end=360,
    #         fill= '#FFFFFF'
    #     )
    #     rotated = temp_img.rotate(-45 , expand=True)
    #     self.config.image.paste(rotated , (0,0) , rotated)
    #     self.config.image.save('rotated_pieslice.png')