import time
# import sys
# import RPi.GPIO as GPIO
from hx711 import HX711

hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(1)
hx.reset()
hx.tare()

print("Tare done! Add weight now...")


def get_weight():
    i = 0
    weight = 0
    while i < 1000:
        weight = hx.get_weight(5)  #valoarea medie de la 5 masuratori
        i = i + 1
        print(weight)

        hx.power_down()
        hx.power_up()
        time.sleep(0.1)
    return weight
