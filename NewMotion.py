#!/usr/bin/python
from SimpleCV import *


cam = Camera(prop_set = {"width":320,"height":240})

size = cam.getImage().size()
disp = Display(size)

lot=[]

#myDrawingLayer = DrawingLayer((320,240))
#myDrawingLayer.setDefaultColor("Black")

while True:

	img = cam.getImage().flipHorizontal()
	dist = img.colorDistance(Color.BLACK).dilate(2)

	segmented = dist.stretch(200,255)

	blobs = segmented.findBlobs()

	if blobs:

		circles = blobs.filter([b.isCircle(0.2) for b in blobs])
		print circles.coordinates()
		
		if circles:
			lot.append((circles[-1].x, circles[-1].y))
			img.drawCircle((circles[-1].x, circles[-1].y), circles[-1].radius(),Color.BLUE,3)
			#img.dl().circle((circles[-1].x, circles[-1].y), 6, Color.BLACK, width = 1, filled=True)
	for (x,y) in lot:
		img.dl().circle((x,y), 6, Color.BLACK, width = 2, filled=True)
#	for i in range(len(lot))
#		a, b=lot[i]
#		c, d=lot[i-1]
#		img.dl().line(start=
	#img.addDrawingLayer(myDrawingLayer)
	#img.applyLayers()
	img.show()
