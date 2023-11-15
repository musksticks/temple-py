from random import randint
from colorama import Fore

# VARIABLES
gameStarted = 0 

# GAME

while True:
    turn =+ 1

    try:
        if gameStarted == 0:
            Playing = input("Welcome to The Mysterious Temple\nWould you like to play? (Y)es, (N)o: ")
            if Playing.upper() == "Y":
                gameStarted = 1
            if Playing.upper() == "N":
                break
            else:
                continue

        if gameStarted == 1:
            ans = input("You have walked into a temple and are greeted with 3 doors\n(N)orth, (E)ast, (S)outh, (W)est")
            if ans.upper() == "N":
                

    # ERROR HANDLING
    except ValueError:
        print("Invalid Entry")
