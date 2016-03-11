#!/usr/bin/env python 
 
#creates Timer, calls motion, and checks chosen word with guess

from Tkinter import *
import threading
import ChooseCat
import NewMotion
import tkSimpleDialog

# calls motion function
def openDrawing():
	NewMotion.drawFunction()

#sets clock to 45 seconds
sec = 45

#creates timer and creates dialog that checks guess word with chosen word
def tick():
	global sec 
	if (sec <=  0):
		time['text']='stop'
		global result
		result = tkSimpleDialog.askstring("Ask Audience", "What is your guess?")
		if(result == ChooseCat.ChosenWord):
			print("Winner")
			print(ChooseCat.ChosenWord)
		else:
			print("Nope")
			print(result)
			print(ChooseCat.ChosenWord)
		
	else:
		sec = sec - 1
		time['text'] = sec
		# Take advantage of the after method of the Label
		time.after(1000, tick)

#combines timer and openDrawing call
def combo():
	t=threading.Thread(target=openDrawing)
	t.start()
	tick()

#calls timer and creates window
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
