#!/usr/bin/python

#Camera for pictionAIRy
#2/17/16
#Mary/ Alex/ Sam/ Karen/ Theodora

# import simplecv and camera
from SimpleCV import Camera

#initialize camera
cam = Camera()

# Loop to continuously get images
while True:

    # Get Image from camera
	 img = cam.getImage()

    # Show the image
	 img.show()
