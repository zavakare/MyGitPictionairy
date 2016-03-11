#!/usr/bin/env python

#user chooses category and recieves drawing word

import Tkinter
from Tkinter import *
import random
import GamePlay
import startGame
import loadArray
import tkMessageBox as box

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
	button2 = Button(root, text="Computer", command=selectCat2, font=("Georgia", 40))
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


#picks random word to draw from specific array, removes that word from array, and displays chosen word in message box

def selectCat1() :
	
	global ChosenWord	
	ChosenWord=random.choice (loadArray.array)
	print ChosenWord
	loadArray.array.remove(ChosenWord)
	print loadArray.array
	print ChosenWord
	root = Tk().withdraw()
	var = box.showinfo('Draw This Word',ChosenWord)
	GamePlay.main()

def selectCat2() :
        
	global ChosenWord
	ChosenWord=random.choice (loadArray.array2)
        print ChosenWord
        loadArray.array2.remove(ChosenWord)
        print loadArray.array2
        print ChosenWord
	var = box.showinfo('Draw This Word',ChosenWord)
	GamePlay.main()
		
def selectCat3() :
        
	global ChosenWord
        ChosenWord=random.choice (loadArray.array3)
        print ChosenWord
        loadArray.array3.remove(ChosenWord)
        print loadArray.array3
        print ChosenWord
	var = box.showinfo('Draw This Word',ChosenWord)
	GamePlay.main()
	
def selectCat4() :
	
	global ChosenWord
        ChosenWord=random.choice (loadArray.array4)
        print ChosenWord
        loadArray.array4.remove(ChosenWord)
        print loadArray.array4
        print ChosenWord
	var = box.showinfo('Draw This Word',ChosenWord)
	GamePlay.main()
