import sys
from PIL import Image , ImageDraw , ImageFont
sys.path.append('../')
from config import config
class Bg:
    def __init__(self , conf : config.Configuration):
        self.config = conf
    def background_color(self):
        # create a rectangle for partition lcd [x0 , y0 => x1 , y1]
        self.config.draw.rectangle(
        [0, 0, self.config.width, self.config.height // 2],
        fill='#535c68'
        )
        self.config.draw.rectangle(
            [0, self.config.height // 2, self.config.width, self.config.height],
            fill='#f7f1e3'
        )