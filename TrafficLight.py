import machine
import utime

green_light = machine.Pin(15, machine.Pin.OUT)
yellow_light = machine.Pin(14, machine.Pin.OUT)
red_light = machine.Pin(13, machine.Pin.OUT)

while True:
    red_light.value(1)
    utime.sleep(5)
    red_light.value(0)
    yellow_light.value(0)
    green_light.value(1)
    utime.sleep(5)
    green_light.value(0)
    yellow_light.value(1)
    utime.sleep(2)
    yellow_light.value(0)
