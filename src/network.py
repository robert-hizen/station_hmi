import sys
import logging
import time
from PIL import Image
sys.path.append('..')
from config import config
class Network:
    X_CORDINATE = 95
    Y_CORDINATE = 165
    def __init__(self ,conf : config.Configuration , connection_status = None):
        self.config =  conf
        self.conn_status = connection_status
        self.dir  = '/home/user-null/Documents/station_lcd/template/picture/network'
    def connection(self):
        try:
            try: 
                if self.conn_status is None:
                    while True:
                        img = Image.open(f'{self.dir}/no_con.jpg')
                        self.config.image.paste(img, (Network.X_CORDINATE,Network.Y_CORDINATE))
                        self.config.disp.ShowImage(self.config.image.rotate(180))
                        time.sleep(0.5)

                        clear_img = Image.new("RGB" , (img.width , img.height) , '#f7f1e3')
                        self.config.image.paste(clear_img , (Network.X_CORDINATE , Network.Y_CORDINATE))
                        self.config.disp.ShowImage(self.config.image.rotate(180))
                        time.sleep(0.5)
                elif self.conn_status == 'weak':
                    img = Image.open(f'{self.dir}/weak_con.jpg')
            except ValueError as e:
                pass
        except Exception as e:
            logging.error(f'Unable to load image : {e}')