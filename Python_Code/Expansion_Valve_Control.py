from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import RPi.GPIO as GPIO


mh = Adafruit_MotorHAT(addr = 0x70)
myStepper = mh.getStepper(200,1)
myStepper.setSpeed(30)


def openExpansionValve():
    myStepper.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)


def closeExpansionValve():
    myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)
