from machine import Pin
from neopixel import NeoPixel
import time

n = 7 # Set the number of pixels on your NeoPixel
pin = Pin(5, Pin.OUT)   # setup GPIO5 pin (D1) as output to drive the NeoPixels
np = NeoPixel(pin, n)   # create NeoPixel object on GPIO5, for n pixels
np[0] = (255, 255, 255) # set the first pixel to white
np.write()              # write data to all pixels
np[0] = (0, 0, 0) # set the first pixel to nothing (black)
np.write()              # write data to all pixels

def cycle():
    for i in range(4 * n): # setup a loop that lasts 4 times the number of NeoPixels and turns each LED on
        for j in range(n): # setup a nested loop that goes thru each pixel and turns the other LEDs off
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255) # turns one of n LEDs white in sequence with modulo ie 1 % 7 = 0, 7 % 7 = 0..8 % 7 = 1, 9 & 7 = 2..13 % 7 = 6, 14 % 7 = 0, and onwards to 4 * n
        np.write() # write to all LEDs
        time.sleep_ms(25) # sleep for 25 microseconds

def colourBounce(stretcher):
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128 - stretcher)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)


def bounce():
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

def fade():
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

def clear():
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
