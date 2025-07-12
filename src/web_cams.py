import sys
import time
import logging
from PIL import Image
sys.path.append('..')
from config import config
class  Cams:
    def __init__(self , con , conf : config.Configuration):
        self.config = conf
        self.dir  = '/home/user-null/Documents/station_lcd/template/picture'
        self.connection = con
    def web_cams(self):
        try:
            img = Image.open(self.dir + '/Icons/web_cams.jpg')
            try:
                if self.connection == 'connect':
                    self.config.image.paste(img , (40 , 165))
                    return
                elif self.connection == 'disconnect':                
                    while True:
                        self.config.image.paste(img , (40 , 165))
                        self.config.disp.ShowImage(self.config.image.rotate(180))
                        time.sleep(0.5)
                        
                        clear_img = Image.new("RGB" , (img.width , img.height) , '#f7f1e3')
                        self.config.image.paste(clear_img , (40,165))
                        self.config.disp.ShowImage(self.config.image.rotate(180))
                        time.sleep(0.5)
            except ValueError as e:
                    logging.error(f'Invalid status {e}')
        except Exception as e:
            print(f'Error loading image : {e}')