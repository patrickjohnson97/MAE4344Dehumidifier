import RPi.GPIO as GPIO

FAN_IN1_PIN = 21
FAN_IN2_PIN = 20
FAN_IN3_PIN = 16

GPIO.setup(FAN_IN1_PIN, GPIO.OUT)
GPIO.setup(FAN_IN2_PIN, GPIO.OUT)
GPIO.setup(FAN_IN3_PIN, GPIO.OUT)

def turnOffFan():
    GPIO.output(FAN_IN3_PIN, GPIO.HIGH)
    GPIO.output(FAN_IN2_PIN, GPIO.HIGH)
    GPIO.output(FAN_IN1_PIN, GPIO.HIGH)

def setSlowSpeed():
    GPIO.output(FAN_IN3_PIN, GPIO.LOW)
    GPIO.output(FAN_IN2_PIN, GPIO.HIGH)
    GPIO.output(FAN_IN1_PIN, GPIO.HIGH)

def setMediumSpeed():
    GPIO.output(FAN_IN3_PIN, GPIO.HIGH)
    GPIO.output(FAN_IN2_PIN, GPIO.LOW)
    GPIO.output(FAN_IN1_PIN, GPIO.HIGH)

def setMaximumSpeed():
    GPIO.output(FAN_IN3_PIN, GPIO.HIGH)
    GPIO.output(FAN_IN2_PIN, GPIO.HIGH)
    GPIO.output(FAN_IN1_PIN, GPIO.LOW)
