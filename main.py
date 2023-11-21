from random import randint
from colorama import Fore

# VARIABLES
turn = 0
lives = 3
maxlives = 3
dead = False
guardianhealth = 3
gameStarted = 0

def coinflip():
    side = randint(0,1)

    if side == 0:
        return "Heads"
    else:
        return "Tails"
    
# GAME
while True:
    turn += 1

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
            if ans.upper() == "N": #COMPLETE, FLOOR 2, 50/50 +2 LIFE
                nans = input("You walk into a room with a chest. Do you open it? (Y)es, (N)o: ")

                if nans.upper() == "Y":
                    lives += 2
                    maxlives = 5
                    print("You open the chest and recieve +2 life, you also proceed to the next floor.")
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
                    continue

            if ans.upper() == "W": #COMPLETE, FLOOR 3 OR BACK
                wans = input("You find a mysterious tunnel. Do you enter it? (Y)es, (N)o: ")

                if wans.upper() == "Y":
                    print("You enter the tunnel and skipped a floor of the temple.")
                    area = 3
                
                if wans.upper() == "N":
                    print("You go back to the other room")
                    continue

        # AREA 2
        if gameStarted == 1 and area == 2:
            ans = input("You find yourself in a dark room with two doors.\n(N)orth or (S)outh: ")

            if ans.upper() == "N":  # 
                tans = input("You enter a room with a talking statue.\nDo you (L)isten or (I)gnore? ")

                if tans.upper() == "L":
                    print("The statue tells you a riddle and grants you access to the next floor.")
                    area = 3
                elif tans.upper() == "I":
                    print("The statue doesnt take that kindly and smashes you to pieces.")
                    lives -= 1
                    if lives == 0:
                        gameStarted = 0
                    else: 
                        print(f"You still have {lives} lives")
                        continue

            if ans.upper() == "S":  # 
                dans = input("You encounter a deep pit. Do you (J)ump in or (G)o around? ")

                if dans.upper() == "J":
                    print("You jump into the pit and die.")
                    lives -= 1
                    if lives == 0:
                        gameStarted = 0
                    else: 
                        print(f"You still have {lives} lives")
                elif dans.upper() == "G":
                    print("You choose to go around the pit and proceed to the next area.")
                    area = 3

        # AREA 3 - BOSS FIGHT
        if gameStarted == 1 and area == 3:
            print("You enter the final floor to find the Guardian of the Temple!")
        
            choice = input("The Guardian is about to attack! Do you (A)ttack, (D)efend, or (R)un? ")

            if choice.upper() == "A":
                print("You attack the guardian!")
                attack = randint(0, 1)
                if attack == 0:
                    guardianhealth -= 1
                    print(f"You hit the Guardian! {guardianhealth}/3")
                    
                else:
                    lives -= 1
                    print(f"Your attack misses, and the Guardian counterattacks! {lives}/{maxlives}")
                    if lives == 0:
                        dead = True
                    else:
                        print(f"You still have {lives} lives")

            elif choice.upper() == "D":
                print("You defend against the Guardian's attack.")
                defense = randint(0, 1)
                if defense == 0:
                    guardianhealth -= 1
                    print(f"Your defense holds, and you counterattack! {guardianhealth}/3")
                else:
                    lives -= 1
                    print(f"Your defense fails, and the guardian hits you! {lives}/3")
                    if lives == 0:
                        dead = True
                    else:
                        print(f"You still have {lives} lives")

            elif choice.upper() == "R":
                print("You try to run, but the Guardian catches you!")
                lives -= 1
                if lives == 0:
                    dead = True
                else:
                    print(f"You still have {lives} lives")

            else:
                print("Invalid choice. Try again.")
                continue

            # Defeated the guardian
            if guardianhealth == 0:
                print(f"{Fore.GREEN}Congratulations! You defeated the Guardian and completed the game!{Fore.WHITE}")
                print(f"You completed the game in {turn} turns")
                gameStarted = 0
                break
            elif dead == True:
                print("You were defeated by the Guardian. Game over.")
                gameStarted = 0
                break

    # ERROR HANDLING
    except ValueError:
        print("Invalid Entry")
