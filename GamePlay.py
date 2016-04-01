#!/usr/bin/env python

#creates Timer, calls motion, and checks chosen word with guess

from Tkinter import *
import threading
import ChooseCat
import NewMotion
import tkSimpleDialog
import startGame
import subprocess
import RPi.GPIO as GPIO
import time
import ChooseCat
from multiprocessing import Process
import os

# even if the button has been pressed
# off if the button has not been pressed
button_pressed=1
roundNumber=0
team1Drawing=0
team2Drawing=0
team1Score=0
team2Score=0
ChosenWord='nada'


# calls motion function
def openDrawing(nm):
#        NewMotion.drawFunction()
	os.system('./NewMotion.py')
        print "Hello"

#sets clock to 45 seconds
sec = 5 

#creates timer and creates dialog that checks guess word with chosen word
def tick(num):
        global sec
	print ("In the tick method")
        if (sec <=  0):
                # checks to see if the button has been pressed
                # if it has been pressed, don't ask for guess
                if (button_pressed % 2 != 0):
                        time['text']='stop'
                        global result
                        result = tkSimpleDialog.askstring("Ask Audience", "What is your guess?")
                        check_guess(result)

        else:
		print ("We're in the else...")
                sec = sec - 1
                time['text'] = sec
                # Take advantage of the after method of the Label
                time.after(1000, tick)

def check_guess(guess):
	global team1Score
	global team2Score
        if(guess == ChosenWord):
                print("Winner")
                if (roundNumber % 2 == 0):
                        team1Score = int(team1Score) + 1
                else:
                        team2Score = int(team2Score) + 1
		saveRoundInfo()
        else:
                print("Nope")
                print(guess)
                print(ChosenWord)
		saveRoundInfo()
        if (roundNumber >= 4):
                print "END OF GAME"
                #call to winners page

def startButton(number):
	global button_pressed
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        while True:
                input_state = GPIO.input(18)
                if input_state == False:
                        print('Button Pressed')
                        button_pressed+=1
                        result = tkSimpleDialog.askstring("Ask Audience", "What is your guess?")
                        check_guess(result)
                        time.sleep(0.2)


#combines timer and openDrawing call
def combo():
	global buttonP
	global openSim
	global startT

	buttonP = Process(target=startButton, args=(0,))
	openSim = Process(target=openDrawing, args=(0,))
	startT = Process(target=tick, args=(0,))
#	guiLo = Process(target=main, args=(0,))
	buttonP.start()
	openSim.start()
	startT.start()
	buttonP.join()
	openSim.join()
	startT.join()
#	tick()
#	p = Process(target=openDrawing, args=())
#	q = Process(target=tick, args=())
#	q.start()
#	p.start()
#	tick()
#	q.join()
#	p.join()
#	pool = Pool(processes=3)
#        t=threading.Thread(target=openDrawing)
#        t.start()
#        q=threading.Thread(target=tick)
#        q.start()
#        tick()
#        f=threading.Thread(target=startButton)
#        f.start()
#        q=threading.Thread(target=tick)
#        q.start()
#       pool = Pool(processes=3)
#       pool.apply_async(openDrawing)
#       pool.apply_async(tick).start()
#       pool.apply_async(startButton)
#       p = multiprocessing.Process(None, openDrawing)
#       p.start()
#       q = multiprocessing.Process(None, tick)
#       q.start()
#       r = multiprocessing.Process(None, startButton)
#       r.start()
#       processes - []


def saveRoundInfo():
                outf = open('roundInfo.txt', 'w')
                outstr = str(roundNumber)+','+str(team1Drawing)+','+str(team2Drawing)+','+str(team1Score) +','+str(team2Score)
                outf.write(outstr)
                outf.close()
		os.system('./killIt.sh')

#calls timer and creates window
def main():
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

	with open("drawThis.txt","r") as ins:
                lines = ins.readlines()
                for line in lines:
			words = line.split()
                        ChosenWord = words[0]

        #create blank window and set minimum size
        root = Tk()
        root.minsize(1780, 1080)
        root.title('Timer')

        #creates label for displaying round information
        round = Label(root, text="Round #" + `roundNumber`, font=("Helvetica", 46))
        round.pack()

        #load team and individual names from array
        with open("savedNames.txt","r") as ins:
                lines = ins.readlines()
                nameArray = []
                for line in lines:
                        words = line.split()
                        for word in words:
                                nameArray.append(word)

        #if round number is even, team 2 is drawing
        #if round number is odd, team 1 is drawing
        if (roundNumber % 2 == 0): #even
                teamDrawing = Label(root, text='Hey Team ' + nameArray[3] + ', your turn to draw.', font=("Helvetica", 26))
                teamDrawing.pack()
	                # determines which team member is drawing this round
                if (team2Drawing  % 2 == 0): #even
                        teamMemberDrawing = Label(root, text=nameArray[5] + ' you''re up!', font=("Helvetica", 26))
                        teamMemberDrawing.pack()
                else:
                        teamMemberDrawing = Label(root, text=nameArray[4] + ' you''re up!', font=("Helvetica", 26))
                        teamMemberDrawing.pack()
                # change next drawing member for team
                team2Drawing=team2Drawing + 1


        else: #odd
                teamDrawing = Label(root, text='Hey Team ' + nameArray[0] + ', your turn to draw.', font=("Helvetica", 26))
                teamDrawing.pack()
                # determines which team member is drawing this round
                if (team1Drawing  % 2 == 0): #even
                        teamMemberDrawing = Label(root, text=nameArray[2] + ' you''re up!', font=("Helvetica", 26))
                        teamMemberDrawing.pack()
                else:
                        teamMemberDrawing = Label(root, text=nameArray[1] + ' you''re up!', font=("Helvetica", 26))
                        teamMemberDrawing.pack()
                # change next drawing member for team
                team1Drawing=team1Drawing + 1

        # change round number
        roundNumber=roundNumber + 1

        global time
        time = Label(root, fg='green', font=("Helvetica", 76))
        time.pack()
        Button(root, fg='blue', text='Start', command=combo).pack()

        # create score labels
        team1ScoreLbl = Label(root, text=nameArray[0] + ' : ' + `team1Score`, font=("Helvetica", 56))
        team2ScoreLbl = Label(root, text=nameArray[3] + ' : ' + `team2Score`, font=("Helvetica", 56))
        team1ScoreLbl.place(x=550,y=750)
        team2ScoreLbl.place(x=950,y=750)
        root.mainloop()

if __name__ == "__main__":
        main()

