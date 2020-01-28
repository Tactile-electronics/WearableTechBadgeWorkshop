from machine import Signal, Pin
from time import sleep

ledPin2 = machine.Pin(2, machine.Pin.OUT)
led2 = Signal(ledPin2, invert=True)
led2.off()

while True:
    led2.on()
    sleep(0.5)
    led2.off()
    sleep(0.25)
