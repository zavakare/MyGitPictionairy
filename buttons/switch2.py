#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	if GPIO.input(18) == GPIO.LOW:
		print "Button 1 pressed"
		break
	if GPIO.input(22) == GPIO.LOW:
		print "button 2 pressed"
		break
		
