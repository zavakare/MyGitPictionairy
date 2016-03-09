#!/usr/bin/env python

import Tkinter
from Tkinter import *
import random

#stores information saved from entry boxes
cat = []

def select():
        # initialize window size, title
        root = Tk()
        root.minsize(1780,1080)
        myvar = StringVar()
        root.title('Choose a category!')

	#creates main menu  buttons
	button = Button(root, text="Animals", command=selectCat1, font=("Georgia", 40))
	button2 = Button(root, text="Holidays", command=selectCat2, font=("Georgia", 40))
	button3 = Button(root, text="Food", command=selectCat3, font=("Georgia", 40))
	button4 = Button(root, text="Objects", command=selectCat4, font=("Georgia", 40))

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

	root.mainloop()

def selectCat1() :
	with open("category1.txt","r") as ins:
                array = []
                for line in ins:
                        array.append(line)
	ChosenWord=random.choice (array)
	print ChosenWord
	array.remove(ChosenWord)
	print array
	print ChosenWord	
def selectCat2() :
        with open("category2.txt","r") as ins:
		array = []
		for line in ins:
			array.append(line)
	ChosenWord=random.choice (array)
        print ChosenWord
        array.remove(ChosenWord)
        print array
        print ChosenWord

	
def selectCat3() :
        with open("category3.txt","r") as ins:
                array = []
                for line in ins:
                        array.append(line)
        ChosenWord=random.choice (array)
        print ChosenWord
        array.remove(ChosenWord)
        print array
        print ChosenWord



def selectCat4() :
	with open("category4.txt","r") as ins:
                array = []
                for line in ins:
                        array.append(line)
        ChosenWord=random.choice (array)
        print ChosenWord
        array.remove(ChosenWord)
        print array
        print ChosenWord


#if__name__ == "__main__":
 #       mainStart()

