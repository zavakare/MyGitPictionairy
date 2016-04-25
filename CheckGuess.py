#!/usr/bin/env python

#determines whether answer matches chosenWord and saves round info

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

# opens files to determine current round, score, and who's turn it is
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
            roundNumber = int(words[0])
            team1Drawing = int(words[1])
            team2Drawing = int(words[2])
            team1Score = int(words[3])
            team2Score = int(words[4])

    #determines chosen word
    with open("drawThis.txt","r") as ins:
        lines = ins.readlines()
        for line in lines:
            words = line.split()
            ChosenWord = words[0]
                        
# save info pertaining to playing round
def saveRoundInfo():
    print "Saving into file:" + str(roundNumber+1)+','+str(team1Drawing)+','+str(team2Drawing)+','+str(team1Score) +','+str(team2Score)
    outf = open('roundInfo.txt', 'w')
    outstr = str(roundNumber+1)+','+str(team1Drawing)+','+str(team2Drawing)+','+str(team1Score) +','+str(team2Score)
    outf.write(outstr)
    outf.close()

    # when 4 rounds is over : display
    if (roundNumber+1 > 4):
        print "END OF GAME"
        WinnerLoser.main()
    # or restart round
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
	
    # if team guesses word correctly : 
    if(result== ChosenWord):
        # message box is displayed
        tkMessageBox.showinfo("You got it dude!","Your guess is correct. Your team recieves one point")
		
        # changes score
	if (roundNumber % 2 == 0):
            team2Score = int(team2Score) + 1
        else:
            team1Score = int(team1Score) + 1
                
	#saves all information in round
        saveRoundInfo()
                
    # if team guesses word incorrectly
    else:
        # message box is displayed
        tkMessageBox.showinfo("You didn't get it dude","Your guess is not correct. You recieve nothing :(")
	saveRoundInfo()
	
    root.mainloop()

if __name__ == "__main__":
    main()
