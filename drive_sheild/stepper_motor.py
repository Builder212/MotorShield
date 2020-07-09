import RPi.GPIO as GPIO
import time

class stepper:
    ''' Defines stepper motor pins on the MotorShield

        Arguments:
        motor = stepper motor
    '''

    stepperpins = {"STEPPER1":{"en1":11, "en2":22, "c1":13,"c2":15, "c3":18, "c4":16},
                   "STEPPER2":{"en1":19, "en2":32, "c1":21,"c2":23, "c3":24, "c4":26}}

    def __init__(self, motor):
        self.config = self.stepperpins[motor]
        GPIO.setup(self.config["en1"],GPIO.OUT)
        GPIO.setup(self.config["en2"],GPIO.OUT)
        GPIO.setup(self.config["c1"],GPIO.OUT)
        GPIO.setup(self.config["c2"],GPIO.OUT)
        GPIO.setup(self.config["c3"],GPIO.OUT)
        GPIO.setup(self.config["c4"],GPIO.OUT)

        GPIO.output(self.config["en1"],GPIO.HIGH)
        GPIO.output(self.config["en2"],GPIO.HIGH)
        GPIO.output(self.config["c1"],GPIO.LOW)
        GPIO.output(self.config["c2"],GPIO.LOW)
        GPIO.output(self.config["c3"],GPIO.LOW)
        GPIO.output(self.config["c4"],GPIO.LOW)

    ''' Set steps of Stepper Motor

        Arguments:
        w1,w2,w3,w4 = Wire of Stepper Motor
    '''
    def setStep(self, w1, w2, w3, w4):
        GPIO.output(self.config["c1"], w1)
        GPIO.output(self.config["c2"], w2)
        GPIO.output(self.config["c3"], w3)
        GPIO.output(self.config["c4"], w4)

    ''' Rotate Stepper motor in forward direction

        Arguments:
        delay = time between steps in miliseconds
        steps = Number of Steps
    '''
    def forward(self, delay, steps):
        for i in range(0, steps):
            self.setStep(1, 0, 0, 0)
            time.sleep(delay)
            self.setStep(0, 1, 0, 0)
            time.sleep(delay)
            self.setStep(0, 0, 1, 0)
            time.sleep(delay)
            self.setStep(0, 0, 0, 1)
            time.sleep(delay)

    ''' Rotate Stepper motor in backward direction

        Arguments:
        delay = time between steps
        steps = Number of Steps
    '''
    def backward(self, delay, steps):
        for i in range(0, steps):
            self.setStep(0, 0, 0, 1)
            time.sleep(delay)
            self.setStep(0, 0, 1, 0)
            time.sleep(delay)
            self.setStep(0, 1, 0, 0)
            time.sleep(delay)
            self.setStep(1, 0, 0, 0)
            time.sleep(delay)

    def stop(self):
        ''' Stops power to the motor,
     '''
        print("Stop Stepper Motor")
        GPIO.output(self.config['c1'],GPIO.LOW)
        GPIO.output(self.config['c2'],GPIO.LOW)
        GPIO.output(self.config['c3'],GPIO.LOW)
        GPIO.output(self.config['c4'],GPIO.LOW)
