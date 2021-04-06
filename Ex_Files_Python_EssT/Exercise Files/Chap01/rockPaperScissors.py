""" Rock Paper Scissors
--------------------------------------------------------------
"""

import random
import os
import re
os.system('cls' if os.name=='nt' else clear)
while (1< 2):
    print ("\n")
    print ("Rock, Paper, Scissors - Shoot!")
    userChoice = raw_input("Choose your weapon [R]ock, [P]aper, or [S]cissors: ")
    if not re.match("[SsRrPp]", userChoice):
        print ("Please choose a letter: ")
        print ("[R]ock, [P]aper, or [S]cissors.")
        continue
    # Echo the user's choice
    print ("You choose: " + userChoice)
    choices = ['R', 'P', 'S']
    opponentChoice = random.choice(choices)
    print ("I choose: " + opponentChoice)
    if opponentChoice == str.upper(userChoice):
        print ("Tie!")
    elif opponentChoice == 'R' and userChoice.upper() == 'S':
        print ("Rock beats Scissors, I lose")
        continue
    elif opponentChoice == 'S' and userChoice.upper() == 'P':
        print ("Scissors beats paper, I lose")
        continue
    elif opponentChoice == 'P' and userChoice.upper() == 'R':
        print ("Paper beats rock, I lose")
        continue
    else:
        print ("I win!")