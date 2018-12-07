import Adafruit_DHT


# Fill in this pin list with whatever pins you connect the dht data wires to.
DHTPinList = [DHTPIN1,DHTPIN2,DHTPIN3,DHTPIN4,DHTPIN5]

INTAKE_AIR_PIN = DHTPIN1

# This is how many DHT sensors you have connected to the Pi
numDHT = len(DHTPinList)
def getAverageAirTemp():
    temp = 0.0
    hum = 0.0
    for i in DHTPinList:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, i)
        temp += temperature
        hum += humidity
    temp = temp/numDHT
    temp = round(temp,1)
    tempString = "Air Temperature: "+ str(temp)
    hum = hum / numDHT
    hum = round(hum, 1)
    humString = "Air Humidity: " + str(hum)
    print(tempString)
    print(humString)
    return temp,hum

def getAverageAirHumidity():
    hum = 0.0
    for i in DHTPinList:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, i)
        hum += humidity
    hum = hum/numDHT
    hum = round(hum, 1)
    humString = "Air Humidity: " + str(hum)
    print(humString)
    return hum

def getIntakeAirHumidity():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, INTAKE_AIR_PIN)

    humidity = round(humidity, 1)
    humString = "Intake Air Humidity: " + str(humidity)
    print(humString)
    return humidity

def getIntakeAirTemperature():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, INTAKE_AIR_PIN)

    temperature = round(temperature, 1)
    tempString = "Intake Air Temperature: " + str(temperature)
    print(tempString)
    return temperature
