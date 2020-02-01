from machine import Signal, Pin, ADC
from time import sleep

ledPin2 = machine.Pin(2, machine.Pin.OUT)
Led2 = Signal(ledPin2, invert=True)

adc = ADC(0)

val = 0

while True:
  val = adc.read()
  print(val)
  if val < 100:
    Led2.on()
  else:
    Led2.off()
  sleep(0.25)