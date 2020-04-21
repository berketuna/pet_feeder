#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

class Stepper(): # Stepper object with its driver
    def __init__(self, pins):
        GPIO.setmode(GPIO.BOARD) # GPIO pin configuration according to their position
        self.pins = pins
        GPIO.setup(pins, GPIO.OUT)
        self.phases = ((1,0,0,0),
                       (1,1,0,0),
                       (0,1,1,0),
                       (0,0,1,0),
                       (0,0,1,1),
                       (0,0,0,1),
                       (1,0,0,1),
                       (0,0,0,0)) 

    def rotate(self, cycles, direction, speed):
        if direction == 'ccw':
            for cycle in range(cycles*510):
                for phase in range(8):
                    GPIO.output(self.pins, self.phases[phase])
                    sleep(0.0019-(speed*0.00001))
        if direction == 'cw':
            for cycle in range(cycles*510):
                for phase in range(8):
                    GPIO.output(self.pins, self.phases[-phase])
                    sleep(0.0019-(speed*0.00001))

    def cleanws(self):
        GPIO.cleanup()


