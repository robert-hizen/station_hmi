import sys
import logging
from PIL import Image
sys.path.append('..')
from config import config
class CopyRight:
    X_CORDINATE = 110
    Y_CORDINATE = 210
    def __init__(self , conf : config.Configuration):
        self.config = conf
        self.dir = '/home/user-null/Documents/station_lcd/template/picture'
    def pooyesh_machine_logo(self):
        img = Image.open(f'{self.dir}/pooyesh_machine.jpg')
        self.config.image.paste(img , (CopyRight.X_CORDINATE , CopyRight.Y_CORDINATE))
