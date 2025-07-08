from conf import config
import logging
if __name__ == '__main__':
    conf1 = config.Configuration()
    try:
        # configure our display
        conf1.init_display()
        conf1.show_image()
    except Exception as e:
        logging.error(f"Error : {e}")
        conf1.module_die