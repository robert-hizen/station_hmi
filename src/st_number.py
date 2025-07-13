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
            img = Image.open(f'template/picture/{num}-solid.jpg').convert("RGB")
            power_image = Image.open(f'template/picture/Powers/power-{state}.jpg')
            img_resized = img.resize((40,40))
            power_resized = power_image.resize((30,30))
            self.config.image.paste(img_resized , (100,35))
            self.config.image.paste(power_resized , (55,35) )
        except Exception as e:
            logging.error(f"Error loading image: {e}")
            self.config.module_die()
        
          