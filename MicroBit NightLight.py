from microbit import *

all_on = Image()
pin0.read_digital()

while True:
    value = pin0.read_analog()
    
    light_level = int(value / 113)
    lamp_level = 9 - light_level
    all_on.fill(lamp_level)
    
    display.show(all_on)
    