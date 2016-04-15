#!/usr/bin/env python

# allows users to enter team names and player names

import Tkinter
from Tkinter import *
import ChooseCat
import loadArray

#stores information saved from entry boxes
info = []


#keeps track of round number, and which player from each team is drawing next
#global roundNumber
#roundNumber=1
#global team1Drawing
#team1Drawing=0
#global team2Drawing
#team2Drawing=0

#keeps tracks of current score
#global team1Score
#team1Score=0
#global team2Score
#team2Score=0


def mainStart():
	# initialize window size, title
	root = Tk()
	root.minsize(1780,1080)
	root.configure(bg =  "Purple" )
	myvar = StringVar()
	root.title('It is time to make our teams!')
	
	#team 1 enters team name
	Label(root, text='Team 1 enter your team name:', bg = "Purple", font=("Georgia", 17)).pack(side=TOP,padx=10,pady=10)
	team1Entry = Entry(root, width=10, textvariable=myvar)
	team1Entry.pack(side=TOP,padx=10,pady=10)
	
	#team 1 player 1 enters own name
	Label(root, text='Team 1: Player 1 enter your name:', bg = "Purple", font=("Georgia", 17) ).pack(side=TOP,padx=10,pady=10)
	t1player1Entry = Entry(root, width=10)
	t1player1Entry.pack(side=TOP,padx=10,pady=10)

	#team 1 player 2 enters own name
	Label(root, text='Team 1: Player 2 enter your name:', bg = "Purple", font=("Georgia", 17)).pack(side=TOP,padx=10,pady=10)
	t1player2Entry = Entry(root, width=10)
	t1player2Entry.pack(side=TOP,padx=10,pady=10)

	#team 2 enters name
	Label(root, text='Team 2 enter your team name:', bg = "Purple", font=("Georgia", 17)).pack(side=TOP,padx=10,pady=10)
	team2Entry = Entry(root, width=10)
	team2Entry.pack(side=TOP,padx=10,pady=10)

	#team 2 player 1 enters own name
	Label(root, text='Team 2: Player 1 enter your name:', bg = "Purple", font=("Georgia", 17)).pack(side=TOP,padx=10,pady=10)
	t2player1Entry = Entry(root, width=10)
	t2player1Entry.pack(side=TOP,padx=10,pady=10)

	#team 2 player 2 enters own name
	Label(root, text='Team 2: Player 2 enter your name:', bg = "Purple", font=("Georgia", 17)).pack(side=TOP,padx=10,pady=10)
	t2player2Entry = Entry(root, width=10)
	t2player2Entry.pack(side=TOP,padx=10,pady=10)

	#is called when Ready to Play button is pressed
	def SaveInfo():
		#gets text from each entry box and saves it in array
	        info.append(team1Entry.get())
		info.append(t1player1Entry.get())
		info.append(t1player2Entry.get())
		info.append(team2Entry.get())
		info.append(t2player1Entry.get())
		info.append(t2player2Entry.get())

		#open file which will save entries
        	outf = open('savedNames.txt', 'w')
		#send each user entry into the file
	       	for item in info:
		        print>>outf, item
	        outf.close()
		#initializes round number, team 1 member drawing, team 2 member drawing,
		#team 1 score, team 2 score
		outf = open('roundInfo.txt', 'w')
		outf.write('1,0,0,0,0')
                outf.close()

		loadArray.arrayOne()
		loadArray.arrayTwo()
		loadArray.arrayThree()
		loadArray.arrayFour()
		ChooseCat.select()
	
	#Ready to Play button
	Button(root, text='READY TO PLAY', command = SaveInfo).pack()
	

	root.mainloop()


if __name__ == "__main__":
	mainStart()

