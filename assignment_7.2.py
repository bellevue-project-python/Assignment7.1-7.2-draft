# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <Gabriel J Purvis>
# Creation Date: <09/21/2020>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	#print() # redundant print() has been removed "6"

def chooseCave():
	cave = '' # there was an improper indentation using spaces rather than tab '1'
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()
	return cave #return caves #cave was plural but cave (singular) was the assigned variable '5'

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(2)	#time.sleep(3) #comment above implies intention is for a 2 second wait, corrected '3' to '2' "8"
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	#print() # redundant print() removed '9'
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print('Gobbles you down in one bite!') #print 'Gobbles you down in one bite!' #missing a () for the string '2'

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y': #while playAgain = 'yes' or playAgain = 'y': #needed to be changed to == to be in line with proper formating '3'
	displayIntro()
	caveNumber = chooseCave() #caveNumber = choosecave() #capitilazation error on choosecave() corrected to chooseCave, refer to line 18 '4'
	checkCave(caveNumber)
    
																 #print('Do you want to play again? (yes or no)')/ this line can be removed when added to the input question below
	playAgain = input('Do you want to play again? (yes or no)')	#playAgain = input()/ added previous lines print into the input question "10"
	if playAgain == "no" or playAgain !='no': #if playAgain == "no": #corrected an inconsistency when running the program, if user entered in 'n' or another varient other than 'no', print() line below did not function. #added or playAgain !='no' to allow for variant answers that result in the following print() "11"
		print("Thanks for playing") #print("Thanks for planing") #spelling error 'planing' corrected to 'playing' "7"

