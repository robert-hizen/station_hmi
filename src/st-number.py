import sys
import logging
sys.path.append('..')
from config import config
class StationNumber:
    def __init__(self , conf):
        self.config = conf
    def st_number(self , num):
        for i in range(1,10):
            if i == num:
                pass