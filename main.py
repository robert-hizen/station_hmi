from config import config
from src import bg
from src import st_number
from src import status
import logging
if __name__ == '__main__':
    conf = config.Configuration()
    back_fround_color = bg.Bg(conf)
    station_number = st_number.StationNumber(conf)
    status_value = status.Status(conf)
    try:
        # configure our display
        conf.init_display()
        back_fround_color.background_color()
        station_number.st_number(3 , 'off')
        status_value.rounded_rectangle('warning')
        status_value.circle()
        status_value.Status_logo_message('warning','warning' , 'Dosing Error!')
        conf.show_image()
    except Exception as e:
        logging.error(f"Error : {e}")
        conf.module_die