#MANIFEST

# master branch
* .gitignore : extensions of files to not be added/committed

* CheckGuess.py : after the user makes a guess, their answer is checked against the correct answer

* ChooseCat.py : players are able to choose which category they would like to draw from

* GUI.py : main menu of game; contains: Start, About Us, Rules, & Exit buttons

* GamePlay.py : actual game portion; contains: timer, recognition of when button is pressed, call to SimpleCV & motion tracking, team scores

* NewMotion.py : tracking of orange circle using SimpleCV

* SendMessage.py : main Pi sends the word which must be drawn to the secondary Pi via sockets

* WinnerLoser.py : determines which team (if any) has won

* killAllPython.sh, killIt.sh, killItAgain.sh : scripts which kill appropriate windows depending on certain scenarios

* loadArray.py : loads category files into game

* receiveIt.py : displays received word on secondary Pi display

* reciever.py : receives the word which will be drawn from main Pi via sockets

* roundInfo.txt : keeps track of round #, which team 1 member is drawing, which team 2 member is drawing, team 1's score, team 2's score

* savedNames.txt : keeps track of team and individual names

* startGame.py : players enter team and individual name information
