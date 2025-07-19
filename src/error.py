import sys
from PIL import ImageFont , Image , ImageDraw
sys.path.append('..') 
from config import config
class Error:
    # Initialize temp image 
    TEMP_IMAGE_CORDINATE = (130,170) 
    BACKGROUND_COLOR = (0,0,0,0)
    # Initial rounded rectangle variables
    ROUNDED_RECTANGLE_CORDINATE = [(35,130),(106,157)]
    ROUNDED_RADIUS = 30
    ROUNDED_RECTANGLE_COLOR = '#aaa69d'

    # Initial Pieslice indented cut variables
    PIESLICE_CORDNIATE = [(20,152) , (110,170)]
    PIESLICE_COLOR = '#535c68'

    # Initialize Text
    TEXT_CORDINATE = (40,135)
    TEXT_COLOR = '#f5f6fa'

    # Rotate degree and final cordinate for image
    DEGREE = -69
    FINAL_CORDINATE = (170 , -34)
    def __init__(self , error_code ,conf : config.Configuration):
        self.config = conf
        self.error = error_code
        self.error_font  = ImageFont.truetype('/home/user-null/Documents/station_lcd/Font/bold.otf' , size=14)
    def error_code(self):
    
        temp_img = Image.new("RGBA" , Error.TEMP_IMAGE_CORDINATE , Error.BACKGROUND_COLOR)
        temp_draw = ImageDraw.Draw(temp_img)

        temp_draw.rounded_rectangle(
                Error.ROUNDED_RECTANGLE_CORDINATE,
                Error.ROUNDED_RADIUS,
                fill=Error.ROUNDED_RECTANGLE_COLOR,
        )
        # using for create indented rounded rectangle
        temp_draw.pieslice(
            Error.PIESLICE_CORDNIATE,
            start=180,
            end=360,
            fill= Error.PIESLICE_COLOR
        )
        temp_draw.text(
            Error.TEXT_CORDINATE,
            text='MFE:2131',
            fill=Error.TEXT_COLOR,
            font=self.error_font
        )
        rotated_img = temp_img.rotate(Error.DEGREE , expand=True).convert("RGBA")

        self.config.image.paste(rotated_img , Error.FINAL_CORDINATE , rotated_img)
