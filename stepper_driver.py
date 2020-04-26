#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

class Stepper():# Stepper object with its driver
    def __init__(self, pins):
        self.pins = pins
        self.cycle_step = 515 #Number of steps needed for stepper motor to
                              # approximately rotate 360 degrees  
        self.sleep_time = 0.002# How fast the steps initiate after one another. Keep as is.
        self.phases = ((1,0,0,0), #
                       (1,1,0,0), # 
                       (0,1,1,0), #
                       (0,0,1,0), # High pin timing to drive the 4-input stepper driver
                       (0,0,1,1), #
                       (0,0,0,1), #
                       (1,0,0,1)) #

    def rotate(self, cycles, direction):
        GPIO.setmode(GPIO.BOARD) # GPIO pin configuration according to their position
        GPIO.setup(self.pins, GPIO.OUT, initial= GPIO.LOW) # Initialize the pins for rotation
        total_step = (self.cycle_step)*cycles # Total steps needed for input cycle
        
        for step in range(total_step):
            for phase in range(7):
                if direction == 'ccw': # Turn counter-clockwise
                    GPIO.output(self.pins, self.phases[phase])
                    sleep(self.sleep_time)
                if direction == 'cw': # Turn clockwise
                    GPIO.output(self.pins, self.phases[-phase])
                    sleep(self.sleep_time)
            if step  == (total_step-1):
                GPIO.cleanup() # Cleaning up the used pins after the rotation is finished

