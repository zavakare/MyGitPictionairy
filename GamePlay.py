#!/usr/bin/env python 
 
from Tkinter import *
import threading
import NewMotion

def openDrawing():
	NewMotion.drawFunction()

sec = 45

def tick():
	global sec 
	if (sec <=  0):
		time['text']='stop'
	else:
		sec = sec - 1
		time['text'] = sec
		# Take advantage of the after method of the Label
		time.after(1000, tick)

def combo():
	t=threading.Thread(target=openDrawing)
	t.start()
	tick()

def main():
	#create blank window and set minimum size
	root = Tk()
	root.minsize(1780, 1080)
	root.title('Timer')

	global time
	time = Label(root, fg='green', font=("Helvetica", 76))
	time.pack()
	Button(root, fg='blue', text='Start', command=combo).pack()
	root.mainloop()

if __name__ == "__main__":
	main()

