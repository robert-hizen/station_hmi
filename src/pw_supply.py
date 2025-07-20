import sys
from PIL import Image , ImageFont , ImageDraw
sys.path.append('..')
from config import config
class PowerSupply:
    # Initialize temp image 
    TEMP_IMAGE_CORDINATE = (130,130) 
    BACKGROUND_COLOR = (0,0,0,0)
    # Initial rounded rectangle variables
    ROUNDED_RECTANGLE_CORDINATE = [(30,80),(70,120)]
    ROUNDED_RADIUS = 30
    ROUNDED_RECTANGLE_COLOR = '#aaa69d'

    # Initial Pieslice indented cut variables
    PIESLICE_CORDINATE = [(30 , 112) , (70,130)]
    PIESLICE_COLOR = '#535c68'

    # Initialize Text
    TEXT_CORDINATE = (42,96)
    TEXT_COLOR = '#f5f6fa'

    #Rotate  degree and final cordinate for image
    DEGREE = 80
    FINAL_CORDINATE = (-96 , 2)
    def __init__(self,voltage ,conf : config.Configuration):
        self.voltage = voltage
        self.config = conf
        font_directory = '/home/user-null/Documents/station_lcd/Font/'
        self.voltage_font = ImageFont.truetype(font_directory + 'bold.otf' , size=12)
    def power_supply(self):
        temp_img = Image.new("RGBA" , PowerSupply.TEMP_IMAGE_CORDINATE , PowerSupply.BACKGROUND_COLOR)
        temp_draw = ImageDraw.Draw(temp_img)

        temp_draw.rounded_rectangle(
            PowerSupply.ROUNDED_RECTANGLE_CORDINATE,
            PowerSupply.ROUNDED_RADIUS,
            PowerSupply.ROUNDED_RECTANGLE_COLOR,
        )
        temp_draw.pieslice(
            PowerSupply.PIESLICE_CORDINATE,
            start=180,
            end=360,
            fill= PowerSupply.PIESLICE_COLOR
        )
        temp_draw.text(
            PowerSupply.TEXT_CORDINATE,
            text=f'{self.voltage}V',
            fill= PowerSupply.TEXT_COLOR,
            font= self.voltage_font,
        )
        rotated_img = temp_img.rotate(PowerSupply.DEGREE,expand=True).convert("RGBA")

        self.config.image.paste(rotated_img , PowerSupply.FINAL_CORDINATE , rotated_img)
            