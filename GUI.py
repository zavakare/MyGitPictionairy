#!/usr/bin/env python 

from Tkinter import *

#create blank window
root = Tk()

root.minsize(1900,1080)
root.configure(bg =  "Purple" )
root.title("The Reflections + Alex presents: pictionAIRy")
#create text
title = Label(root, text='pictionAIRy', font=("Helvetica", 76), fg="Black", bg = "Purple" )

#put text on the screen
#can't choose where with this code need to find more exact code
title.pack()

def closewindow():
	exit()

def listrules():
	print "Rules listed"

#creates buttons
button = Button(root, text="Exit", command=closewindow, font=("Georgia", 40))
button2 = Button(root, text="Rules", command=listrules, font=("Georgia", 40))
button3 = Button(root, text="Start", command=closewindow, font=("Georgia", 40))
button4 = Button(root, text="About Us", command=closewindow, font=("Georgia", 40))

#size of buttons
button.config(height=3, width=7)
button2.config(height=3, width=7)
button3.config(height=3, width=7)
button4.config(height=3, width=7)

#placing of button
button3.place(x=520, y=320)
button2.place(x=920, y=320)
button4.place(x=520, y=520)
button.place(x=920, y=520)

#display window on screen
root.mainloop()
