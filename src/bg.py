import sys
sys.path.append('../')
from config import config
class Bg:
    X_ZERO_CORDINATE = 0
    Y_ZERO_CORDINATE = 0
    def __init__(self , conf : config.Configuration):
        self.config = conf
    def background_color(self):
        # Create a half Circle with background color <#535c68>
        X_ONE_CORDINATE = self.config.width
        Y_ONE_CORDINATE = self.config.height
        self.config.draw.rectangle(
        [Bg.X_ZERO_CORDINATE, Bg.Y_ZERO_CORDINATE, X_ONE_CORDINATE, Y_ONE_CORDINATE],
        fill='#535c68'
        )