import RPi.GPIO as GPIO

DAMPER_IN1_PIN = 24
DAMPER_IN2_PIN = 23

GPIO.setup(DAMPER_IN1_PIN, GPIO.OUT)
GPIO.setup(DAMPER_IN2_PIN, GPIO.OUT)

def openDamper():
    GPIO.output(DAMPER_IN1_PIN, GPIO.LOW)
    GPIO.output(DAMPER_IN2_PIN, GPIO.HIGH)

def closeDamper():
    GPIO.output(DAMPER_IN1_PIN, GPIO.HIGH)
    GPIO.output(DAMPER_IN2_PIN, GPIO.LOW)


# Note: the damper will stop on its own when it reaches maximum open or closed state
def stopMotion():
    GPIO.output(DAMPER_IN1_PIN, GPIO.HIGH)
    GPIO.output(DAMPER_IN2_PIN, GPIO.HIGH)
