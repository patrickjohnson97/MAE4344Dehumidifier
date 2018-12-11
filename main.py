# PLEASE WRITE YOUR OWN CODE
# THIS CODE WAS WRITTEN TO INTERFACE WITH FIREBASE DATABASE AND IOS APP
# DO NOT USE THIS CODE IN PRODUCTION
# USE THE CLASSES ON GITHUB TO WRITE YOUR OWN MAIN.PY

'''
Copyright (C) 2018 Patrick Johnson - All Rights Reserved
   You may use, distribute and modify this code under the
   terms of the XYZ license, which unfortunately won't be
   written for another century.

   You should have received a copy of the XYZ license with
   this file. If not, please write to: patrick@patrickjohnson.co
'''

import Adafruit_DHT
import RPi.GPIO as GPIO
import os
import glob
from google.cloud import firestore
import time
import Adafruit_ADS1x15
import smtplib
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

# mh = Adafruit_MotorHAT(addr = 0x70)
# myStepper = mh.getStepper(200,1)
# myStepper.setSpeed(30)


numDS = 10
numDHT = 5
INTAKE_AIR_PIN = 8

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/mae4344-5859b-firebase-adminsdk-joh4j-b785a3a6c9.json"
os.environ["GCLOUD_PROJECT"] = "mae4344-5859b"
db = firestore.Client()

GAIN = 1
adc = Adafruit_ADS1x15.ADS1015()
tankCapacity = 55.0
ADC_SDA_PIN = 2
ADS_SCL_PIN = 3
DS18B20_PIN = 4
MUX_S0_PIN = 17
MUX_S1_PIN = 18
MUX_S2_PIN = 27
MUX_S3_PIN = 22
DAMPER_IN1_PIN = 24
DAMPER_IN2_PIN = 23
COMPRESSOR_IN1_PIN = 15
COMPRESSOR_IN2_PIN = 14
DHT_LOC1_PIN = 10
DHT_LOC2_PIN = 9
DHT_LOC3_PIN = 11
DHT_LOC4_PIN = 25
DHT_LOC5_PIN = 8
FAN_IN1_PIN = 21
FAN_IN2_PIN = 20
FAN_IN3_PIN = 16
PUMP_IN1_PIN = 12
relayPinList = [FAN_IN1_PIN, FAN_IN2_PIN, FAN_IN3_PIN, PUMP_IN1_PIN, DAMPER_IN1_PIN, DAMPER_IN2_PIN, COMPRESSOR_IN1_PIN, COMPRESSOR_IN2_PIN]

def getMode():
	modes_ref = db.collection(u'modes')
	modes = modes_ref.get()
	for mode in modes:
		diction = mode.to_dict()
		num = int(diction.get("value"))
	return num


def sendEmail(msg):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	# Next, log in to the server
	server.login("okstatedehumidifier@gmail.com", "dehumidify4344")
	print("About to email...")
	# Send the mail
	msgToSend = "User, \n" \
		  "The dehumidifier has issued the following alert: \n" \
		  "\t-"+msg+"\n" \
					"Have a nice day!" # The /n separates the message from the headers
	server.sendmail("okstatedehumidifier@gmail.com", "pjsoccer97@gmail.com", msgToSend)
	print("Email sent!")
	return 0


def setUpRelays():

	for i in relayPinList:
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, GPIO.HIGH)
	return 0


def getHumidity():
	humidity_ref = db.collection(u'humidity')
	humids = humidity_ref.get()
	for humid in humids:
		diction2 = humid.to_dict()
		humidity = float(diction2.get("value"))
		humidity = round(humidity, 1)
	return humidity


def getCapacity():
	capacity_ref = db.collection(u'capacity')
	caps = capacity_ref.get()
	for cap in caps:
		diction3 = cap.to_dict()
		capacity = float(diction3.get("value"))
		capacity = round(capacity, 1)
	return capacity


def sendWaterTemperature(waterTemp):
	wtemp_ref = db.collection(u'watertemps').document(u'watertemp')

	wtemp_ref.set({
		u'value': waterTemp
	}, merge=True)
	return 0


def sendAirTemperature(airTemp):
	atemp_ref = db.collection(u'airtemps').document(u'airtemp')

	atemp_ref.set({
		u'value': airTemp
	}, merge=True)
	return 0


def sendAirHumidity(airHum):
	aHum_ref = db.collection(u'airhumidities').document(u'humidity')

	aHum_ref.set({
		u'value': airHum
	}, merge=True)
	return 0

def sendCFM(cfmToSend):
	s = 3.0*((abs(cfmToSend)/(5.0*500)*0.5)**0.5) * 4004.4*0.82*(1.0/18.0)
	s = round(s,1)
	cfmRef = db.collection(u'cfm').document(u'cfm')

	cfmRef.set({
		u'value': s
	}, merge=True)
	return 0

def sendIntakeTemperature():
	inRef = db.collection(u'airhumidities').document(u'humidity')
	intake = getIntakeAirHumidity()
	inRef.set({
		u'value': intake
	}, merge=True)


STOP_EMAILING = False


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
	sendCapacity(31.1)
	global STOP_EMAILING

	if (temp > 28.3) and (not STOP_EMAILING):
		#sendEmail(msg="The water temperature has exceeded 28.5 degrees Celsius.")
		STOP_EMAILING = True
	return temp,roughCapacity

#FILL IN PINS

def sampleAnalog():
	pinList = [MUX_S0_PIN, MUX_S1_PIN, MUX_S2_PIN, MUX_S3_PIN]
	for k in pinList:
		GPIO.setup(k, GPIO.OUT)
	# mux selector
	for i in range(4):
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
		value = adc.read_adc(0, gain=GAIN)
		if(i == 0):
			sendCFM(value)
		vstring = "ADC Voltage from channel ["+str(i) + "] : " + str(value)
		print(vstring)
	return 0

def openExpansionValve():
	myStepper.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)

def closeExpansionValve():
	myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)



def shutdown():
	for i in relayPinList:
		GPIO.output(i, GPIO.HIGH)
	print("Shutting down")
	return 0

humEpsilon = 1.0

def highEfficiencyMode(tHum, tCap, curCap):
	print("High Efficiency Mode Active")
	intakeHumidity = getIntakeAirHumidity()
	if (intakeHumidity > tHum + tCap):
		print("Air is more humid than target, dehumidification in process")

		# damper control (close)

		GPIO.output(23, GPIO.LOW)
		GPIO.output(24, GPIO.HIGH)

		# fan control (medium)
		GPIO.output(20, GPIO.LOW)
		GPIO.output(21, GPIO.HIGH)
		GPIO.output(16, GPIO.HIGH)


	elif (intakeHumidity > tHum - humEpsilon):
		print("Air at target humidity")
		# fan control (slow)
		GPIO.output(16, GPIO.LOW)
		GPIO.output(21, GPIO.HIGH)
		GPIO.output(20, GPIO.HIGH)
		return
	else:
		print("Air is less humid than target, slowing down in process")

		# damper control (open)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(23, GPIO.HIGH)

		# fan control (slow)
		GPIO.output(16, GPIO.LOW)
		GPIO.output(21, GPIO.HIGH)
		GPIO.output(20, GPIO.HIGH)
	if (curCap < threshCapacity - 4):
		print("Capacity less than target, heating in process")

		# turnOnWaterPump()
		GPIO.output(PUMP_IN1_PIN, GPIO.LOW)

		# fan control (medium)
		GPIO.output(20, GPIO.LOW)
		GPIO.output(21, GPIO.HIGH)
		GPIO.output(16, GPIO.HIGH)

		# damper control (open)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(23, GPIO.HIGH)

	elif (curCap < threshCapacity + 4):
		print("Capacity has reached target level")

		# fan control (slow)
		GPIO.output(16, GPIO.LOW)
		GPIO.output(21, GPIO.HIGH)
		GPIO.output(20, GPIO.HIGH)
		return
	else:
		print("Capacity more than target, slowing down in process")

		# turnOffWaterPump()
		GPIO.output(PUMP_IN1_PIN, GPIO.HIGH)

		# fan control (slow)
		GPIO.output(16, GPIO.LOW)
		GPIO.output(21, GPIO.HIGH)
		GPIO.output(20, GPIO.HIGH)

		# closeExpansionValve()

		# damper control (close)
		GPIO.output(23, GPIO.LOW)
		GPIO.output(24, GPIO.HIGH)

	return 0

def dehumidifyMode(threshHumidity):
	# intakeHumidity = getIntakeAirHumidity(intakePin)
	GPIO.output(PUMP_IN1_PIN, GPIO.HIGH)
	print("Dehumidify mode active")
	intakeHumidity = getIntakeAirHumidity()
	if(intakeHumidity>threshHumidity+humEpsilon):
		print("Air is more humid than target, dehumidification in process")

		# damper control (close)

		GPIO.output(23, GPIO.LOW)
		GPIO.output(24, GPIO.HIGH)

		# fan control (maximum)
		GPIO.output(21, GPIO.LOW)
		GPIO.output(20, GPIO.HIGH)
		GPIO.output(16, GPIO.HIGH)

		# reduce compressor speed if possible
		# GPIO.output(14, GPIO.HIGH)
		# GPIO.output(15, GPIO.HIGH)

		# closeExpansionValve()

	elif(intakeHumidity>threshHumidity-humEpsilon):
		print("Air at target humidity")
		# Keep Compressor speed at medium
		# GPIO.output(15, GPIO.LOW)
		# GPIO.output(14, GPIO.HIGH)
		return
	else:
		print("Air is less humid than target, slowing down in process")

		# damper control (open)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(23, GPIO.HIGH)

		# fan control (medium)
		GPIO.output(20, GPIO.LOW)
		GPIO.output(21, GPIO.HIGH)
		GPIO.output(16, GPIO.HIGH)

		# increase compressor speed if possible
		# GPIO.output(15, GPIO.HIGH)
		# GPIO.output(14, GPIO.LOW)

		# openExpansionValve()
	

# def getHotWaterCapacity():
# 	count = 0.0
# 	for sensor in glob.glob("/sys/bus/w1/devices/28*/w1_slave"):
# 		id = sensor.split("/")[5]
# 		count = 0.0
# 		try:
# 			f = open(sensor, "r")
# 			data = f.read()
# 			f.close()
# 			if "YES" in data:
# 				(discard, sep, reading) = data.partition(' t=')
# 				t = float(reading) / 1000.0
# 				if(t>30.0):
# 					count = count+1
#
# 				# print("{} {:.1f}".format(id, t))
# 			else:
# 				print("999.9")
# 		except IOError:
# 			print "Could not read file:", sensor
# 	percentage = count / numDS
# 	roughCapacity = percentage * tankCapacity
# 	global STOP_EMAILING
#
# 	if (percentage < 1) and (not STOP_EMAILING):
# 		# sendEmail(msg="You ran out of hot water! Turn on hot water to expedite hot water production")
# 		STOP_EMAILING = True
# 	return roughCapacity

def sendCapacity(capacity):
	capRef = db.collection(u'waterCapacity').document(u'cap')
	capRef.set({
		u'value': capacity
	}, merge=True)
	return 0

def hotWaterMode(threshCapacity,c):
	# c = getHotWaterCapacity()
	print("Hot water mode active")
	if(c<threshCapacity-4):
		print("Capacity less than target, heating in process")

		#turnOnWaterPump()
		GPIO.output(PUMP_IN1_PIN, GPIO.LOW)

		# increase compressor speed if possible
		GPIO.output(15, GPIO.HIGH)
		GPIO.output(14, GPIO.LOW)

		# fan control (maximum)
		GPIO.output(21, GPIO.LOW)
		GPIO.output(20, GPIO.HIGH)
		GPIO.output(16, GPIO.HIGH)

		# damper control (open)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(23, GPIO.HIGH)


		# openExpansionValve()

	elif(c<threshCapacity+4):
		print("Capacity has reached target level")
		GPIO.output(15, GPIO.LOW)
		GPIO.output(14, GPIO.HIGH)
		return
	else:
		print("Capacity more than target, slowing down in process")

		#turnOffWaterPump()
		GPIO.output(PUMP_IN1_PIN, GPIO.HIGH)

		# decrease compressor speed if possible
		GPIO.output(14, GPIO.HIGH)
		GPIO.output(15, GPIO.HIGH)

		# fan control (medium)
		GPIO.output(20, GPIO.LOW)
		GPIO.output(21, GPIO.HIGH)
		GPIO.output(16, GPIO.HIGH)

		# closeExpansionValve()

		# damper control (close)
		GPIO.output(23, GPIO.LOW)
		GPIO.output(24, GPIO.HIGH)



sensor = Adafruit_DHT.DHT22

dhtPinList = [9,10,11, 8, 25]


def getAirTemp():
	temp = 0.0
	hum = 0.0
	for i in dhtPinList:
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

def getAirHumidity():
	hum = 0.0
	for i in dhtPinList:
		humidity, temperature = Adafruit_DHT.read_retry(sensor, i)
		hum += humidity
	hum = hum/numDHT
	hum = round(hum, 1)
	humString = "Air Humidity: " + str(hum)
	print(humString)
	return hum

INTAKE_AIR_PIN = 8
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

setUpRelays()
count = 0
try:
	while(True):
		count = count+1
		if(count % 6000) == 0:
			STOP_EMAILING = False

		wTemp , c = readWaterTemperature()
		sendWaterTemperature(waterTemp=wTemp)
		aTemp, aHum = getAirTemp()
		sendAirTemperature(airTemp=aTemp)
		# aHum = getAirHumidity()
		sendAirHumidity(airHum=aHum)
		sampleAnalog()
		threshCapacity = getCapacity()
		capString = "Capacity: "+str(threshCapacity)
		threshHumidity = getHumidity()
		humString = "Humidity: "+str(threshHumidity)
		print(capString)
		print(humString)
		mode = getMode()
		# sendCapacity()
		# sendIntakeTemperature()
		# High Efficiency Mode
		if mode == 0:
			highEfficiencyMode(threshHumidity, threshCapacity, 31.1)

		# Dehumidify Mode
		if mode == 1:
			dehumidifyMode(threshHumidity)

		# Hot Water Mode
		if mode == 2:
			hotWaterMode(threshCapacity, 31.1)
		time.sleep(1)
		print
		print

except KeyboardInterrupt:
	shutdown()

