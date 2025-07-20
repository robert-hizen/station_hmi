import sys
import time
from PIL import Image
sys.path.append('..')
from config import config

class DosingWebCam:
    X_CORDINATE = 181
    Y_CORDINATE = 26
    BLINKER_TIME = 0.3
    TEMP_IMAGE_COLOR = (0,0,0,0)

    def __init__(self, connection_status, conf: config.Configuration):
        self.config = conf
        self.connection = connection_status
        self.dir = '/home/user-null/Documents/station_lcd/template/picture/Icons'
        self.last_blink_time = time.time()
        self.blink_state = False

        self.img_on = Image.open(f'{self.dir}/web_cams.jpg').convert("RGBA")
        self.clear_img = Image.new("RGBA", self.img_on.size, DosingWebCam.TEMP_IMAGE_COLOR)
        self.current_image = self.clear_img.copy()

    def update(self):
        '''Blink or non-Blink Icon with on/off Conditions'''
        now = time.time()
        if self.connection == 'off':
            if now - self.last_blink_time > DosingWebCam.BLINKER_TIME:
                self.blink_state = not self.blink_state
                self.last_blink_time = now

            self.current_image = self.img_on if self.blink_state else self.clear_img

        elif self.connection == 'on':
            self.current_image = self.img_on

    def update_connection(self, new_status):
        self.connection = new_status
