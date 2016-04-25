#!/usr/bin/env python

# allows users to enter team names and player names

import Tkinter
from Tkinter import *
import ChooseCat
import loadArray
from PIL import Image, ImageTk


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
	start = Toplevel()
	start.minsize(1780,1080)
	start.configure(bg =  "Purple" )

	myvar = StringVar()

	#setting window name
	start.title('It is time to make our teams!')

	#Team Title 
	imgTeamT = Image.open("allImages/TeamTitle.gif")
	renderTeamT = ImageTk.PhotoImage(imgTeamT)
	imgTitleT = Label(start, image=renderTeamT,bg =  "Purple" )
	imgTitleT.image = renderTeamT
	imgTitleT.pack()

	Team1Title = Image.open("allImages/TeamOne.gif")
        renderTeam1Title = ImageTk.PhotoImage(Team1Title)
        imgTeam1Title = Label(start, image=renderTeam1Title,bg =  "Purple" )
        imgTeam1Title.image = renderTeam1Title
        imgTeam1Title.place(x=250,y=200)

	#team 1 enters team name
	Team1 = Image.open("allImages/EnterTeamBlue.gif")
        renderTeam1 = ImageTk.PhotoImage(Team1)
        imgTeam1 = Label(start, image=renderTeam1,bg =  "Purple" )
        imgTeam1.image = renderTeam1
        imgTeam1.place(x=100,y=300)


	team1Entry = Entry(start, width=30,font=("Helvetica",30), textvariable=myvar)
	team1Entry.place(x=100,y=380)
	

	#team 1 player 1 enters own name
	Team1Player1 = Image.open("allImages/Player1Green.gif")
        renderTeam1Player1 = ImageTk.PhotoImage(Team1Player1)

        imgTeam1Player1 = Label(start, image=renderTeam1Player1,bg =  "Purple" )
        imgTeam1Player1.image = renderTeam1Player1
        imgTeam1Player1.place(x=100,y=450)

	t1player1Entry = Entry(start, width=30,font=("Helvetica",30))
	t1player1Entry.place(x=100,y=530)


	#team 1 player 2 enters own name
	Team1Player2 = Image.open("allImages/Player2Pink.gif")
        renderTeam1Player2 = ImageTk.PhotoImage(Team1Player2)

	imgTeam1Player2 = Label(start, image=renderTeam1Player2,bg =  "Purple" )
        imgTeam1Player2.image = renderTeam1Player2
        imgTeam1Player2.place(x=100,y=600)

        t1player2Entry = Entry(start, width=30,font=("Helvetica",30))
        t1player2Entry.place(x=100,y=680)


	#Team 2 Title
	Team2Title = Image.open("allImages/TeamTwo.gif")
        renderTeam2Title = ImageTk.PhotoImage(Team2Title)
        imgTeam2Title = Label(start, image=renderTeam2Title,bg =  "Purple" )
        imgTeam2Title.image = renderTeam1Title
        imgTeam2Title.place(x=1250,y=200)


	#team 2 enters name
	Team2 = Image.open("allImages/EnterTeamYellow.gif")
        renderTeam2 = ImageTk.PhotoImage(Team2)

        imgTeam2 = Label(start, image=renderTeam2,bg =  "Purple" )
        imgTeam2.image = renderTeam2
        imgTeam2.place(x=1050,y=300)

	team2Entry = Entry(start, width=30,font=("Helvetica",30))
	team2Entry.place(x=1050,y=380)


	#team 2 player 1 enters own name
	Team2Player1 = Image.open("allImages/Player1Blue.gif")
        renderTeam2Player1 = ImageTk.PhotoImage(Team2Player1)

        imgTeam2Player1 = Label(start, image=renderTeam2Player1,bg =  "Purple" )
        imgTeam2Player1.image = renderTeam2Player1
        imgTeam2Player1.place(x=1050,y=450)

	t2player1Entry = Entry(start, width=30,font=("Helvetica",30))
	t2player1Entry.place(x=1050,y=530)

	#team 2 player 2 enters own name
	Team2Player2 = Image.open("allImages/Player2Orange.gif")
        renderTeam2Player2 = ImageTk.PhotoImage(Team2Player2)

        imgTeam2Player2 = Label(start, image=renderTeam2Player2,bg =  "Purple" )
        imgTeam2Player2.image = renderTeam2Player2
        imgTeam2Player2.place(x=1050,y=600)

	t2player2Entry = Entry(start, width=30,font=("Helvetica",30))
	t2player2Entry.place(x=1050,y=680)


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
	

	imgButtonR = Image.open("allImages/readyToPlayButton.gif")
	renderReady = ImageTk.PhotoImage(imgButtonR)

	#Ready to Play button
	ReadyButton=Button(start, image=renderReady, command = SaveInfo,bg="Purple")
	ReadyButton.config(height=180, width=380)	
	ReadyButton.place(x=710, y=760)

	
	#display window on screen
	start.mainloop()


if __name__ == "__main__":
	mainStart()

