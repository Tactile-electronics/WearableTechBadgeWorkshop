## Wearable Tech Badge Workshop

Learn basics of wearable technology with microbits, sensors, Processing, simple electronics




### Session 1

<!--<img src="https://domesticscience.org.uk/criticalkits/images/WearableBioLEDKit1.jpg" width="600">-->

Make & test a DIY Wearable Pressure Sensor using a Microbit

![Skill Covered](https://img.shields.io/badge/skill-making-red.svg?longCache=true&style=plastic)
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

Here we use [Microbit](https://microbit.org/code/) and [OpenProcessing](https://openprocessing.org) and [p5.js](https://p5js.org/) to learn basic principles of how to manipulate analog sensor data with code, in this case

 * We will borrow Laura Pullig's [What DoES Health Look Like (WDHLL)](https://github.com/DoESLiverpool/what-does-health-look-like/) to learn and experience coding for data visualisation.
 * We'll start with an introduction to Microbits as it's a good way in to code for newcomers.
 * We'll introduce peope to P5.js, a javascript implementation of the popular Processing programming language.
  * Use [jackie1050's & zarinos test openprocessing sketches](https://www.openprocessing.org/user/139031) and experiment with P5.js.

<!--<img src="https://domesticscience.org.uk/criticalkits/images/WearableBioLEDKit2.jpg" width="600">
-->

### Session 3

Make a circuit that illuminates LEDs in flashing sequences

![Skill Covered](https://img.shields.io/badge/skill-making-red.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-electonics-green.svg?longCache=true&style=plastic)

Here the 3 of us were interested in exploring physical computing in counterpoint to the previous workshops software layers. We are often frustrated with having to use code to do simple routing or logic that could easily be done with electronic components. Programming with components means you really understand what components do and how they scale up into Integrated circuits and gives a more intimate understanding of the tech we use.


 * We've used this [555 Timer Learning Site](http://www.555-timer-circuits.com/) to make our circuits


## 555 timer

Simple timing chip

<img src="images/TimerLayout.gif">

[555 Timer Circuit Resources](http://www.555-timer-circuits.com/#circuits)


### Simple Flasher

<img src="images/555flashersmall.gif" height="250">

<img src="images/555FlasherSchem.gif" height="250">

Component|No.|Source|Produced|Notes
--|--|--|--|--
Mini Breadboard|1|ShrimpingIt surplus|China
3V Battery pack|1|ShrimpingIt surplus|China|Considering replacing with rechargeable LIPO battery
Jumper Wires|9|DoES Surplus|
555 Timer Chip|1|Ebay|China
Capacitor 1μF|1|ShrimpingIt surplus|China
Resistor 1k Ohm|2|ShrimpingIt surplus|China
Resistor 470k Ohm|1|ShrimpingIt surplus|China
Conductive Yarn |||


### Traffic light


<img src="images/traffic_light_breadboard.jpg" width="300">
<img src="images/TrafficLightsSchem.gif" width="300">
<img src="images/bio_illuminator.gif" width="600">

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


### Session 4
Make our wearable

![Skill Covered](https://img.shields.io/badge/skill-making-red.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-sewing-orange.svg?longCache=true&style=plastic)
![Skill Covered](https://img.shields.io/badge/skill-microscopy-black.svg?longCache=true&style=plastic)

Finally we assemble everything using a textile pocket to enclose electronics

 * Enclose the `555` & `DIP` switch illumination circuit in a customisable fabric template
 * Test it as a bio-illuminator
 * Make sure it also works as a name badge when no organisms are available. As our algae are only 100 nm long they can easily live between the writing that is done on the writable microscope slide (ie so you can wear the badge and write your name on it). It's a name badge so it's inherently sociable in the right context. Conversations can include or exclude microbiological critters depending on context.
 * We can also look in detail under the microscope at the physical nature of the components, and potentially make PDMS microfluidic moulds from the markings and micro structures of the components and textile materials.


