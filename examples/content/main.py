from switch import Switch
from machine import Pin
from machine import Timer
from neopixel import NeoPixel
import time
import lights2

n = 8

button_green = Pin(14, Pin.IN, Pin.PULL_UP)
button_red = Pin(12, Pin.IN, Pin.PULL_UP)
my_switch_green = Switch(button_green)
my_switch_red = Switch(button_red)
neopixel_pin = Pin(5, Pin.OUT)
np = NeoPixel(neopixel_pin, n)
level = 0
brightdiv = 4 # fraction 1/4
steps = 6
max_level = 8
for i in range(n):
    np[i] = (255 // brightdiv, 0, 255 // brightdiv)
np.write()
time.sleep_ms(60)
rgb_start_discontent = [160, 60, 30]
rgb_end_discontent = [40, 25, 15]
rgb_sparkle_discontent = [25, 255, 0]
rgb_start_content = [200, 55, 0]
rgb_end_content = [135, 120, 0]
rgb_sparkle_content = [255, 255, 255]
rgb_blue = [0, 0, 255]
rgb_red = [255, 0, 0]

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
    elif (my_switch_green_new_value and not my_switch_green_value) and level < max_level:
        level += 1
    elif (my_switch_red_new_value and not my_switch_red_value) and level > -1 * max_level:
        level -= 1

    if level < 0:
        lights2.sparkle(level, brightdiv, steps, max_level, rgb_start_discontent, rgb_end_discontent, rgb_sparkle_discontent)
    elif level > 0:
        lights2.smooth(level, brightdiv, steps, max_level, rgb_start_content, rgb_end_content, rgb_sparkle_content)
    else:
        lights2.sparkle(level, brightdiv, steps, max_level, rgb_red, rgb_red, rgb_sparkle_content)
  
