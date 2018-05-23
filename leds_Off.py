#!/usr/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
print "Lights On"
GPIO.output(32,GPIO.LOW)
GPIO.output(36,GPIO.LOW)
