from RPi.GPIO import GPIO
import time

class sensor:
    ''' Defines a sensor connected to the sensor pins on the MotorShield

        Arguments:
        sensortype = string identifying which sensor is being configured.
            i.e. "IR1", "IR2", "ULTRASONIC"
        boundary = an integer specifying the minimum distance at which the sensor
            will return a Triggered response of True.
    '''
    Triggered = False
    def iRCheck(self):
        input_state = GPIO.input(self.config["echo"])
        if input_state == True:
            print("Sensor 2: Object Detected")
            self.Triggered = True
        else:
            self.Triggered = False

    def sonicCheck(self):
        GPIO.output(self.config["trigger"], True)
        time.sleep(0.00001)
        GPIO.output(self.config["trigger"], False)
        start = time.time()
        while GPIO.input(self.config["echo"])==0:
            start = time.time()
        while GPIO.input(self.config["echo"])==1:
            stop = time.time()
        elapsed = stop-start
        measure = (elapsed * 34300)/2
        self.lastRead = measure
        if self.boundary > measure:
            print("Boundary breached")
            print(self.boundary)
            print(measure)
            self.Triggered = True
        else:
            self.Triggered = False

    sensorpins = {"IR1":{"echo":7, "check":iRCheck}, "IR2":{"echo":12, "check":iRCheck},
                  "ULTRASONIC":{"trigger":29, "echo": 31, "check":sonicCheck}}

    def trigger(self):
        ''' Executes the relevant routine that activates and takes a reading from the specified sensor.

        If the specified "boundary" has been breached the Sensor's Triggered attribute gets set to True.
    '''
        self.config["check"](self)
        print("Trigger Called")

    def __init__(self, sensortype, boundary):
        self.config = self.sensorpins[sensortype]
        self.boundary = boundary
        self.lastRead = 0
        if "trigger" in self.config:
            print("trigger")
            GPIO.setup(self.config["trigger"],GPIO.OUT)
        GPIO.setup(self.config["echo"],GPIO.IN)
