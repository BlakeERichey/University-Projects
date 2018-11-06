import random

enemyShipsCoordinates = [(1,1), (1,2), (1,3), (1,4), (1,5)]


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
    if helper_didhit(guess):
        print("Hit!")
    else:
        print("Miss")
    return guess

def helper_afterhitGuess(guess):
    pass

#returns if the guess accurately guessed a ships location
def helper_didhit(guess):
    if guess in enemyShipsCoordinates:
        flagHit = 1
        return True
    else:
        flagHit = 0
        return False

def helper_attack():
    if hitFlag = 1:
        helper_afterhitGuess()
    elif hitFlag = 0:
        helper_randomGuess()
    

print('my guess is ' + str(helper_randomGuess()) + str(flagHit))
