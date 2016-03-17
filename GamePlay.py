#!/usr/bin/env python 
 
#creates Timer, calls motion, and checks chosen word with guess

from Tkinter import *
import threading
import ChooseCat
import NewMotion
import tkSimpleDialog
import startGame

# calls motion function
def openDrawing():
	NewMotion.drawFunction()

#sets clock to 45 seconds
sec = 45

#creates timer and creates dialog that checks guess word with chosen word
def tick():
	global sec 
	if (sec <=  0):
		time['text']='stop'
		global result
		result = tkSimpleDialog.askstring("Ask Audience", "What is your guess?")
		if(result == ChooseCat.ChosenWord):
			print("Winner")
			print(ChooseCat.ChosenWord)
		else:
			print("Nope")
			print(result)
			print(ChooseCat.ChosenWord)
		
	else:
		sec = sec - 1
		time['text'] = sec
		# Take advantage of the after method of the Label
		time.after(1000, tick)

#combines timer and openDrawing call
def combo():
	t=threading.Thread(target=openDrawing)
	t.start()
	tick()

#calls timer and creates window
def main():
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
	team1Score = Label(root, text=nameArray[0] + ': ' + `startGame.team1Score`, font=("Helvetica", 56))
	team2Score = Label(root, text=nameArray[3] + ': ' + `startGame.team2Score`, font=("Helvetica", 56))
	team1Score.place(x=550,y=750)
	team2Score.place(x=950,y=750)
	root.mainloop()

if __name__ == "__main__":
	main()
