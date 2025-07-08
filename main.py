from config import config
from src import bg
import logging
if __name__ == '__main__':
    conf = config.Configuration()
    back_fround_color = bg.Bg(conf)
    try:
        # configure our display
        conf.init_display()
        back_fround_color.background_color()
        conf.show_image()
    except Exception as e:
        logging.error(f"Error : {e}")
        conf.module_die