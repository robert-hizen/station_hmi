import sys
from PIL import Image , ImageFont , ImageDraw
sys.path.append('..')
from config import config
class PowerSupply:
    def __init__(self,voltage ,conf : config.Configuration):
        self.voltage = voltage
        self.config = conf
        font_directory = '/home/user-null/Documents/station_lcd/Font/'
        self.voltage_font = ImageFont.truetype(font_directory + 'bold.otf' , size=20)
    def power_supply(self):
        # power_image = Image.open('template/picture/Powers/power-supply.jpg')
        # self.config.image.paste(power_image , (55,60))
        # seprator_line = Image.open('template/picture/vertical_line/line.jpg') 
        # self.config.image.paste(seprator_line , (113,63))
        temp_img = Image.new("RGBA" , (150,1) , (0,0,0,0))
        temp_draw = ImageDraw.Draw(temp_img)

        temp_draw.rounded_rectangle(
            [
                (30 , 90),
                (70 , 119)
            ],
            radius=10,
            fill= '#aaa69d'
        )
        temp_draw.text(
            (35,95),
            text=f'{self.voltage}V',
            fill='#f7f1e3',
            font= self.voltage_font,
        )
        rotated_img = temp_img.rotate(0,expand=True).convert("RGBA")

        self.config.image.paste(rotated_img , (100,1) , rotated_img)
            