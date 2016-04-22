#!/usr/bin/env python 
import startGame 
from Tkinter import *
from PIL import Image, ImageTk


#creates GUI interface, begins game

#create blank window and set minimum size
root = Tk()
root.minsize(1780, 1080)


#Opening the images
imgTitle = Image.open("pictionary.gif")
render = ImageTk.PhotoImage(imgTitle)
imgStartB = Image.open("StartButton.gif")
renderStart = ImageTk.PhotoImage(imgStartB)
imgRulesB = Image.open("RulesButton.gif")
renderRules = ImageTk.PhotoImage(imgRulesB)
imgAboutB = Image.open("AboutUsButton.gif")
renderAbout = ImageTk.PhotoImage(imgAboutB)
imgExitB = Image.open("ExitButton.gif")
renderExit = ImageTk.PhotoImage(imgExitB)



#Using Label to display our imgTitle
img = Label(root, image=render,bg =  "Purple" )
img.image = render
img.place(x=400,y=20)


#change background color
root.configure(bg =  "Purple" )

#set window title
root.title("The Reflections + Alex presents: pictionAIRy")

#create title text and default place on screen
title = Label(root, font=("Helvetica", 76), fg="Black", bg = "Purple" )
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
	rulesWin.configure(bg =  "Purple" )
	RuleHeader = Label(rulesWin, text = 'Rules Listed', bg = "Purple", font=("Georgia", 30) )
	RuleHeader.pack()
	Rule1 = Label(rulesWin, text = '1.Separate into 2 teams, each team consisting of 2 people, and enter your team names. ', bg = "Purple", font=("Georgia", 17)  )
	Rule1.pack()
	Rule2 = Label(rulesWin, text = '2.Pick 1 player to begin and choose your drawing category. ', bg = "Purple", font=("Georgia", 17)  )
        Rule2.pack()
	Rule3 = Label(rulesWin, text = '3.Player 1 gets word to draw and gets tracking device to put on the dominate hand. ', bg = "Purple", font=("Georgia", 17))
        Rule3.pack()
	Rule4 = Label(rulesWin, text = '4.Stand in front of web cam and draw. You will have 45 seconds to draw this.  ', bg = "Purple", font=("Georgia", 17) )
        Rule4.pack()
	Rule5 = Label(rulesWin, text = '5.You will have unlimited unoffical guesses and one offical guess.  You will offically guess by hitting the buzzer and saying your answer out loud. ', bg = "Purple", font=("Georgia", 17)  )
        Rule5.pack()
	Rule6 = Label(rulesWin, text = '6.The team will get the point if the guess is correct.  The Team at the end of 3 rounds with the most points will win! ', bg = "Purple", font=("Georgia", 17)  )
        Rule6.pack()
	#rulesButton = Button(rulesWin, text="Go BaCk", command=closewindow, font=("Georgia", 40))
	#rulesButton.pack()
	rulesButton = Button(rulesWin, text = 'Quit', command=rulesWin.quit)
	rulesButton.pack()
	#self.root.mainloop()

def quit():
       rulesWin.destroy()

def aboutus():
	AboutWin = Tk()
        AboutWin.minsize(1200,800)
	AboutWin.configure(bg =  "Purple" )

        AboutHeader = Label(AboutWin, text = 'About Us', bg = "Purple", font=("Georgia", 30) )
        AboutHeader.pack()
        AboutUsText = Label(AboutWin, text = 'The game pictionAIRy was made over the course of the spring 2016 semester. Made by Alex, Mary, Theodora, Sam, and Karen.\n All of the group members are currently computer science majors, which attend Dominican University in River Forest.\n The project was for CPSC 431, Principles of Unix and Professor Bonakdarian. \n The group managed the time wisely and had a lot of fun making the project. ', bg = "Purple", font=("Georgia", 17))
        AboutUsText.pack()
	
	

#creates main menu  buttons
button = Button(root, image=renderExit, command=closewindow, bg="Purple")
button2 = Button(root, image=renderRules, command=listrules, bg="Purple")
button3 = Button(root, image=renderStart,command=openGame,bg="Purple")
button4 = Button(root, image=renderAbout, command=aboutus, bg="Purple")

#size of buttons
button.config(height=200, width=400)
button2.config(height=200, width=400)
button3.config(height=200, width=400)
button4.config(height=200, width=400)

#placing of button
button.place(x=420, y=620)
button3.place(x=420, y=320)
button2.place(x=920, y=320)
button4.place(x=920, y=620)

#display window on screen
root.mainloop()
