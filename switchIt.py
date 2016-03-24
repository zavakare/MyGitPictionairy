#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import whatever

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

hey = True

while hey==True:
	input_state = GPIO.input(18)
	if input_state == False:
		print "In the switchIt file"
		whatever.pressed += 1
		print whatever.pressed
		print "Button pressed"
		hey = False
		time.sleep(0.2)
print whatever.pressed
