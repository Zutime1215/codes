import random

x = random.randint(1, 10)
count = 0
while count < 3: 
    count += 1
    chanceLeft = 3 - count
    userInput = int(input("Input your Guess between 1 and 10: "))
    if userInput != x:
        if chanceLeft == 0:
            print("You have no chance left :( ")
            # print("The number was",x)
            print("Better luck next time")
        else:
            print("Wrong guess")
            # print("The number was",x)
            print(f"You have {chanceLeft} chance left")
    else :
        print("Congratulations! You guessed it correct")
        break
