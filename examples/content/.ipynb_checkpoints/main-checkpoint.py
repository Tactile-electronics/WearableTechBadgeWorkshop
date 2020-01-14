from machine import Pin
from neopixel import NeoPixel
import time

n = 7
button_green = Pin(14, Pin.IN, Pin.PULL_UP)
button_red = Pin(12, Pin.IN, Pin.PULL_UP)
neopixel_pin = Pin(5, Pin.OUT)
np = NeoPixel(neopixel_pin, n)
level = 0

for i in range(n):
    np[i] = (0, 0, 255)
np.write()

while True:
    button_green_1 = button_green.value()
    button_red_1 = button_red.value()
    time.sleep(0.01)
    button_green_2 = button_green.value()
    button_red_2 = button_red.value()

    print ("Button green %d %d" %(button_green_1, button_green_2))
    print ("Button red %d %d" % (button_red_1, button_red_2))

    if (button_green_1 and not button_green_2) and level < 7:
        level += 1
    
    if (button_red_1 and not button_red_2) and level > -7:
        level -= 1

    for i in range(n):
        np[i] = (0, 0, 124)
    for i in range(abs(level)):
        if level > 0:
            np[i] = (0, 124, 0)
        elif level < 0:
            np[i] = (124, 0, 0)
    np.write()



