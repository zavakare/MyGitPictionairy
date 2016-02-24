#!/usr/bin/env python 

from Tkinter import *

#create blank window
root = Tk()

root.minsize(500,500)

#create text
title = Label(root, text='pictionAIRy')

#put text on the screen
#can't choose where with this code need to find more exact code
title.pack()

def closewindow():
	exit()

def listrules():
	print "Rules listed"
	root2 = Tk()
	title2 = Label(root2, text='maybe this works...')
	title2.pack()
	root2.mainloop()
button = Button(root, text="Exit", command=closewindow)
button2 = Button(root, text="Rules", command=listrules)
button.pack()
button2.pack()

#display window on screen
root.mainloop()
