import sys
import time
import sys
from PIL import Image
sys.path.append('..')
from config import config
class Arduino:
    X_CORDINATE = 100
    Y_CORDIANATE = 165
    def __init__(self ,conf : config.Configuration , status = None):
        self.config = conf
        self.arduino_state = status
        self.dir = '/home/user-null/Documents/station_lcd/template/picture/arduino'
    def arduino_connection(self):
        img = Image.open(f'{self.dir}/arduino.jpg')
        if self.arduino_state is None:
            self.config.image.paste(img , (Arduino.X_CORDINATE , Arduino.Y_CORDIANATE))

            # while True:
            #     self.config.disp.ShowImage(self.config.image.rotate(180))
            #     time.sleep(0.5)

            #     clear_img = Image.new("RGB" , (img.width , img.height) , '#f7f1e3')
            #     self.config.image.paste(clear_img , (Arduino.X_CORDINATE , Arduino.Y_CORDIANATE))
            #     self.config.disp.ShowImage(self.config.image.rotate(180))
            #     time.sleep(0.5)
                # self.config.disp.ShowImage(self)