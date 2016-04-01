#!/usr/bin/env python

from Tkinter import *

def whoWins():
        global team1Score
        global team2Score
	global team1Name
	global team2Name

        with open("roundInfo.txt","r") as ins:
                lines = ins.readlines()

                for line in lines:
                        words = line.split(",")
                        team1Score = int(words[3])
                        team2Score = int(words[4])

        with open("savedNames.txt","r") as ins:
                lines = ins.readlines()
                nameArray = []
                for line in lines:
                        words = line.split()
                        for word in words:
                                nameArray.append(word)
		team1Name=nameArray[0]
		team2Name=nameArray[3]

def main():
	#window to display end of game, winner, and loser

	#create blank window and set minimum size
	Ending = Tk()
	Ending.minsize(1780, 1080)

	#change background color
	Ending.configure(bg =  "Purple" )

	#set window title
	Ending.title("Game Over")

	#create title text and default place on screen
	title = Label(Ending, text='Game Over', font=("Helvetica", 76), fg="Black", bg = "Purple")
	title.pack()
	whoWins()
	if (team1Score > team2Score):
		team1Wins = Label(Ending, text='Team ' + `team1Name` + ' you win!', font=("Helvetica", 76), fg="Black", bg="Purple")
		team1Wins.pack()
	elif (team2Score > team1Score):
		team2Wins = Label(Ending, text='Team ' + `team2Name` + ' you win!', font=("Helvetica", 76), fg="Black", bg="Purple")
		team2Wins.pack()
	# tells who won the game and who lost, or if there was a tie
	else:
		teamsTie = Label(Ending, text='No one wins! It is a tie:/', font=("Helvetica", 76), fg="Black", bg="Purple")
                teamsTie.pack()


	Ending.mainloop()

if __name__ == "__main__":
	main()
