import time
import random
rollone = 0
rolltwo = 0
rollthree = 0

def TwoPlayerQuit():
    Exit = input("would you like to exit now? Y/N \n")
    Exit = Exit.upper()
    if Exit == "Y":
        exit()
    elif Exit =="N":
        TwoPlayerGame()

def TwoPlayerGame():
        playerOneSpace = 0
        playerTwoSpace = 0
        move = 0
        
        print("You have to get from 30 to 0 before your opponent does!\n") 
        time.sleep(1)


        while playerOneSpace < 30 and playerTwoSpace < 30: #Loops the roll mechanic when 30 hasn't been hit yet 
            move = random.randint(1,6) #Roll mechanic
            print(winner,"rolled a",move)
            if move == 6:
                print("You got a 6! Roll again!") #If they get a 6 they roll again
                extraMove = random.randint(1,6)
                totalMove = extraMove + move #Calculates the double move
                print(totalMove,"in total!")
                move = totalMove
            playerOneSpace = playerOneSpace + move
            if playerOneSpace == 1: #If they roll a 1 on their first go they go forward an additional 5 spaces
                print("Tough start? Go forward 5!")
                playerOneSpace = playerOneSpace + 5
            elif playerOneSpace == 13: #If they get 13 places from the end they go back 5
                print("Oh no unlucky 13! Go back 5")
                playerOneSpace = playerOneSpace - 5
            if playerOneSpace > 29: #When player 1 gets 30+ they win
                print(winner,"wins!")
                TwoPlayerQuit()
            elif playerOneSpace < 31: #When they haven't hit 30 it says how many spaces they have gone out of 30
                print(winner,"has gone",playerOneSpace," out of 30 spaces!")
            input()
            
            move2 = random.randint(1,6)
            print(loser,"rolled a",move2)
            if move2 == 6:
                print("You got a 6! Roll again")
                extraMove2 = random.randint(1,6)
                totalMove2 = extraMove2 + move2
                print(totalMove2,"in total!")
                move2 = totalMove2
            playerTwoSpace = playerTwoSpace + move2        
            if playerTwoSpace == 1:
                print("Tough start? go forward 5!")
                playerTwoSpace = playerTwoSpace + 5
            elif playerTwoSpace == 13:
                print("Oh no unlucky 13! Go back 5")
                playerTwoSpace = playerTwoSpace - 5
            if playerTwoSpace > 29:
                print(loser,"wins!")
                TwoPlayerQuit()
            elif playerTwoSpace < 31:
                print(loser,"has gone",playerTwoSpace,"out of 30 spaces!")
            input()

def ThreePlayerQuit():
    Exit = input("would you like to exit now? Y/N \n")
    Exit = Exit.upper()
    if Exit == "Y":
        exit()
    elif Exit =="N":
        ThreePlayerGame()

def ThreePlayerGame():
        playerOneSpace = 0
        playerTwoSpace = 0
        playerThreeSpace = 0
        move = 0
        
        print("You have to get from 30 to 0 before your opponent does!\n") 
        time.sleep(1)


        while playerOneSpace < 30 and playerTwoSpace < 30 and playerThreeSpace < 30: #Loops the roll mechanic when 30 hasn't been hit yet 
            move = random.randint(1,6) #Roll mechanic
            print(winner,"rolled a",move)
            if move == 6:
                print("You got a 6! Roll again!") #If they get a 6 they roll again
                extraMove = random.randint(1,6)
                totalMove = extraMove + move #Calculates the double move
                print(totalMove,"in total!")
                move = totalMove
            playerOneSpace = playerOneSpace + move
            if playerOneSpace == 1: #If they roll a 1 on their first go they go forward an additional 5 spaces
                print("Tough start? Go forward 5!")
                playerOneSpace = playerOneSpace + 5
            elif playerOneSpace == 13: #If they get 13 places from the end they go back 5
                print("Oh no unlucky 13! Go back 5")
                playerOneSpace = playerOneSpace - 5
            if playerOneSpace > 29: #When player 1 gets 30+ they win
                print(winner,"wins!")
                ThreePlayerQuit()
            elif playerOneSpace < 31: #When they haven't hit 30 it says how many spaces they have gone out of 30
                print(winner,"has gone",playerOneSpace," out of 30 spaces!")
            input()
            
            move2 = random.randint(1,6)
            print(middle,"rolled a",move2)
            if move2 == 6:
                print("You got a 6! Roll again")
                extraMove2 = random.randint(1,6)
                totalMove2 = extraMove2 + move2
                print(totalMove2,"in total!")
                move2 = totalMove2
            playerTwoSpace = playerTwoSpace + move2        
            if playerTwoSpace == 1:
                print("Tough start? go forward 5!")
                playerTwoSpace = playerTwoSpace + 5
            elif playerTwoSpace == 13:
                print("Oh no unlucky 13! Go back 5")
                playerTwoSpace = playerTwoSpace - 5
            if playerTwoSpace > 29:
                print(middle,"wins!")
                ThreePlayerQuit()
            elif playerTwoSpace < 31:
                print(middle,"has gone",playerTwoSpace,"out of 30 spaces!")
            input()

            move3 = random.randint(1,6)
            print(loser,"rolled a",move3)
            if move3 == 6:
                print("You got a 6! Roll again")
                extraMove3 = random.randint(1,6)
                totalMove3 = extraMove3 + move3
                print(totalMove3,"in total!")
                move3 = totalMove3
            playerThreeSpace = playerThreeSpace + move3        
            if playerThreeSpace == 1:
                print("Tough start? go forward 5!")
                playerThreeSpace = playerThreeSpace + 5
            elif playerThreeSpace == 13:
                print("Oh no unlucky 13! Go back 5")
                playerThreeSpace = playerThreeSpace - 5
            if playerThreeSpace > 29:
                print(loser,"wins!")
                ThreePlayerQuit()
            elif playerTwoSpace < 31:
                print(loser,"has gone",playerThreeSpace,"out of 30 spaces!")
            input()

Number = "0"
while Number != "2" and Number != "3":
    print("Please input a working value.\n")
    Number = input("Are 2 or 3 people playing?\n")
if Number == "2" or Number == "3":
    print(Number,"people are playing!\n")
else:
    Number = "0"

if Number == "2":
    playerone = input("What is the name of Player 1?\n")
    playerone = playerone.capitalize()
    print("Okay! Player 1 is",playerone+"!")

    playertwo = input("What is the name of Player 2?\n")
    playertwo = playertwo.capitalize()
    print("Okay! Player 2 is",playertwo+"!")

    while playerone == playertwo: #If they are the same name player two has to redo their name
        print("That is the same name! Give another name.") 
        playertwo = input()
        playertwo = playertwo.capitalize()
    print("Player 2 is now",playertwo)
    time.sleep(1)

    while rollone == rolltwo:
        input(playerone+", hit space to continue\n")
        rollone = random.randint(1,6)
        print(playerone+" got a",str(rollone)+"!\n\n")
        rollone = int(rollone)

        input(playertwo+", hit space to continue\n")
        rolltwo = random.randint(1,6)
        print(playertwo+" got a",str(rolltwo)+"!\n\n")
        rolltwo = int(rolltwo)

        if rollone == rolltwo:
            print("You got the same! Try again\n")
        elif rollone > rolltwo:
            winner = playerone
            loser = playertwo
            print(playerone+" got a higher score;",str(rollone)+". "+playerone+" goes first!")
        elif rollone < rolltwo:
            winner = playertwo
            loser = playerone
            print(playertwo+" got a higher score;",str(rolltwo)+". "+playertwo+" goes first!")
    TwoPlayerGame()



#3 players is a lot of the same code but duped and slightly edited to work.
elif Number == "3":
    playerone = input("What is the name of Player 1?\n")
    playerone = playerone.capitalize()
    print("Okay! Player 1 is",playerone+"!")

    playertwo = input("What is the name of Player 2?\n")
    playertwo = playertwo.capitalize()
    print("Okay! Player 2 is",playertwo+"!")

    playerthree = input("What is the name of Player 3?\n")
    playerthree = playerthree.capitalize()
    print("Okay! Player 3 is",playerthree+"!")

    while playertwo == playerone: #If they are the same name player two has to redo their name
        print("That is the same name! Player 1, give another name.") 
        playerone = input()
        playerone = playerone.capitalize()
    print("Player 1 is now",playerone)
    time.sleep(1)

    while playerthree == playertwo:
        print("That is the same name! Player 2, give another name.") 
        playertwo = input()
        playertwo = playertwo.capitalize()
    print("Player 2 is now",playertwo)
    time.sleep(1)

    while playerone == playerthree:
        print("That is the same name! Player 3, give another name.") 
        playerthree = input()
        playerthree = playerthree.capitalize()
    print("Player 3 is now",playerthree)
    time.sleep(1)

    while rollone == rolltwo or rollone == rollthree or rolltwo == rollthree:
        input(playerone+", hit space to continue\n")
        rollone = random.randint(1,6)
        print(playerone+" got a",str(rollone)+"!\n\n")
        rollone = int(rollone)

        input(playertwo+", hit space to continue\n")
        rolltwo = random.randint(1,6)
        print(playertwo+" got a",str(rolltwo)+"!\n\n")
        rolltwo = int(rolltwo)

        input(playerthree+", hit space to continue\n")
        rollthree = random.randint(1,6)
        print(playerthree+" got a", str(rollthree)+"!\n\n")        

        while rollone == rolltwo:
            print("You got the same! Try again\n")
            input(playerone+", hit space to continue\n")
            rollone = random.randint(1,6)
            print(playerone+" got a",str(rollone)+"!\n\n")
            rollone = int(rollone)

            input(playertwo+", hit space to continue\n")
            rolltwo = random.randint(1,6)
            print(playertwo+" got a",str(rolltwo)+"!\n\n")
            rolltwo = int(rolltwo)
            

        while rollone == rollthree:
            print("You got the same! Try again\n")
            input(playerone+", hit space to continue\n")
            rollone = random.randint(1,6)
            print(playerone+" got a",str(rollone)+"!\n\n")
            rollone = int(rollone)

            input(playerthree+", hit space to continue\n")
            rollthree = random.randint(1,6)
            print(playerthree+" got a",str(rollthree)+"!\n\n")
            rollthree = int(rollthree)        

        while rolltwo == rollthree:
            print("You got the same! Try again\n")
            input(playertwo+", hit space to continue\n")
            rolltwo = random.randint(1,6)
            print(playertwo+" got a",str(rolltwo)+"!\n\n")
            rolltwo = int(rolltwo)

            input(playerthree+", hit space to continue\n")
            rollthree = random.randint(1,6)
            print(playerthree+" got a",str(rollthree)+"!\n\n")
            rollthree = int(rollthree)  

        if rollone > rolltwo > rollthree:
            winner = playerone
            middle = playertwo
            loser = playerthree
            print(playerone+" got the highest score;",str(rollone)+". "+playerone+" goes first!")
            print(playertwo+" was in the middle;",str(rolltwo)+". "+playertwo+" goes second!")
        elif rollone > rollthree >rolltwo:
            winner = playerone
            middle = playerthree
            loser = playertwo
            print(playerone+" got the highest score;",str(rollone)+". "+playerone+" goes first!")
            print(playerthree+" was in the middle;",str(rollthree)+". "+playerthree+" goes second!")
        elif rolltwo > rollone > rollthree:
            winner = playertwo
            middle = playerone
            loser = playerthree
            print(playertwo+" got the highest score;",str(rolltwo)+". "+playertwo+" goes first!")
            print(playerone+" was in the middle;",str(rollone)+". "+playerone+" goes second!")
        elif rolltwo > rollthree > rollone:
            winner = playertwo
            middle = playerthree
            loser = playerone
            print(playertwo+" got the highest score;",str(rolltwo)+". "+playertwo+" goes first!")
            print(playerthree+" was in the middle;",str(rollthree)+". "+playerthree+" goes second!")
        elif rollthree > rollone > rolltwo:
            winner = playerthree
            middle = playerone
            loser = playertwo
            print(playerthree+" got the highest score;",str(rollthree)+". "+playerthree+" goes first!")
            print(playerone+" was in the middle;",str(rollone)+". "+playerone+" goes second!")
        elif rollthree > rolltwo > rollone:
            winner = playerthree
            middle = playertwo
            loser = playerone
            print(playerthree+" got the highest score;",str(rollthree)+". "+playerthree+" goes first!")
            print(playertwo+" was in the middle;",str(rolltwo)+". "+playertwo+" goes second!")
    ThreePlayerGame()
            
