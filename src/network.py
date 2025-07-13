import time
import threading
import logging
from PIL import Image
from config import config

class Network:
    X_CORDINATE = 90
    Y_CORDINATE = 60

    def __init__(self, conf: config.Configuration, status=None):
        self.config = conf
        self.status = status  # None یا 'best'
        self.dir = '/home/user-null/Documents/station_lcd/template/picture/network'
        self.last_blink_time = time.time()
        self.blink_state = False

        self.img_best = Image.open(f'{self.dir}/best_con.jpg').convert("RGBA")
        self.img_no_con = Image.open(f'{self.dir}/no_con.jpg').convert("RGBA")
        self.clear_img = Image.new("RGBA", self.img_no_con.size, (0, 0, 0, 0))
        self.current_image = self.clear_img.copy()

    def update(self):
        now = time.time()
        if self.status is None:
            # چشمک زدن برای حالت no connection
            if now - self.last_blink_time > 0.3:
                self.blink_state = not self.blink_state
                self.last_blink_time = now
            self.current_image = self.img_no_con if self.blink_state else self.clear_img
        elif self.status == 'best':
            # تصویر ثابت برای حالت best
            self.current_image = self.img_best

    def update_status(self, new_status):
        if new_status != self.status:
            self.status = new_status
