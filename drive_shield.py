import RPi.GPIO as GPIO
import time, sys
from drive_sheild/arrow import arrow
from drive_sheild/motor import motor, motor_set
from drive_sheild/sensor import sensor
from drive_sheild/stepper_motor import stepper

class drive_sheild:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.M1 = None
        self.M2 = None
        self.M3 = None
        self.M4 = None

    def setup_motor(self, motor):
        config = 1
        motor_list = ['motor_1', 'motor_2', 'motor_3', 'motor_4']
        if motor == motor_1ist[0]:
            self.M1 = motor(motor, config)
        elif motor == motor_1ist[1]:
            self.M2 = motor(motor, config)
        elif motor == motor_1ist[2]:
            self.M3 = motor(motor, config)
        elif motor == motor_1ist[3]:
            self.M4 = motor(motor, config)
        else:
            print("The \'motor\' value you entered for setup_motor is incorrect.")
            sys.exit()
