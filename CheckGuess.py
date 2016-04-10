#!/usr/bin/env python

from Tkinter import *
import tkSimpleDialog
import tkMessageBox
import os
import WinnerLoser

roundNumber=0
team1Drawing=0
team2Drawing=0
team1Score=0
team2Score=0
ChosenWord='nada'

def openFiles():
        global team1Drawing
        global team2Drawing
        global roundNumber
        global ChosenWord
        global team1Score
        global team2Score

        with open("roundInfo.txt","r") as ins:
               lines = ins.readlines()

               for line in lines:
                        words = line.split(",")
                        roundNumber = int(words[0])+1
                        team1Drawing = int(words[1])
                        team2Drawing = int(words[2])
                        team1Score = int(words[3])
                        team2Score = int(words[4])

        with open("drawThis.txt","r") as ins:
                lines = ins.readlines()
                for line in lines:
                        words = line.split()
                        ChosenWord = words[0]
def saveRoundInfo():
		print str(roundNumber)+','+str(team1Drawing)+','+str(team2Drawing)+','+str(team1Score) +','+str(team2Score)
                outf = open('roundInfo.txt', 'w')
                outstr = str(roundNumber)+','+str(team1Drawing)+','+str(team2Drawing)+','+str(team1Score) +','+str(team2Score)
                outf.write(outstr)
                outf.close()
                if (roundNumber > 4):
                        print "END OF GAME"
                        #call to winners page
                        WinnerLoser.main()
		else:
	                os.system('./killItAgain.sh')


def main():
	global team1Score
	global team2Score
	global team1Drawing
	global team2Drawing
	root = Tk()
        root.minsize(1780, 1080)
	openFiles()
	result = tkSimpleDialog.askstring("Ask Audience", "What is your guess?")

        if(result== ChosenWord):
                tkMessageBox.showinfo("You got it dude!","Your guess is correct. Your team recieves one point")

		if (roundNumber % 2 == 0):
                        team1Score = int(team1Score) + 1
			team1Drawing = team1Drawing + 1
                else:
                        team2Score = int(team2Score) + 1
			team2Drawing = team2Drawing +1
                saveRoundInfo()
        else:
                tkMessageBox.showinfo("You didn't get it dude","Your guess is not correct. You recieve nothing :(")
		saveRoundInfo()
	
	root.mainloop()

if __name__ == "__main__":
        main()

