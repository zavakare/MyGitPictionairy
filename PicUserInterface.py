#!/usr/bin/python

#pictionAIRy UI
#Alex Elizalde/ Theodora Ronstadt/ Samantha Traczyk/ Mary Lee/ Karen Zavala
#2/12/16
#CPSC 434
#The purpose of this file is to set up the basic UI for the PictionAIRy Project

import random

words=[]
print "Welcome to pictionAIRy"
print "Are you ready to play?"
print "Press N for a new game."
print "Press R for rules."
print "Press E to exit."

playing = True
while True:
        choice.lower() = raw_input("Enter your choice: ")

        if choice == 'n':
                print "New Game Started"
		print "Choose a category"
		print "Animals"
		print "Sports"
		print "Food"
		print "Objects"
        	while playing:
			category_choice.lower() = raw_input("Enter a category : ")
			
			if category_choice == 'animals':
				with open("category1.txt") as rnd:
					for line in rnd:
						line=line.strip()
						words.append(line)
				print "Word to draw: ", words[random.randint(0,len(words)-1)]		

			elif category_choice == 'sports':
				with open("category2.txt") as rnd:
					for line in rnd:
						line=line.strip()
						words.append(line)
				print "Word to draw: ", words[random.randint(0,len(words)-1)]
			
			elif category_choice == 'food':
                        	with open("category3.txt") as rnd:
                                	for line in rnd:
                                        	line=line.strip()
                                                words.append(line)
                                print "Random word draw: ", words[random.randint(0,len(words)-1)]
			
			elif category_choice == 'objects':
                                with open("category4.txt") as rnd:
                                	for line in rnd:
                                        	line=line.strip()
                                                words.append(line)
                                print "Random word draw: ", words[random.randint(0,len(words)-1)]
			else:
				print "Not a valid category"
	elif choice == 'r':
                print "These are the Rules"
        elif choice == 'e':
                print "Exit"
        else:
                print "Not a valid choice"

else:
        print " YOU ARE SO WRONG RIGHT NOW!"
