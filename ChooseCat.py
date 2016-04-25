#!/usr/bin/env python

#user chooses category and recieves drawing word

import Tkinter
from Tkinter import *
import random
import GamePlay
import loadArray
import tkMessageBox
import os
from PIL import Image, ImageTk




#stores information saved from entry boxes
cat = []
global ChosenWord



#creates choose category window
def select():
        # initialize window size, title
        categoryPage = Toplevel()
       	categoryPage.minsize(1780,1080)
	
	imgCategory = Image.open("CategoryTitle.gif")
	renderCategory = ImageTk.PhotoImage(imgCategory)
	
	#Using Label to display our imgTitle
	imgCategoryL = Label(categoryPage, image=renderCategory,bg =  "Purple" )
	imgCategoryL.image = renderCategory
	imgCategoryL.place(x=300,y=40)



	categoryPage.configure(bg =  "Purple" )
        myvar = StringVar()
        categoryPage.title('Choose a category!')
	


	#opening Images
	imgAnimals = Image.open("AnimalsButton.gif")
        renderAnimals = ImageTk.PhotoImage(imgAnimals)
	imgComputer = Image.open("ComputerButton.gif")
        renderComputer = ImageTk.PhotoImage(imgComputer)
	imgFood = Image.open("foodButton.gif")
        renderFood = ImageTk.PhotoImage(imgFood)
	imgObject = Image.open("ObjectButton.gif")
        renderObject = ImageTk.PhotoImage(imgObject)

	#creates main menu  buttons
	button = Button(categoryPage, image=renderAnimals, command=selectCat1,bg = "Purple" )
	button2 = Button(categoryPage, image=renderComputer, command=selectCat2, bg = "Purple")
	button3 = Button(categoryPage, image=renderFood, command=selectCat3, bg = "Purple")
	button4 = Button(categoryPage, image=renderObject, command=selectCat4, bg = "Purple")
	
	#size of buttons
	button.config(height=200, width=400)
	button2.config(height=200, width=400)
	button3.config(height=200, width=400)
	button4.config(height=200, width=400)

	#placing of button
	button3.place(x=420, y=320)
	button2.place(x=920, y=320)
	button4.place(x=420, y=620)
	button.place(x=920, y=620)

	categoryPage.mainloop()


#picks random word to draw from specific array
#removes that word from array, and sends chosen word to touchscreen
# if category is empty, game automatically shuts down
def selectCat1() :
	array = []
	if(os.stat("category1.txt").st_size==0):
		tkMessageBox.showinfo("Error", "Empty category file. Game will now shutdown.")
		os.system("./killAllPython.sh")
	else:
		with open("Categories/category1.txt","r") as ins:
			lines = ins.readlines()
                	for line in lines:
				words = line.split()
				for word in words:
        	                	array.append(word)

		ChosenWord=random.choice (array)
		#open file which will save entries
        	outf = open('Categories/category1.txt', 'w')
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
        if(os.stat("category2.txt").st_size==0):
                tkMessageBox.showinfo("Error", "Empty category file. Game will now shutdown.")
                os.system("./killAllPython.sh")
        else:
	        with open("Categories/category2.txt","r") as ins:
        	        lines = ins.readlines()
                	for line in lines:
                        	words = line.split()
	                        for word in words:
        	                        array.append(word)

	        ChosenWord=random.choice (array)
        	#open file which will save entries
	        outf = open('Categories/category2.txt', 'w')
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
        if(os.stat("category3.txt").st_size==0):
                tkMessageBox.showinfo("Error", "Empty category file. Game will now shutdown.")
                os.system("./killAllPython.sh")
        else:
	        with open("Categories/category3.txt","r") as ins:
        	        lines = ins.readlines()
                	for line in lines:
	                        words = line.split()
        	                for word in words:
                	                array.append(word)

	        ChosenWord=random.choice (array)
	        #open file which will save entries
	        outf = open('Categories/category3.txt', 'w')
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
	if(os.stat("category4.txt").st_size==0):
                tkMessageBox.showinfo("Error", "Empty category file. Game will now shutdown.")
                os.system("./killAllPython.sh")
        else:

	        with open("Categories/category4.txt","r") as ins:
        	        lines = ins.readlines()
	                for line in lines:
	                        words = line.split()
	                        for word in words:
	                                array.append(word)

        	ChosenWord=random.choice (array)
	        #open file which will save entries
	        outf = open('Categories/category4.txt', 'w')
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
