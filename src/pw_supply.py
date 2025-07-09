import sys
from PIL import Image , ImageFont
sys.path.append('..')
from config import config
class PowerSupply:
    def __init__(self,voltage ,conf : config.Configuration):
        self.voltage = voltage
        self.config = conf
        font_directory = '/home/user-null/Documents/station_lcd/Font/'
        self.voltage_font = ImageFont.truetype(font_directory + 'bold.otf' , size=20)
    def power_supply(self):
        power_image = Image.open('template/picture/Powers/power-supply.jpg')
        self.config.image.paste(power_image , (55,60))
        self.config.draw.text(
            (75,63),
            text=f' :{self.voltage}V',
            fill='#f7f1e3',
            font= self.voltage_font,
        )
        seprator_line = Image.open('template/picture/vertical_line/line.jpg') 
        self.config.image.paste(seprator_line , (112,63))

            