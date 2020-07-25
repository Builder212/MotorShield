import RPi.GPIO as GPIO

class motor:
    motor_pins = {"motor_4":{"config":{1:{"e":32,"f":24,"r":26},2:{"e":32,"f":26,"r":24}}},
                 "motor_3":{"config":{1:{"e":19,"f":21,"r":23},2:{"e":19,"f":23,"r":21}}},
                 "motor_2":{"config":{1:{"e":22,"f":16,"r":18},2:{"e":22,"f":18,"r":16}}},
                 "motor_1":{"config":{1:{"e":11,"f":15,"r":13},2:{"e":11,"f":13,"r":15}}}}

    def __init__(self, motor, config):
        self.pins = self.motor_pins[motor]["config"][config]
        GPIO.setup(self.pins['e'],GPIO.OUT)
        GPIO.setup(self.pins['f'],GPIO.OUT)
        GPIO.setup(self.pins['r'],GPIO.OUT)
        self.PWM = GPIO.PWM(self.pins['e'], 50)
        self.PWM.start(0)
        GPIO.output(self.pins['e'],GPIO.HIGH)
        GPIO.output(self.pins['f'],GPIO.LOW)
        GPIO.output(self.pins['r'],GPIO.LOW)

    def forward(self, speed):
        self.PWM.ChangeDutyCycle(speed) #0-100
        GPIO.output(self.pins['f'],GPIO.HIGH)
        GPIO.output(self.pins['r'],GPIO.LOW)

    def reverse(self,speed):
        self.PWM.ChangeDutyCycle(speed) #0-100
        GPIO.output(self.pins['f'],GPIO.LOW)
        GPIO.output(self.pins['r'],GPIO.HIGH)

    def stop(self):
        self.PWM.ChangeDutyCycle(0)
        GPIO.output(self.pins['f'],GPIO.LOW)
        GPIO.output(self.pins['r'],GPIO.LOW)

class motor_set:
    def __init__(self, *motors):
        self.motor = []
        for i in motors:
            print(i.pins)
            self.motor.append(i)

    def forward(self,speed):
        for i in range(len(self.motor)):
            self.motor[i].forward(speed) #0-100

    def reverse(self,speed):
        for i in range(len(self.motor)):
            self.motor[i].reverse(speed) #0-100

    def stop(self):
        for i in range(len(self.motor)):
            self.motor[i].stop()
