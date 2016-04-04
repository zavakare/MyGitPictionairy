#!/usr/bin/env python

#user chooses category and recieves drawing word

import Tkinter
from Tkinter import *
import random
import GamePlay
import loadArray
import tkMessageBox as box
import os

#stores information saved from entry boxes
cat = []
global ChosenWord

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
	array = []
	with open("category1.txt","r") as ins:
		lines = ins.readlines()
                for line in lines:
			words = line.split()
			for word in words:
                        	array.append(word)

	ChosenWord=random.choice (array)
	array.remove(ChosenWord)
	#open file which will save entries
        outf = open('category1.txt', 'w')
	#send each user entry into the file
        print>>outf, ' '.join(array)
	outf.close()
	outf = open('drawThis.txt', 'w')
	print >>outf, ChosenWord
	outf.close()
	os.system('./SendMessage.py')
	GamePlay.main()

def selectCat2() :
        array = []
        with open("category2.txt","r") as ins:
                lines = ins.readlines()
                for line in lines:
                        words = line.split()
                        for word in words:
                                array.append(word)

        ChosenWord=random.choice (array)
        array.remove(ChosenWord)
        #open file which will save entries
        outf = open('category1.txt', 'w')
        #send each user entry into the file
        print>>outf, ' '.join(array)
        outf.close()
        outf = open('drawThis.txt', 'w')
        print >>outf, ChosenWord
        outf.close()
        os.system('./SendMessage.py')
        GamePlay.main()
	
def selectCat3() :
        array = []
        with open("category3.txt","r") as ins:
                lines = ins.readlines()
                for line in lines:
                        words = line.split()
                        for word in words:
                                array.append(word)

        ChosenWord=random.choice (array)
        array.remove(ChosenWord)
        #open file which will save entries
        outf = open('category1.txt', 'w')
        #send each user entry into the file
        print>>outf, ' '.join(array)
        outf.close()
        outf = open('drawThis.txt', 'w')
        print >>outf, ChosenWord
        outf.close()
        os.system('./SendMessage.py')
        GamePlay.main()        
	
def selectCat4() :
        array = []
        with open("category4.txt","r") as ins:
                lines = ins.readlines()
                for line in lines:
                        words = line.split()
                        for word in words:
                                array.append(word)

        ChosenWord=random.choice (array)
        array.remove(ChosenWord)
        #open file which will save entries
        outf = open('category1.txt', 'w')
        #send each user entry into the file
        print>>outf, ' '.join(array)
        outf.close()
        outf = open('drawThis.txt', 'w')
        print >>outf, ChosenWord
        outf.close()
        os.system('./SendMessage.py')
        GamePlay.main()

if __name__ == "__main__":
	select()
