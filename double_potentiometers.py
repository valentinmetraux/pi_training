#!/usr/bin/env python3

import RPi.GPIO as GPIO
import ADC0834
import time


def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    ADC0834.setup()

def destroy():
    # Release resource
    GPIO.cleanup()
    
def loop():
    while True:
        start = ADC0834.getResult(0)
        end = ADC0834.getResult(2)
        print(f'Range {start} - {end}')
        time.sleep(0.2)
        
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the program destroy() will be executed.
        destroy()