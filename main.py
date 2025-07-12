from config import config
from src import bg
from src import st_number
from src import status
from src import error
from src import pw_supply 
from src import feed 
from src import web_cams
from src import network
from src import arduino
import logging
if __name__ == '__main__':
    conf = config.Configuration()
    back_fround_color = bg.Bg(conf)
    station_number = st_number.StationNumber(conf)
    status_value = status.Status(conf)
    error_state = error.Error('1234',conf)
    power_supply_instance = pw_supply.PowerSupply(5 , conf)
    feed_instance = feed.Feed('on',conf)
    web_cam = web_cams.Cams( 'connect' , conf)
    network_connection = network.Network(conf)
    arduino_ctrl = arduino.Arduino(conf , None)
    try:
        # configure our display
        conf.init_display()
        back_fround_color.background_color()
        station_number.st_number(3 , 'off')
        error_state.error_code()
        status_value.rounded_rectangle('warning')
        status_value.circle()
        status_value.Status_logo_message('warning','warning' , 'Dosing Error!')
        power_supply_instance.power_supply()
        feed_instance.feed_state()
        web_cam.web_cams()
        network_connection.connection()
        arduino_ctrl.arduino_connection()
        conf.show_image()
    except Exception  as e:
        logging.error(f"Error : {e}")
        conf.module_die