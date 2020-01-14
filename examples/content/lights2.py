from machine import Pin
from neopixel import NeoPixel
import time
import urandom

n = 8
pin = Pin(5, Pin.OUT)   # set GPIO5 (D1) to output to drive NeoPixels
np = NeoPixel(pin, 8)   # create NeoPixel driver on GPIO0 for 7 pixels

def cycle():
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

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

def sparkle(level, brightdiv, steps, max_level, rgb_start, rgb_end, rgb_sparkle):

    for x in range(n):
        if sparkling(abs(level)):
            np[x] = (rgb_sparkle[0] // brightdiv, rgb_sparkle[1] // brightdiv, rgb_sparkle[2] // brightdiv)
        else:
            np[x] = get_colour(rgb_start, rgb_end, abs(level), max_level, brightdiv)
            

    np.write()
    time.sleep_ms(6)

def smooth(level, brightdiv, steps, max_level, rgb_start, rgb_end, rgb_sparkle):

    selected = []

    for x in range(n):
        if sparkling(abs(level)):
            np[x] = (rgb_sparkle[0] // brightdiv, rgb_sparkle[1] // brightdiv, rgb_sparkle[2] // brightdiv)
            selected.append(1)
        else:
            np[x] = get_colour(rgb_start, rgb_end, abs(level), max_level, brightdiv)
            selected.append(0)

    for x in range(n):
        for y in range(steps):
            if selected[x]:
                np[x] = (
                    255 // brightdiv + (y * (1 - (1 // brightdiv)) // steps),
                    255 // brightdiv + (y * (1 - (1 // brightdiv)) // steps),
                    255 // brightdiv + (y * (1 - (1 // brightdiv)) // steps),
                )
        np.write()
        time.sleep_ms(6)
        for y in range(steps):
            if selected[x]:
               np[x] = (
                    255 // brightdiv + ((steps - y) * (1 - (1 // brightdiv)) // steps),
                    255 // brightdiv + ((steps - y) * (1 - (1 // brightdiv)) // steps),
                    255 // brightdiv + ((steps - y) * (1 - (1 // brightdiv)) // steps),
                )
        np.write()
        time.sleep_ms(6)

# Less or more likely to return True, based on the sparkle_chance.
# sparkle_chance of 0 means 0% chance of returning True.
# sparkle_chance of 255 means 100% chance of returning True.
def sparkling(sparkle_chance):
    return sparkle_chance > 0 and sparkle_chance >= randint(1, 256)

def randint(min, max):
    span = max - min + 1
    div = 0x3fffffff // span
    offset = urandom.getrandbits(30) // div
    val = min + offset
    return val

def static_rainbow(brightdiv):
    np[7] = (255 // brightdiv, 0, 0)
    np[6] = (148 // brightdiv, 0, 211 // brightdiv)
    np[5] = (75 // brightdiv, 0, 130 // brightdiv)
    np[4] = (0, 0, 255 // brightdiv)
    np[3] = (0, 255 // brightdiv, 0)
    np[2] = (255 // brightdiv, 255 // brightdiv, 0)
    np[1] = (255 // brightdiv, 127 // brightdiv, 0)
    np[0] = (255 // brightdiv, 0, 0)
    np.write()

def get_colour(rgb_start, rgb_end, level, max_level, brightdiv):
    rgb_out = [0, 0, 0]
    for y in range(3):
        rgb_out[y] =  (rgb_start[y] + ((rgb_end[y] - rgb_start[y]) * level // max_level)) // brightdiv
    return rgb_out
