import RPi.GPIO as GPIO

COMPRESSOR_IN1_PIN = 15
COMPRESSOR_IN2_PIN = 14

GPIO.setup(COMPRESSOR_IN1_PIN, GPIO.OUT)
GPIO.setup(COMPRESSOR_IN2_PIN, GPIO.OUT)

# Note: Minimum speed of the compressor we were using was 1800 RPM
def setMinimumSpeed():
    GPIO.output(COMPRESSOR_IN1_PIN, GPIO.HIGH)
    GPIO.output(COMPRESSOR_IN2_PIN, GPIO.HIGH)

def setSecondSlowestSpeed():
    GPIO.output(COMPRESSOR_IN1_PIN, GPIO.LOW)
    GPIO.output(COMPRESSOR_IN2_PIN, GPIO.HIGH)

def setSecondFastestSpeed():
    GPIO.output(COMPRESSOR_IN1_PIN, GPIO.HIGH)
    GPIO.output(COMPRESSOR_IN2_PIN, GPIO.LOW)

# Note: Maximum speed of compressor we were using was 3600 RPM
def setMaximumSpeed():
    GPIO.output(COMPRESSOR_IN1_PIN, GPIO.LOW)
    GPIO.output(COMPRESSOR_IN2_PIN, GPIO.LOW)
