import sys
import logging
sys.path.append('..')
from config import config
class Status:
    RECTANGLE_CORDINATE = [(0,121) , (240,240)]

    # Initialize Erro rectangle handler
    ERROR_RECTANGLE_COLOR = '#ff4d4d'
    # Initialize Erro rectangle handler
    WARNING_RECTANGLE_COLOR = '#ff9f1a'

    # Initialize Text
    TEXT_CORDINATE = (30,135)
    TEXT_COLOR = '#f7f1e3'
    def __init__(self , conf : config.Configuration , status , error_text):
        self.config = conf
        self.status = status
        self.error_text = error_text
    def rounded_rectangle(self):
        '''Create a rectangle in bottom half circle'''
        if self.status == 'error':
            self.config.draw.rectangle(
                Status.RECTANGLE_CORDINATE,
                Status.ERROR_RECTANGLE_COLOR  
        )
        elif self.status == 'warning':
            self.config.draw.rectangle(
                Status.RECTANGLE_CORDINATE,
                Status.WARNING_RECTANGLE_COLOR  
        )   
        else :
            logging.error("Please enter valid status")
            self.config.module_die()
    @staticmethod
    def wrap_text(text , line_lenght = 17):
        '''For Wrap a text for prevent our text placement out of lcd range'''
        return '\n'.join([text[i:i+line_lenght] for i in range(0,len(text) , line_lenght)])
    def Status_logo_message(self):

        wrapped_text = self.wrap_text(self.error_text , line_lenght= 17 )
        error_font = self.config.big_bold_font
        self.config.draw.text(
            Status.TEXT_CORDINATE,
            text=wrapped_text,
            fill= Status.TEXT_COLOR,
            font= error_font
        )