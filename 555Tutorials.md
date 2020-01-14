## 555 Tutorials

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

#### Example

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


