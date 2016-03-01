#!/usr/bin/env python


import Tkinter
from Tkinter import *

def mainStart():
	root = Tk()
	root.minsize(1780,1080)
	root.title('It is time to make our teams!')
	Label(root, text='Team 1 enter your team name:').pack(side=TOP,padx=10,pady=10)

	team1Entry = Entry(root, width=10)
	team1Entry.pack(side=TOP,padx=10,pady=10)

	Label(root, text='Team 1: Player 1 enter your name:').pack(side=TOP,padx=10,pady=10)

	player1Entry1 = Entry(root, width=10)
	player1Entry1.pack(side=TOP,padx=10,pady=10)

	Label(root, text='Team 1: Player 2 enter your name:').pack(side=TOP,padx=10,pady=10)

	player2Entry1 = Entry(root, width=10)
	player2Entry1.pack(side=TOP,padx=10,pady=10)


	Label(root, text='Team 2 enter your team name:').pack(side=TOP,padx=10,pady=10)

	team2Entry = Entry(root, width=10)
	team2Entry.pack(side=TOP,padx=10,pady=10)

	Label(root, text='Team 2: Player 1 enter your name:').pack(side=TOP,padx=10,pady=10)

	player1Entry2 = Entry(root, width=10)
	player1Entry2.pack(side=TOP,padx=10,pady=10)

	Label(root, text='Team 2: Player 2 enter your name:').pack(side=TOP,padx=10,pady=10)

	player2Entry2 = Entry(root, width=10)
	player2Entry2.pack(side=TOP,padx=10,pady=10)


	Button(root, text='READY TO PLAY').pack()

	root.mainloop()
if __name__ == "__main__":
	main()

