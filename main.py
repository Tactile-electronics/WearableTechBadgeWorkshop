from machine import Signal, Pin, ADC
import time

ledPin2 = machine.Pin(2, machine.Pin.OUT)
Led2 = Signal(ledPin2, invert=True)

adc = ADC(0)

while True:
    stretch = 500 - (adc.read() *10)
    Led2.on()
    time.sleep_ms(stretch)
    Led2.off()
    time.sleep_ms(stretch)
