"""Save your file as "code.py" or "main.py" to run on the actual device.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""

# import CPX library
from adafruit_circuitplayground.express import cpx
import time

cpx.pixels.brightness = 1
 
while True:
    cpx.pixels[0] = (255, 0, 0)
    cpx.pixels[1] = (0, 255, 0)
    cpx.pixels[2] = (0, 0, 255)
