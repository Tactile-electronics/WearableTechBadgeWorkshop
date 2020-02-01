from machine import Signal, Pin, ADC
import time

ledPin2 = machine.Pin(2, machine.Pin.OUT)
Led2 = Signal(ledPin2, invert=True)

adc = ADC(0)
sensor_max = 500 # This is the max reading for my sensor, you'll need to find your max reading
while True:
    stretch = sensor_max - (adc.read() *10) #assign stretch to the maximum less our sensor reading
    Led2.on()
    time.sleep_ms(stretch)
    Led2.off()
    time.sleep_ms(stretch)
