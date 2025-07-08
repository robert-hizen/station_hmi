import sys
import logging
from PIL import Image , ImageDraw , ImageFont
sys.path.append('..')
from config import config
class StationNumber:
    def __init__(self , conf : config.Configuration):
        self.config = conf
    def st_number(self , num):
        # i didnt use loops for time complexity
        if not (1<= num <= 9):
            logging.error("Invalid station number")
        try:
            # canvas = Image.new("RGB", (240, 240), "#2C3E50")  # یا "#000000" برای مشکی
            img = Image.open(f'template/picture/{num}-solid.jpg').convert("RGB")
            self.config.image.paste(img , (120,8))
        except Exception as e:
            logging.error(f"Error loading image: {e}")
          