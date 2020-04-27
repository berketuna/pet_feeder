#!/usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep

class Stepper():# Stepper object with its driver
    def __init__(self, pins):
        self.pins = pins
        self.cycle_step = 512 #Number of steps needed for stepper motor to
                              # approximately rotate 360 degrees  
        self.sleep_time = 0.003# How fast the steps initiate after one another. Keep as is.
                                  
      #                           # High pin timings to drive the 4-input stepper driver
      # self.phase =   ( 
      #                (1,0,0,0), #
      #                (1,1,0,0), # 
      #                (0,1,0,0), #                 --Half Stepping--
      #                (0,1,1,0), #
      #                (0,0,1,0), #
      #                (0,0,1,1), #
      #                (0,0,0,1), #
      #                (1,0,0,1)) #
        
        self.phase =   ( 
                       (1,1,0,0), #
                       (0,1,1,0), #             --Dual Phase Stepping--
                       (0,0,1,1), #                 
                       (1,0,0,1)) #

    def rotate(self, cycles, direction):
        GPIO.setmode(GPIO.BOARD) # GPIO pin configuration according to their position
        GPIO.setup(self.pins, GPIO.OUT, initial= GPIO.LOW) # Initialize the pins for rotation
        total_step = (self.cycle_step)*cycles # Total steps needed for input cycle
        
        for step in range(total_step):
            for phase in range(4):
                if direction == 'ccw': # Turn counter-clockwise
                    GPIO.output(self.pins, self.phase[phase])
                    sleep(self.sleep_time)
                if direction == 'cw': # Turn clockwise
                    GPIO.output(self.pins, self.phase[-phase])
                    sleep(self.sleep_time)
            if step  == (total_step-1):
                GPIO.cleanup() # Cleaning up the used pins after the rotation is finished

