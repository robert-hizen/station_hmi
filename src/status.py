import sys
import logging
sys.path.append('..')
from config import config
from PIL import Image
class Status:
    def __init__(self , conf : config.Configuration):
        self.config = conf
    def rounded_rectangle(self , status):
        if status == 'error':
            self.config.draw.rounded_rectangle(
                [(17 , 121) , (223 , 210)],
                radius=50,
                fill= '#ff4d4d'  
        )
        elif status == 'warning':
            self.config.draw.rounded_rectangle(
                [(17 , 121) , (223 , 210)],
                radius=50,
                fill= '#ff9f1a'  
        )   
        else :
            logging.error("Please enter valid status")
            self.config.module_die()
    def circle(self):
        self.config.draw.arc(
            [(30,95) ,(100,150)],
            start= 0,
            end=360,
            fill='#f7f1e3',
            width=3  
        )
    @staticmethod
    def wrap_text(text , line_lenght = 13):
        return '\n'.join([text[i:i+line_lenght] for i in range(0,len(text) , line_lenght)])
    def Status_logo_message(self ,txt ,status , error_text):
        font = self.config.bold_font
        self.config.draw.text(
            (42 ,128),
            text= txt,
            fill= '#4b4b4b',
            font= font
        )
        # error_img = Image.open(f'template/picture/warning_error/{status}.jpg')
        # self.config.image.paste(error_img , (55 , 100))

        wrapped_text = self.wrap_text(error_text , line_lenght= 13 )
        error_font = self.config.big_bold_font
        self.config.draw.text(
            (105 , 92),
            text=wrapped_text,
            fill= '#f7f1e3',
            font= error_font
        )