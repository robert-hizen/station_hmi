import time
import threading
import logging
from PIL import Image
from config import config

class Arduino:
    X_CORDINATE = 30
    Y_CORDINATE = 40

    def __init__(self, conf: config.Configuration, status=None):
        self.config = conf
        self.status = status  # None یا 'on'
        self.dir = '/home/user-null/Documents/station_lcd/template/picture/arduino'
        self.last_blink_time = time.time()
        self.blink_state = False

        self.img_on = Image.open(f'{self.dir}/arduino.jpg').convert("RGBA")
        self.clear_img = Image.new("RGBA", self.img_on.size, (0, 0, 0, 0))
        self.current_image = self.clear_img.copy()

    def update(self):
        now = time.time()
        if self.status is None:
            if now - self.last_blink_time > 0.3:
                self.blink_state = not self.blink_state
                self.last_blink_time = now
            self.current_image = self.img_on if self.blink_state else self.clear_img
        elif self.status == 'on':
            self.current_image = self.img_on

    def update_status(self, new_status):
        if new_status != self.status:
            self.status = new_status
