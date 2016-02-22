#pictionAIRy UI
#Alex Elizalde/ Theodora Ronstadt/ Samantha Traczyk/ Mary Lee/ Karen Zavala
#2/12/16
#CPSC 434
#The purpose of this file is to set up the basic UI for the PictionAIRy Project


print "Welcome to pictionAIRy"
print "Are you ready to play?"
print "Press N for a new game."
print "Press R for rules."
print "Press E to exit."

while True:
        choice = raw_input("Enter your choice: ")

        if choice == 'N':
                print "New Game Started"
        elif choice == 'R':
                print "These are the Rules"
        elif choice == 'E':
                print "Exit"
        else:
                print "Not a valid choice"

else:
        print " YOU ARE SO WRONG RIGHT NOW!"
