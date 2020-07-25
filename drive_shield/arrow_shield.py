import RPi.GPIO as GPIO

class arrow():
    arrow_pins={1:33,2:35,3:37,4:36}
    def __init__(self, which):
        self.pin = self.arrow_pins[which]
        GPIO.setup(self.pin,GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def on(self):
        GPIO.output(self.pin,GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin,GPIO.LOW)
