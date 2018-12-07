import RPi.GPIO as GPIO

PUMP_IN1_PIN = 12

GPIO.setup(PUMP_IN1_PIN, GPIO.OUT)


def turnOnWaterPump():
    GPIO.output(PUMP_IN1_PIN, GPIO.LOW)

def turnOffWaterPump():
    GPIO.output(PUMP_IN1_PIN, GPIO.HIGH)
