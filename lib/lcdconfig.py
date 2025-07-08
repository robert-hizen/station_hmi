# /*****************************************************************************
# * | File        :	  epdconfig.py
# * | Author      :   Waveshare team
# * | Function    :   Hardware underlying interface
# * | Info        :
# *----------------
# * | This version:   V1.0
# * | Date        :   2019-06-21
# * | Info        :   
# ******************************************************************************
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documnetation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to  whom the Software is
# furished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

import os
import sys
import time
import spidev
import logging
import numpy as np
from gpiozero import *

class RaspberryPi:
    # Constructor
    def __init__(self,spi=spidev.SpiDev(0,0),spi_freq=40000000,rst = 27,dc = 25,bl = 18,bl_freq=1000,i2c=None,i2c_freq=100000):
        # Initialize
        self.np=np
        self.INPUT = False
        self.OUTPUT = True

        # Set value from a __init__ param
        self.SPEED  = spi_freq
        self.BL_freq = bl_freq
        # Set module pin as output and use our  Attributes  
        self.RST_PIN = self.gpio_mode(rst,self.OUTPUT)
        self.DC_PIN = self.gpio_mode(dc,self.OUTPUT)
        self.BL_PIN = self.gpio_pwm(bl)
        self.bl_DutyCycle(0)
        
        #Initialize SPI
        self.SPI = spi
        if self.SPI!=None :
            self.SPI.max_speed_hz = spi_freq
            self.SPI.mode = 0b00
    # Set PinMode Dinamically
    def gpio_mode(self,Pin,Mode,pull_up = None,active_state = True):
        # if mode == 1 (OUTPUT)
        # if active high == true we have a maximum voltage
        if Mode:
            return DigitalOutputDevice(Pin,active_high = True,initial_value =False)
        # Else mode != 1 (INPUT)
        else:
            return DigitalInputDevice(Pin,pull_up=pull_up,active_state=active_state)
    # ON or OFF Pins
    def digital_write(self, Pin, value):
        if value:
            Pin.on()
        else:
            Pin.off()
    # for read data from pin
    def digital_read(self, Pin):
        return Pin.value
    # intrupt or delay
    def delay_ms(self, delaytime):
        time.sleep(delaytime / 1000.0)
    # for managing backlight
    def gpio_pwm(self,Pin):
        return PWMOutputDevice(Pin,frequency = self.BL_freq)

    def spi_writebyte(self, data):
        if self.SPI!=None :
            self.SPI.writebytes(data)
    # for managing back light brightness
    def bl_DutyCycle(self, duty):
        if duty < 0:
            duty = 0
        elif duty > 100:
            duty = 100
        self.BL_PIN.value = duty / 100
    # for managing freequency back light
    def bl_Frequency(self,freq):# Hz
        self.BL_PIN.frequency = freq
    # for init SPI module      
    def module_init(self):
        if self.SPI!=None :
            self.SPI.max_speed_hz = self.SPEED        
            # special mode for spi is 00
            self.SPI.mode = 0b00     
        return 0

    def module_exit(self):
        logging.debug("Shutting down SPI and GPIO resources...")
        if self.SPI :
            self.SPI.close()
        
        logging.debug("gpio cleanup...")
        for pin , value in [(self.RST_PIN , 1) , (self.DC_PIN , 0)]:
            self.digital_write(pin , value)   
        if self.BL_PIN:
            self.BL_PIN.close()
        time.sleep(0.001)
        print("Cleanup complete.")