from random import randint
from colorama import Fore

# VARIABLES
lives = 2
gameStarted = 0

def coinflip():
    side = randint(0,1)

    if side == 0:
        return "Heads"
    else:
        return "Tails"
    
# GAME
while True:
    turn =+ 1

    try:
        if gameStarted == 0:
            Playing = input("Welcome to The Mysterious Temple\nWould you like to play? (Y)es, (N)o: ")
            if Playing.upper() == "Y":
                gameStarted = 1
                area = 1
            if Playing.upper() == "N":
                break
            else:
                continue

        # AREA 1
        if gameStarted == 1 and area == 1:
            ans = input("You have walked into a temple and are greeted with 3 doors\n(N)orth, (E)ast, (S)outh, (W)est: ")
            if ans.upper() == "N": #COMPLETE, FLOOR 2, 50/50 +1 LIFE
                nans = input("You walk into a room with a chest. Do you open it? (Y)es, (N)o: ")

                if nans.upper() == "Y":
                    lives += 1
                    print("You open the chest and recieve another life, you also proceed to the next floor.")
                    area = 2
                if nans.upper() == "N":
                    print("You ignore the chest and proceed to the next floor.")
                    area = 2

            if ans.upper() == "E": #COMPLETE, 50/50 YOU DIE OR LIVE
                ans = input("You walk into a new room and are greeted with a coinflip, (H)eads or (T)ails? ")
                flip = coinflip()

                if ans.upper() == "H" and flip == "Heads" or ans.upper() == "T" and flip == "Tails":
                    print("You win and proceed to the next area")
                    area = 2
                else: 
                    print("You were killed by the coin")
                    lives -= 1
                    if lives == 0:
                        gameStarted = 0
                    else: 
                        print(f"You still have {lives} lives")
                        continue
                
            if ans.upper() == "S": #COMPLETE, YOU DIE
                print(f"{Fore.RED}You walk back outside the temple and are killed by a guard{Fore.WHITE}")
                lives -= 1
                if lives == 0:
                    gameStarted = 0
                else: 
                    print(f"You still have {lives} lives")

            if ans.upper() == "W": #COMPLETE, FLOOR 3 OR BACK
                wans = input("You find a mysterious tunnel. Do you enter it? (Y)es, (N)o: ")

                if wans.upper() == "Y":
                    print("You enter the tunnel and skipped a floor of the temple.")
                    area = 3
                
                if wans.upper() == "N":
                    print("You go back to the other room")
                    continue

        if gameStarted == 1 and area == 2:
            ans = input("You find yourself in a dark room with two doors.\n(N)orth or (S)outh: ")

            if ans.upper() == "N":  # Northern path
                tans = input("You enter a room with a talking statue.\nDo you (L)isten or (I)gnore? ")

                if tans.upper() == "L":
                    print("The statue tells you a riddle and grants you access to the next floor.")
                    area = 3
                elif tans.upper() == "I":
                    print("You choose to ignore the statue and proceed.")
                    area = 3

            elif ans.upper() == "S":  # Southern path
                dans = input("You encounter a deep pit. Do you (J)ump over or (G)o around? ")

                if dans.upper() == "J":
                    print("You successfully jump over the pit and proceed to the next area.")
                    area = 3
                elif dans.upper() == "G":
                    print("You choose to go around the pit and proceed to the next area.")
                    area = 3

    # ERROR HANDLING
    except ValueError:
        print("Invalid Entry")
