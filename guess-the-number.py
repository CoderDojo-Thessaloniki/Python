import random

secretNumber =  random.randrange(10)

remainingTries = 8

while remainingTries > 0:
    print("You have " + str(remainingTries) + " remaining tries\n\n")
    userGuessed = int(input("gimme your numba:"))
    
    print("Your number is:")
    
    if userGuessed == secretNumber:
        print("Correct!\n")
        break
    elif userGuessed > secretNumber:
        print("Bigger...\n")
    else:
        print("Smaller\n")

    
    remainingTries -= 1