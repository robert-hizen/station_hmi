import time
import threading
from config import config
from src import cycle_time ,copy_right , error, bg , st_number , status , pw_supply , feed , web_cams , network , arduino
import logging
from PIL import Image

stop_event = threading.Event()

def render_loop(conf , web_cam , network , arduino , static_background):
    while not stop_event.is_set():
        web_cam.update()
        network.update()
        arduino.update()

        base_temp = static_background.copy()
        base_temp.paste(web_cam.current_image , (web_cam.X_CORDINATE , web_cam.Y_CORDINATE) , web_cam.current_image )
        base_temp.paste(network.current_image , (network.X_CORDINATE , network.Y_CORDINATE) , network.current_image )
        base_temp.paste(arduino.current_image , (arduino.X_CORDINATE , arduino.Y_CORDINATE) , arduino.current_image )
        conf.disp.ShowImage(base_temp.rotate(180))
        time.sleep(0.1)

def main():
    conf = config.Configuration()
    back_fround_color = bg.Bg(conf)
    station_number = st_number.StationNumber(conf)
    status_value = status.Status(conf)
    error_state = error.Error('1234', conf)
    power_supply_instance = pw_supply.PowerSupply(5 , conf)
    feed_instance = feed.Feed('off', conf)
    web_cam = web_cams.Cams('off', conf)
    network_con = network.Network(conf ,None)
    arduino_ctrl = arduino.Arduino(conf)
    pooyesh_machine = copy_right.CopyRight(conf)
    cycle_time_instance = cycle_time.CycleTime(conf)
    try:
        conf.init_display()

        back_fround_color.background_color()
        station_number.st_number(7, 'on')
        # error_state.error_code()
        status_value.rounded_rectangle('error')
        status_value.Status_logo_message('Dosing Error! please enter a valid error')
        power_supply_instance.power_supply()
        # cycle_time_instance.cycle(1000)
        feed_instance.feed_state()
        # pooyesh_machine.pooyesh_machine_logo()
        base_static = conf.image.copy()  

        render_thread = threading.Thread(target=render_loop, args=(conf, web_cam, network_con, arduino_ctrl , base_static), daemon=True)
        render_thread.start()
        # conf.show_image()

        while True:
            time.sleep(1)
    
    except Exception as e:
        logging.error(f"Error : {e}")
        stop_event.set()
        render_thread.join()
        conf.module_die


if __name__ == '__main__':
    main()

