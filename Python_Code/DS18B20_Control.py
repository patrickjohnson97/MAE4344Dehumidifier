# Written by Patrick Johnson
# 12-12-2018
# This method allows you to sample the values of the DS18B20s by using their built in one-wire interface.
# This took so long to figure out, but it is actually hella cool, just trust me
import os
import glob
import sys


# This represents the number of DS18B20 sensors that are connected to the Pi at once, the default is 10
numDS = 10
# This represents the capacity of the connected water tank, the default is 55 gal
tankCapacity = 55.0
def readWaterTemperature():
    temp = 0.0
    count = 0.0
    for sensor in glob.glob("/sys/bus/w1/devices/28*/w1_slave"):
        id = sensor.split("/")[5]

        try:
            f = open(sensor, "r")
            data = f.read()
            f.close()
            if "YES" in data:
                (discard, sep, reading) = data.partition(' t=')
                t = float(reading) / 1000.0
                temp += t
                if (t > 30.0):
                    count = count + 1.0
                print("{} {:.1f}".format(id, t))
            else:
                print("999.9")
        except IOError:
            print "Could not read file:", sensor
    temp = temp / numDS
    temp = round(temp, 1)
    percentage = count / numDS
    roughCapacity = percentage * tankCapacity
    return temp,roughCapacity
