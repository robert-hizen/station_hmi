# DONT USE A PARAMETR WITH BOTH CONSTRUCTOR AND METHOD PARAMETR (TOMORROW)
import sys
from PIL import ImageFont , Image , ImageDraw
sys.path.append('..')
from config import config
class CycleTime:
    # Initialize temp image 
    TEMP_IMAGE_CORDINATE = (120,120) 
    BACKGROUND_COLOR = (0,0,0,0)
    # Initial rounded rectangle variables
    ROUNDED_RECTANGLE_CORDINATE = [(16,80),(57,110)]
    ROUNDED_RADIUS = 30
    ROUNDED_RECTANGLE_COLOR = '#aaa69d'

    # Initial Pieslice indented cut variables
    PIESLICE_CORDNIATE = [(15,103) , (60,125)]
    PIESLICE_COLOR = '#535c68'

    # Initialize Text
    TEXT_CORDINATE = (24,90)
    TEXT_COLOR = '#f5f6fa'

    # Rotate degree and final cordinate for image
    DEGREE = 59
    FINAL_CORDINATE = ( -70 , -60)
    def __init__(self , conf : config.Configuration):
        self.config = conf
        dir = '/home/user-null/Documents/station_lcd/Font'
        self.font = ImageFont.truetype(f'{dir}/bold.otf')
    def cycle(self , cycle_txt):
        temp_img = Image.new("RGBA" , CycleTime.TEMP_IMAGE_CORDINATE , CycleTime.BACKGROUND_COLOR )
        temp_draw = ImageDraw.Draw(temp_img)

        temp_draw.rounded_rectangle(
            CycleTime.ROUNDED_RECTANGLE_CORDINATE,
            radius=CycleTime.ROUNDED_RADIUS,
            fill=CycleTime.ROUNDED_RECTANGLE_COLOR,

        )
        temp_draw.pieslice(
            CycleTime.PIESLICE_CORDNIATE,
            start=180,
            end=360,
            fill= CycleTime.PIESLICE_COLOR
        )
        temp_draw.text(
            CycleTime.TEXT_CORDINATE,
            text=f'{cycle_txt}',
            fill= CycleTime.TEXT_COLOR,
            font=self.font
        )

        rotated_img = temp_img.rotate(CycleTime.DEGREE , expand=True).convert("RGBA")

        self.config.image.paste(rotated_img , CycleTime.FINAL_CORDINATE , rotated_img)