# station-lcd

UI for Raspberry Pi with GC9A01-based LCD and serial connection to Arduino.
you can download dependecies from requirments.txt file
you must be use **spi** protocol
`pip install -r requirments.txt`
### TFT Module GCA901
![TFT Moudile GCA901](/template/picture/TFT.jpg)
### Rasberry pi 4b 
![Rasberry pi 4b Board](/template/picture/rassberrypi.jpg)
for more info about this board you can refrence to raspberrypi Docs : [Docs:](https://www.raspberrypi.com/documentation/)
## Wire Connections
|GCA901|Rasberrypi 4b|
|------|-------------|
|VCC|3.3V|
|GND|GND|
|RST|13(PIN) , GPIO 27|
|BLK|17 (PIN)|
|SDA|19 (PIN) , GPIO 10 (MOSI)|
|SCL|23 (PIN) , GPIO 11 (SCLK)|
|CS|24 (PIN) , GPIO 8 (CE0)|
|DC|22 (PIN) , GPIO 25|

