import random

enemyShipsCoordinates = [(1,1), (2,1), (3,1), (4,1), (5,1), (4, 4), (4, 5), (4, 6)]


#creates coordinates system and stores it in enemyBattlefield variable
keys = range(1,11)
values = range(1,11)
coordinates = []
for y in values:    #for 1-10
    for x in keys:  #and 1-10
        coordinates.append((x, y))
enemyBattlefield = sorted(list(set(coordinates)))

#Keeps up with already guess locations so AI cant shoot the same
#place twice and where has yet to be shot
alreadyGuessed = []
availableGuesses = enemyBattlefield
flagHit = 0
flagSunk = 0

#for use with afterHitGuess() to make more intelligent decisions
hitCoordinates = []
smartToGuess = []
smartGuessed = []
orientation = ""
flagSunk = 0

#Guesses randomly a location on the board that has not been chosen yet.
#then shortens the list of remaining available guesses and
#appends the list of already guessed guesses
#guess is the current guess, returned after verifying the guess is valid.
def helper_randomGuess():
    if (len(availableGuesses) == 0):
        return "No more guesses left"
    guess = random.choice(availableGuesses)
    availableGuesses.remove(guess)
    alreadyGuessed.append(guess)
    helper_didhit(guess)
    return guess

def helper_afterhitGuess():
    guess = random.choice(smartToGuess)
    print("testing... guess is" + str(guess))
    smartToGuess.remove(guess)
    smartGuessed.append(guess)
    availableGuesses.remove(guess)
    alreadyGuessed.append(guess)
    helper_didhit(guess)
    return guess

#interprets hitCoordinates to find orientation and sets the orientation
def findOrientation(guess):
    if guess[0] == hitCoordinates[0][0]:
        orientation = "VERTICAL" #not saving orientation to global variable
        print("I made it here " + orientation)
    elif guess[1] == hitCoordinates[0][1]:
        orientation = "HORIZONTAL"
        print("I made it here " + orientation)

#returns if the guess accurately guessed a ships location
def helper_didhit(guess):
    if (guess in enemyShipsCoordinates and len(hitCoordinates) == 1):
        findOrientation(guess)
        print("Orientation is " + orientation)
    if guess in enemyShipsCoordinates:
        if (len(hitCoordinates) == 0):
            smartToGuess.append((guess[0] - 1, guess[1])) #adds cooridinate to left of initial hit to list
            smartToGuess.append((guess[0] + 1, guess[1])) #adds cooridinate to right of initial hit to list
            smartToGuess.append((guess[0], guess[1] - 1)) #adds cooridinate up of initial hit to list
            smartToGuess.append((guess[0], guess[1] + 1)) #adds cooridinate down of initial hit to list
            for x in smartToGuess:
                if x not in availableGuesses:
                    smartToGuess.remove(x)
        hitCoordinates.append(guess)
        print("Hit!")
        #return True
    else:
        print("Miss")
        #return False

#Logic controller function. Will decide what kind of guess to perform
def helper_attack():
    if not(len(hitCoordinates) == 0):
        return helper_afterhitGuess()
    else:
        return helper_randomGuess()
    

print('my guess is ' + str(helper_attack()))