#!/usr/bin/env python 
import startGame 
from Tkinter import *
from PIL import Image, ImageTk


#creates GUI interface, begins game

#create blank window and set minimum size
root = Tk()
frame = Frame(root)
frame.pack()

root.minsize(1780, 1080)


#Opening the images
imgTitle = Image.open("allImages/pictionary.gif")
render = ImageTk.PhotoImage(imgTitle)
imgStartB = Image.open("allImages/StartButton.gif")
renderStart = ImageTk.PhotoImage(imgStartB)
imgRulesB = Image.open("allImages/RulesButton.gif")
renderRules = ImageTk.PhotoImage(imgRulesB)
imgAboutB = Image.open("allImages/AboutUsButton.gif")
renderAbout = ImageTk.PhotoImage(imgAboutB)
imgExitB = Image.open("allImages/ExitButton2.gif")
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
    rulesWin = Toplevel()
    rulesWin.minsize(1400,800)
    rulesWin.configure(bg =  "Purple" )
	
    rulesImg = Image.open("allImages/RulesListed.gif")
    renderRules = ImageTk.PhotoImage(rulesImg)

    imgRulesListed = Label(rulesWin, image=renderRules,bg =  "Purple" )
    imgRulesListed.image = renderRules
    imgRulesListed.place(x=80,y=20)
	

def aboutus():
    AboutWin = Toplevel()
    AboutWin.minsize(1200,800)
    AboutWin.configure(bg =  "Purple" )

    imgTitleAbout = Image.open("allImages/AboutUsPgTitle.gif")
    renderTitleAbout = ImageTk.PhotoImage(imgTitleAbout)

    imgAboutTitle = Label(AboutWin, image=renderTitleAbout,bg =  "Purple" )
    imgAboutTitle.image = renderTitleAbout
    imgAboutTitle.pack()

    imgTitleTeam = Image.open("allImages/groupImageInfo.gif")
    renderImageTeam = ImageTk.PhotoImage(imgTitleTeam)

    imgTeam = Label(AboutWin, image=renderImageTeam,bg =  "Purple" )
    imgTeam.image = renderImageTeam
    imgTeam.place(x=100,y=130)


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
