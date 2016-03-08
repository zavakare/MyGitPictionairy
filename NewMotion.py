#!/usr/bin/python
from SimpleCV import *

#Defines camera and resolution

cam = Camera(prop_set = {"width":320,"height":240})

#creates array where tracked center coordinates will be stored
lot=[]


while True:
	#display=SimpleCV.Display((800,600))
	#get image from camera
	img = cam.getImage().flipHorizontal()
	#want to track object whose color is furthest distance from black
	dist = img.colorDistance(Color.BLUE).dilate(2)

	segmented = dist.stretch(200,255)
	#find blobs in image
	blobs = segmented.findBlobs()

	if blobs:
		#from the blobs which have been found, find circles
		circles = blobs.filter([b.isCircle(0.2) for b in blobs])
		
		if circles:
			lot.append((circles[-1].x, circles[-1].y))
			#outline the found circle in blue on the screen
			img.drawCircle((circles[-1].x, circles[-1].y), circles[-1].radius(),Color.BLUE,3)
	#as long as there is more than 1 point in the list, draw lines between the points
	if (len(lot)>1):
		img.dl().lines(lot, color=(255,0,0), antialias=True, alpha=-1, width=5)
	#display image (camera picture) on the screen
	img.show()
