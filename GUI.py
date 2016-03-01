#!/usr/bin/env python 
import startGame 
from Tkinter import *

#create blank window and set minimum size
root = Tk()
root.minsize(1780, 1080)
#change background color
root.configure(bg =  "Purple" )
#set window title
root.title("The Reflections + Alex presents: pictionAIRy")

#create title text and default place on screen
title = Label(root, text='pictionAIRy', font=("Helvetica", 76), fg="Black", bg = "Purple" )
title.pack()

#calls method in startGame.py to start the team creation
def openGame():
	startGame.mainStart()
#closes window
def closewindow():
	exit()
def rulesExit():
	rulesWin.exit()
#Rules window
def listrules():
	rulesWin = Tk()
	rulesWin.minsize(1200,800)
	RuleHeader = Label(rulesWin, text = 'Rules Listed')
	RuleHeader.pack()
	Rule1 = Label(rulesWin, text = '1.Separate into 2 teams, each team consisting of 2 people, and enter your team names. ')
	Rule1.pack()
	Rule2 = Label(rulesWin, text = '2.Pick 1 player to begin and choose your drawing category. ')
        Rule2.pack()
	Rule3 = Label(rulesWin, text = '3.Player 1 gets word to draw and gets tracking device to put on the dominate hand. ')
        Rule3.pack()
	Rule4 = Label(rulesWin, text = '4.Stand in front of web cam and draw. You will have 45 seconds to draw this.  ')
        Rule4.pack()
	Rule5 = Label(rulesWin, text = '5.You will have unlimited unoffical guesses and one offical guess.  You will offically guess by hitting the buzzer and saying your answer out loud. ')
        Rule5.pack()
	Rule6 = Label(rulesWin, text = '6.The team will get the point if the guess is correct.  The Team at the end of 3 rounds with the most points will win! ')
        Rule6.pack()
	rulesButton = Button(rulesWin, text="Go BaCk", command=closewindow, font=("Georgia", 40))
	rulesButton.pack()

#creates main menu  buttons
button = Button(root, text="Exit", command=closewindow, font=("Georgia", 40))
button2 = Button(root, text="Rules", command=listrules, font=("Georgia", 40))
button3 = Button(root, text="Start", command=openGame, font=("Georgia", 40))
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
