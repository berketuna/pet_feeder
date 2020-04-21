#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

class Stepper():# Stepper object with its driver
    def __init__(self, pins):
        self.pins = pins
        self.cycle_step = 515
        self.phases = ((1,0,0,0),
                       (1,1,0,0),
                       (0,1,1,0),
                       (0,0,1,0),
                       (0,0,1,1),
                       (0,0,0,1),
                       (1,0,0,1))

    def rotate(self, cycles, direction):
        GPIO.setmode(GPIO.BOARD) # GPIO pin configuration according to their position
        GPIO.setup(self.pins, GPIO.OUT, initial= GPIO.LOW)
        sleep_time = 0.00085
        total_step = (self.cycle_step)*cycles
        for step in range(total_step):
            for phase in range(7):
                if direction == 'ccw':
                    GPIO.output(self.pins, self.phases[phase])
                    sleep(sleep_time)
                if direction == 'cw':
                    GPIO.output(self.pins, self.phases[-phase])
                    sleep(sleep_time)
            if step  == (total_step-1):
                GPIO.cleanup()

    def cleanws(self):
        GPIO.cleanup()


