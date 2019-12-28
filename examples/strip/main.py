from switch import Switch
from machine import Pin
from machine import Timer
from neopixel import NeoPixel
import time

n = 8

button_green = Pin(14, Pin.IN, Pin.PULL_UP)
button_red = Pin(12, Pin.IN, Pin.PULL_UP)
my_switch_green = Switch(button_green)
my_switch_red = Switch(button_red)
neopixel_pin = Pin(5, Pin.OUT)
np = NeoPixel(neopixel_pin, n)
level = 0
brightness=50

for i in range(n):
    np[i] = (brightness//2, 0, brightness//2)
np.write()

while True:

    my_switch_green_new_value = False
    my_switch_red_new_value = False
 
    # Disable interrupts for a short time to read shared variable
    irq_state = machine.disable_irq()
    if my_switch_green.new_value_available:
        my_switch_green_value = my_switch_green.value
        my_switch_green_new_value = True
        my_switch_green.new_value_available = False
    if my_switch_red.new_value_available:
        my_switch_red_value = my_switch_red.value
        my_switch_red_new_value = True
        my_switch_red.new_value_available = False

    machine.enable_irq(irq_state)
 
    # If my switch had a new value, print the new state
    if my_switch_green_new_value:
        if my_switch_green_value:
            print("Green Switch Opened")
        else:
            print("Green Switch Closed")

    if my_switch_red_new_value:
        if my_switch_red_value:
            print("Red Switch Opened")
        else:
            print("Red Switch Closed")

    if (my_switch_green_new_value and not my_switch_green_value) and (my_switch_red_new_value and not  my_switch_red_value):
        level = 0
    elif (my_switch_green_new_value and not my_switch_green_value) and level < 8:
        level += 1
    elif (my_switch_red_new_value and not my_switch_red_value) and level > -8:
        level -= 1

    for i in range(n):
        np[i] = (0, 0, brightness)
    for i in range(abs(level)):
        if level > 0:
            np[i] = (0, brightness, 0)
        elif level < 0:
            np[i] = (brightness, 0, 0)
    np.write()
