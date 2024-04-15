# Arducam port to Pico

from machine import Pin, SPI, reset
from camera import *
# Developing on 1.19

'''
#################### PINOUT ####################
Camera wire - ProS3 
VCC - 3V3
GND - GND
SCK - white - 36
MISO - RX - brown - 37
MOSI - TX - yellow - 35
CS - orange - 15
'''

################################################################## CODE ACTUAL ##################################################################
spi = SPI(1,sck=Pin(36), miso=Pin(37), mosi=Pin(35), baudrate=1000000)
cs = Pin(34, Pin.OUT)

cam = Camera(spi, cs)

cam.resolution = '640x480'
sleep_ms(500)
# cam.set_filter(cam.SPECIAL_REVERSE)
cam.set_brightness_level(cam.BRIGHTNESS_PLUS_4)
cam.set_contrast(cam.CONTRAST_MINUS_3)

print('starting capture')
cam.capture_jpg()
sleep_ms(500)
print('starting save')
cam.saveJPG('image.jpg')



#################################################################################################################################################
'''
Benchmarks
- Default SPI speed (1000000?), cam.resolution = '640X480', no burst read (camera pointed at roof) ==== TIME: ~7.8 seconds
- Increased speed (8000000), cam.resolution = '640X480', no burst read (camera pointed at roof) ==== TIME: ~7.3 seconds

'''
