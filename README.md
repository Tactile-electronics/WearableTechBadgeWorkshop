## Wearable Tech Badge Workshop

Learn basics of wearable technology with microbits, sensors, Processing, simple electronics

### Session 1

<!--<img src="https://domesticscience.org.uk/criticalkits/images/WearableBioLEDKit1.jpg" width="600">-->

Make & test a DIY Wearable Pressure Sensor using a [Microbit and Micropython](https://microbit.org/guide/python/)

![Skill Covered](https://img.shields.io/badge/skill-making-red.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-micropython-yellow.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-electronics-green.svg?longCache=true&style=plastic)

This first step develops the basics of a pressure sensor; we can refer to more complex and accurate sensors and reflect on their usage.

 * Follow the [WDHLL pressure sensor build](https://github.com/DoESLiverpool/what-does-health-look-like/tree/master/pressure-sensor)
 * Decide on where and how to wear it and connect it the badge

### Session 2

Connect Microbit and sensor to P5.js and experiment with code

![Skill Covered](https://img.shields.io/badge/skill-dataVisualisation-yellow.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-JavaScript-blue.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-making-red.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-electronics-green.svg?longCache=true&style=plastic)

Here we use [Microbit](https://microbit.org/code/) and [p5.js](https://p5js.org/) to learn basic principles of how to manipulate analog sensor data with code and share on platforms like [OpenProcessing](https://openprocessing.org) and [Glitch](https://glitch.com)

 * We will borrow the course materials from the [What DoES Health Look Like (WDHLL)](https://github.com/DoESLiverpool/what-does-health-look-like/) workshop made by [@Laura_pullig](https://twitter.com/Laura_pullig) & [@Zarino](https://twitter.com/zarino) to learn and experience coding for data visualisation.
 * We'll start with an introduction to Microbits as it's a good way in to code for newcomers.
 * We'll introduce peope to P5.js, a javascript implementation of the popular Processing programming language.
  * Use [jackie1050's & zarinos test openprocessing sketches](https://www.openprocessing.org/user/139031) and experiment with P5.js.

<!--<img src="https://domesticscience.org.uk/criticalkits/images/WearableBioLEDKit2.jpg" width="600">
-->

### Session 2.5

Make a circuit that illuminates LEDs in flashing sequences

![Skill Covered](https://img.shields.io/badge/skill-making-red.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-electonics-green.svg?longCache=true&style=plastic)

Here the 3 of us were interested in exploring physical computing in counterpoint to the previous workshops software layers. We are often frustrated with having to use code to do simple routing or logic that could be done with electronic components. Programming with components means you really understand what components do and how they scale up into Integrated circuits and gives a more intimate understanding of the tech we use.


 * We've used this [555 Timer Learning Site](http://www.555-timer-circuits.com/) to make our circuits


#### 555 Timers

We are using the simple `555` timer chip, one of the most common workhorses of electronics. This integrated circuit creates oscillating square wave signals that can be used to control the flow of voltage in a circuit and so control the logic of say, controlling an LED.

<img src="images/TimerLayout.gif">

Find out more on this [555 Timer Circuit website](http://www.555-timer-circuits.com/#circuits)


#### Simple Flasher

<img src="images/Multi-Timing-555-Flasher.jpg" width="400">
<img src="images/555-Circuit-Schem-Fritzing.png" width="400">
<img src="images/555-Circuit-Breadboard-Fritzing.png" width="400">

We've made a circuit with an array of capacitors and resistors so you can experiment with the timings

##### Timing LED pulses

 * C1 1µF Capacitor
 * C2 100µF Capacitor
 * C3 220µF Capacitor
 * R1 = 4.7K Ohm
 * R2 = 4.7K Ohm
 * R3 = 1K Ohm
 * R4 = 10K Ohm
 * R5 = 47K Ohm
 * R6 = 100K Ohm

You can work out the timings with this formula

t<sub>on</sub> = 0.69 x C1 x (R1 + R2)
t<sub>off</sub> = 0.69 x C1 x R2

t<sub>on</sub> = Length of high pulse (seconds)
t<sub>off</sub> = Length of low pulse (seconds)
C1 = Capacitance in Farads
R1 = Resistance in Ohms
R2 = Resistance in Ohms


##### Example

t<sub>on</sub>  = 0.69 x 0.0001 x (4700 + 4700) = 0.64 seconds
t on = 0.69 X 0.000220 x (4700 + 4700) = 1.42 seconds

#### Components

Component|No.|Source|Produced|Notes
--|--|--|--|--
300 point Half Breadboard|1|ShrimpingIt surplus|China
9V Battery pack|1|ShrimpingIt surplus|China|Consider replacing with rechargeable LIPO battery
Jumper Wires|9|DoES Surplus|
555 Timer Chip|1|Ebay|China
Capacitor 1μF|1|ShrimpingIt surplus|China
Capacitor 100μF|1|ShrimpingIt surplus|China
Capacitor 220μF|1|ShrimpingIt surplus|China
Resistor 4.7k Ohm|1|ShrimpingIt surplus|China
Resistor 4.7k Ohm|1|ShrimpingIt surplus|China
Resistor 10k Ohm|1|ShrimpingIt surplus|China
Resistor 47k Ohm|1|ShrimpingIt surplus|China
Resistor 100k Ohm|1|ShrimpingIt surplus|China
Conductive Yarn/Rubber/Pressure Sensor|||

#### Traffic light

<img src="images/traffic_light_breadboard.jpg" width="400">
<img src="images/TrafficLightsSchem.gif" width="400">
<img src="images/bio_illuminator.gif" width="400">

Component|No.|Cost|Source|Produced|Notes|SubTotal
--|--|--|--|--|--|--
Mini Breadboard|5|1.196|[Ebay](https://www.ebay.co.uk/itm/5pcs-5x-WHITE-Mini-170-Tie-Point-Solderless-Breadboard-Prototype-Arduino-PIC-PI/262900293129)|China||£5.98
555 Timer Chip|10|0.185|[Ebay](https://www.ebay.co.uk/itm/10-x-NE555P-Timer-DIP-8-IC-Timer-Fast-Delivery-UK-Seller/323925336619)|China||£1.85
9V Battery pack|1||ShrimpingIt surplus|China|Considering replacing with rechargeable LIPO battery
Jumper Wires|40||ShrimpingIt Surplus|
Capacitor 100μF|1||ShrimpingIt surplus|China
Resistor 47K Ohm|1||ShrimpingIt surplus|China
Resistor 470 Ohm|1||ShrimpingIt surplus|China
Resistor 220 Ohm|2||ShrimpingIt surplus|China
Resistor 100k Ohm|1||ShrimpingIt surplus|China

### Session 3

#### Micropython and the ESP8266

We're using the [ESP8266](#) ESP-12 WeMos D1 Mini Development Board which is like a cheap version of a microbit.

You can refer to the [MicroPython tutorial for ESP8266](https://docs.micropython.org/en/latest/esp8266/tutorial/index.html#micropython-tutorial-for-esp8266) for full details, but we've selected.

#### Connecting up

Windows - Install [Drivers](https://wiki.wemos.cc/downloads) *(possibly not necessary)* Download [PuTTY](https://putty.org/) to connect your ESP8266 to your computer on USB-Serial
Linux - Use the built in `screen` or Putty using `$ sudo apt-get install putty` in your Linux Terminal
Mac - Install [Drivers](https://wiki.wemos.cc/downloads). Then download [PuTTY](https://putty.org/) or use the built-in `Applications/Terminal` and `screen`

##### Using `screen`

In terminal you can use the command

`$ ls /dev/tty.*`
to list your usb devices.

`$ screen /dev/device_name baud-rate`
is the general format.

`$ screen -S wearable /dev/tty.SLAB_USBtoUART 115200`

Then press enter and you'll see the python prompt. You are now connected to your ESP8266!

### Micropython Command Walkthrough

![Skill Covered](https://img.shields.io/badge/skill-python-black.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-screen-blue.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-terminals-lightblue.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-esp8266-gold.svg?longCache=true&style=plastic)

Flash LEDs in response to our sensors

<img src="images/ESP8266-Schem-Fritzing.png" width="600">


In python like we saw earlier, we import the tools we need to do the various things we need, with microbit, most of it is already there.

Get the machine module to control our ins and outs

`import machine`

Lets define a Pin as an output, using the onboard Pin no. 2

`ledPin2 = machine.Pin(2, machine.Pin.OUT)`

This should turn the LED on!

Now try:

`ledPin2.off()`

Annoyingly defining the pin like this means off has no effect, but we can use Signal to abstract away this.

`from machine import Signal`
`Led2 = Signal(ledPin2, invert=True)`

now things will work more intuitively if we use Led2 instead!

`Led2.off()`
`Led2.on()`

Ok now lets read one of our sensors. Wire up following the diagram above.

The ADC (analog to digital conversion) Pin is labelled A0 on your board and we will need the ADC class to make it work

`from machine import ADC`
`adc = ADC(0)`
`adc.read()`

Will return a value. Ok lets get it to read the values until we press `ctrl +c`. We will use a simple loop using `while`

`while True:` press return and you will see `...` and your cursor will indent automatically.

`adc.read()`

Now press return, and you get another indent, return a few time indicates thats the end of that loop and it will then execute the code.

Play with your sensor and watch the numbers change. Cool eh? Bit fast though, lets slow it down with `time`

`import time`

Now we can use `time.sleep(seconds)` to wait before reading the pin again.

```
while True:
    adc.read()
    time.sleep(0.5)
```

Now lets use that to blink our LED

```
while True:
    Led2.on()
    time.sleep_ms(adc.read() * 10)
    Led2.off()
    time.sleep_ms(adc.read() * 10)
```

Ok but higher resistance, bigger stretch or pressue is slowing our flashes. WE can flip it round

```
while True:
    stretch = 500 - (adc.read() *10)
    Led2.on()
    time.sleep_ms(stretch)
    Led2.off()
    time.sleep_ms(stretch)
```

#### Components

Component|No.|Source|Produced|Notes
--|--|--|--|--
Microusb data cable|1|||
Jumper Wires|4||
Resistor 4.7k Ohm|1||China
Conductive Yarn/Rubber/Pressure Sensor|||


### Session 4
Make our wearable

![Skill Covered](https://img.shields.io/badge/skill-making-red.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-sewing-orange.svg?longCache=true&style=plastic)

Finally we assemble everything using a textile pocket to enclose electronics

 * Enclose the ESP circuit in a customisable fabric template
