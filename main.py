from config import config
from src import bg
from src import st_number
import logging
if __name__ == '__main__':
    conf = config.Configuration()
    back_fround_color = bg.Bg(conf)
    station_number = st_number.StationNumber(conf)
    try:
        # configure our display
        conf.init_display()
        back_fround_color.background_color()
        station_number.st_number(9)
        conf.show_image()
    except Exception as e:
        logging.error(f"Error : {e}")
        conf.module_die