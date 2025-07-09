import sys
import logging
from PIL import Image
sys.path.append('..')
from config import config
class StationNumber:
    def __init__(self , conf : config.Configuration):
        self.config = conf
    def st_number(self , num , state):
        # i didnt use loops for time complexity
        if not (1<= num <= 9):
            logging.error("Invalid station number")
            self.config.module_die()
        try:
            # canvas = Image.new("RGB", (240, 240), "#2C3E50")
            img = Image.open(f'template/picture/{num}-solid.jpg').convert("RGB")
            power_image = Image.open(f'template/picture/Powers/power-{state}.jpg')
            self.config.image.paste(img , (90,8))
            self.config.image.paste(power_image , (120,8) )
        except Exception as e:
            logging.error(f"Error loading image: {e}")
            self.config.module_die()
        # if state != ('on') or state != 'off':
        #         raise ValueError("PLease enter a valid state.")
        
          