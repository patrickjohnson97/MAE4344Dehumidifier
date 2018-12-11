import RPi.GPIO as GPIO
import Adafruit_ADS1x15

# this method is used to sample analog signals from the MUX.
# fill in the SO,S1,S2,S3 pins and the number of them you'll be reading
NUM_PINS_TO_READ = 4

# DO NOT MESS WITH THE GAIN PLEASE!
GAIN = 1
adc = Adafruit_ADS1x15.ADS1015()

def sampleAnalog():
    pinList = [MUX_S0_PIN, MUX_S1_PIN, MUX_S2_PIN, MUX_S3_PIN]
    for k in pinList:
        GPIO.setup(k, GPIO.OUT)
    # mux selector
    for i in range(NUM_PINS_TO_READ):
        temp = i
        count = [0,0,0,0]
        for b in range(4):
            count[3-b] = temp%2
            temp = temp/2
        for j in range(4):
            if count[j] == 1:
                GPIO.output(pinList[j], GPIO.HIGH)
                # debug = str(pinList[j]) + " is set to high"
                # print(debug)
            else:
                GPIO.output(pinList[j], GPIO.LOW)
                #debug = str(pinList[j]) + " is set to low"
                #print(debug)

        # Read the specified ADC channel using the previously set gain value.
        # The default channel for ADC reading is 0. If you want more ADC channels, you will
        # need to connect some more wires to the pi
        value = adc.read_adc(0, gain=GAIN)
        vstring = "ADC Voltage from channel ["+str(i) + "] : " + str(value)
        print(vstring)
    return 0
