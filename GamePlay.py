#!/usr/bin/env python 
 
#creates Timer, calls motion, and checks chosen word with guess

from Tkinter import *
import threading
import ChooseCat
import NewMotion
import tkSimpleDialog
import startGame
import subprocess
import whatever
import RPi.GPIO as GPIO
import time


#global presto
presto=1 

# calls motion function
def openDrawing():
#	NewMotion.drawFunction()
	print "Hello"	
#sets clock to 45 seconds
sec = 15

#creates timer and creates dialog that checks guess word with chosen word
def tick():
	global sec 
#	if (pressed % 2 == 0):
#		print "yupp"
#	else:
#		print "In gameplay the value is: " + str(whatever.pressed) 
#		print "taco"

	if (sec <=  0):
		time['text']='stop'
		global result
		result = tkSimpleDialog.askstring("Ask Audience", "What is your guess?")
		if(result == ChooseCat.ChosenWord):
			print("Winner")
			if (startGame.roundNumber % 2 == 0):
				startGame.team1Score += 1
#				subprocess.call(['/home/pi/PiProject/Team2/killIt.sh'])
#				subprocess.call(['./switch.py'])

				
			else:
				startGame.team2Score += 1
		else:
			print("Nope")
			print(result)
			print(ChooseCat.ChosenWord)
		
	else:
	        if (presto % 2 == 0):
	                print "yupp"
        	else:
                	print "taco"

		sec = sec - 1
		time['text'] = sec
		# Take advantage of the after method of the Label
		time.after(1000, tick)

def startButton():
	global presto
#	subprocess.call(['./switchIt.py'])
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	while True:
	       	input_state = GPIO.input(18)
		if input_state == False:
       		        print('Button Pressed')
			presto+=1
	               	time.sleep(0.2)


#combines timer and openDrawing call
def combo():
	t=threading.Thread(target=openDrawing)
	t.start()
	tick()
	f=threading.Thread(target=startButton)
	f.start()

#calls timer and creates window
def main():
#	subprocess.call(['/home/PiProject/Team2/buttons/switch.py'])
	#create blank window and set minimum size
	root = Tk()
	root.minsize(1780, 1080)
	root.title('Timer')
	
        #creates label for displaying round information
        round = Label(root, text="Round #" + `startGame.roundNumber`, font=("Helvetica", 46))
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
	if (startGame.roundNumber % 2 == 0): #even
		teamDrawing = Label(root, text='Hey Team ' + nameArray[3] + ', your turn to draw.', font=("Helvetica", 26))
		teamDrawing.pack()
		# determines which team member is drawing this round
		if (startGame.team2Drawing  % 2 == 0): #even
			teamMemberDrawing = Label(root, text=nameArray[5] + ' you''re up!', font=("Helvetica", 26))
			teamMemberDrawing.pack()
		else:
			teamMemberDrawing = Label(root, text=nameArray[4] + ' you''re up!', font=("Helvetica", 26))
                        teamMemberDrawing.pack()
		# change next drawing member for team
		startGame.team2Drawing=startGame.team2Drawing + 1


	else: #odd	
		teamDrawing = Label(root, text='Hey Team ' + nameArray[0] + ', your turn to draw.', font=("Helvetica", 26))
		teamDrawing.pack()
		# determines which team member is drawing this round
                if (startGame.team1Drawing  % 2 == 0): #even
                        teamMemberDrawing = Label(root, text=nameArray[2] + ' you''re up!', font=("Helvetica", 26))
                        teamMemberDrawing.pack()
                else:
                        teamMemberDrawing = Label(root, text=nameArray[1] + ' you''re up!', font=("Helvetica", 26))
                        teamMemberDrawing.pack()
		# change next drawing member for team
		startGame.team2Drawing=startGame.team2Drawing + 1

	# change round number
        startGame.roundNumber=startGame.roundNumber + 1

	global time
	time = Label(root, fg='green', font=("Helvetica", 76))
	time.pack()
	Button(root, fg='blue', text='Start', command=combo).pack()
	
	# create score labels
	team1Score = Label(root, text=nameArray[0] + ' : ' + `startGame.team1Score`, font=("Helvetica", 56))
	team2Score = Label(root, text=nameArray[3] + ' : ' + `startGame.team2Score`, font=("Helvetica", 56))
	team1Score.place(x=550,y=750)
	team2Score.place(x=950,y=750)
	root.mainloop()
	subprocess.call(['./switch.py'])
#	startButton()

if __name__ == "__main__":
	main()
	#GPIO.setmode(GPIO.BCM)
	#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
