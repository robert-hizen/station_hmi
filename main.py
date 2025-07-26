import asyncio
import logging
from config import config
from src import web_cams_holder,web_cams_dosing ,cycle_time, copy_right, error, bg, st_number, status, pw_supply, feed, network, arduino


async def render_loop(conf,holder_web_cam ,  web_cam, network, arduino, static_background):
    while True:
        web_cam.update()
        network.update()
        arduino.update()
        holder_web_cam.update()

        base_temp = static_background.copy()
        base_temp.paste(web_cam.current_image, (web_cam.X_CORDINATE, web_cam.Y_CORDINATE), web_cam.current_image)
        base_temp.paste(network.current_image, (network.X_CORDINATE, network.Y_CORDINATE), network.current_image)
        base_temp.paste(arduino.current_image, (arduino.X_CORDINATE, arduino.Y_CORDINATE), arduino.current_image)
        base_temp.paste(holder_web_cam.current_image, (holder_web_cam.X_CORDINATE, holder_web_cam.Y_CORDINATE), holder_web_cam.current_image)

        conf.disp.ShowImage(base_temp.rotate(180))
        await asyncio.sleep(0.1)

async def main():
    conf = config.Configuration()
    back_fround_color = bg.Bg(conf)
    station_number = st_number.StationNumber(conf , 20 , 'on')
    status_value = status.Status(conf , 'error' , 'Dosing Error! please enter a valid error' )
    error_state = error.Error('1234', conf)
    power_supply_instance = pw_supply.PowerSupply(5, conf)
    feed_instance = feed.Feed('off', conf)
    web_cam_dosing = web_cams_dosing.DosingWebCam('off', conf)
    web_cam_holder = web_cams_holder.HolderWebCam('off', conf)           
    network_con = network.Network(conf, 'off')
    arduino_ctrl = arduino.Arduino(conf , None)
    pooyesh_machine = copy_right.CopyRight(conf)
    cycle_time_instance = cycle_time.CycleTime(conf , 2000)

    try:
        conf.init_display()

        back_fround_color.background_color()
        station_number.st_number()
        error_state.error_code()
        power_supply_instance.power_supply()
        status_value.rounded_rectangle()
        cycle_time_instance.cycle()
        status_value.Status_logo_message()
        feed_instance.feed_state()
        pooyesh_machine.pooyesh_machine_logo()

        base_static = conf.image.copy()

        render_task = asyncio.create_task(render_loop(conf, web_cam_holder , web_cam_dosing, network_con, arduino_ctrl, base_static))

        while True:
            await asyncio.sleep(1)

    except Exception as e:
        logging.error(f"Error : {e}")
        conf.module_die()

if __name__ == '__main__':
    asyncio.run(main())
