from drive_shield.arrow_shield import arrow
from drive_shield.motor_shield import motor, motor_set
import RPi.GPIO as GPIO
from time import sleep

if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    m1 = motor("motor_1", 2)
    m2 = motor("motor_2", 2)
    m3 = motor("motor_3", 1)
    m4 = motor("motor_4", 1)
    drive = motor_set(m1, m2, m3, m4)
    drive.forward(100)
    sleep(10)
    drive.stop()
