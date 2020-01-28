from machine import ADC
import time
from lights import *

adc = ADC(0)
adc.read()


while True:
    stretch = 500 - (adc.read() *10)
    colourBounce(stretch)
    time.sleep_ms(stretch)
    colourBounce(stretch)
    time.sleep_ms(stretch)
