import random
answer = random.randint(1, 100)
compguess = random.randint(1,100)
userguess = None

def userMiniGameGuess():
    global userguess
    try:
        userguess = int(input("Please input a number between one and one hundred: "))
        if not((userguess <= 100) and (userguess >= 0)):
            print("Invalid selection. Number must be between 0-100")
            userMiniGameGuess()
    except:
        print("Contents cannot contain any non numeric values. Please try again. E.g. 27")
        userMiniGameGuess()

userMiniGameGuess()
compdiff = abs(answer - compguess)
userdiff = abs(answer - userguess)
if compdiff > userdiff:
    print("you win! you'll go first")
elif userdiff > compdiff:
    print("you lose! the computer will go first")
else:
    print("it was a tie! you'll go first")


