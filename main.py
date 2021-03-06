#!/usr/bin/env python3
from stepper_driver import Stepper

set_pins = (11, 13, 16, 18) # Four output pins on RPi which are connected to IN1-IN2-IN3-IN4
motor = Stepper(set_pins) # Instantiated stepper object

