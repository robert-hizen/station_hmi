import time
import threading
from config import config
from src import error, bg , st_number , status , pw_supply , feed , web_cams , network , arduino
import logging
from PIL import Image
def render_loop(conf , web_cam , network , arduino , static_background):
    while True:
        web_cam.update()
        network.update()
        arduino.update()

        base_temp = static_background.copy()
        base_temp.paste(web_cam.current_image , (web_cam.X_CORDINATE , web_cam.Y_CORDINATE) , web_cam.current_image )
        base_temp.paste(network.current_image , (network.X_CORDINATE , network.Y_CORDINATE) , network.current_image )
        base_temp.paste(arduino.current_image , (arduino.X_CORDINATE , arduino.Y_CORDINATE) , arduino.current_image )
        conf.disp.ShowImage(base_temp.rotate(180))
        time.sleep(0.1)

if __name__ == '__main__':
    conf = config.Configuration()
    back_fround_color = bg.Bg(conf)
    station_number = st_number.StationNumber(conf)
    status_value = status.Status(conf)
    error_state = error.Error('1234', conf)
    power_supply_instance = pw_supply.PowerSupply(5 , conf)
    feed_instance = feed.Feed('on', conf)
    web_cam = web_cams.Cams('on', conf)
    network_con = network.Network(conf , 'best')
    arduino_ctrl = arduino.Arduino(conf , 'on')
    try:
        conf.init_display()

        back_fround_color.background_color()
        station_number.st_number(3, 'off')
        error_state.error_code()
        status_value.rounded_rectangle('warning')
        status_value.circle()
        status_value.Status_logo_message('warning', 'warning', 'Dosing Error!')
        power_supply_instance.power_supply()
        feed_instance.feed_state()

        base_static = conf.image.copy()  # کپی از تصویر ثابت ساخته شده

        render_thread = threading.Thread(target=render_loop, args=(conf, web_cam, network_con, arduino_ctrl , base_static), daemon=True)
        render_thread.start()
        # conf.show_image()

        while True:
            time.sleep(1)
    
    except Exception as e:
        logging.error(f"Error : {e}")
        conf.module_die

