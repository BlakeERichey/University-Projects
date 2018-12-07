import random

playerShipsCoordinates = [('a',1), ('b',1), ('c',1), ('d',1), ('e',1), ('d', 4), ('d', 5), ('d', 6)]


#creates coordinates system and stores it in playerBattlefield variable
keys = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
values = range(1,11)
coordinates = []
for y in values:    #for a-j
    for x in keys:  #and 1-10
        coordinates.append((x, y))
playerBattlefield = sorted(list(set(coordinates)))

#Keeps up with already guess locations so AI cant shoot the same
#place twice and where has yet to be shot
alreadyGuessed = []
availableGuesses = playerBattlefield

#for use with afterHitGuess() to make more intelligent decisions
smartToGuess = []
smartGuessed = []

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
    guess = None #give guess function scope
    guess = random.choice(smartToGuess)
    print("testing... guess is" + str(guess))
    smartToGuess.remove(guess)
    smartGuessed.append(guess)
    availableGuesses.remove(guess)
    alreadyGuessed.append(guess)
    helper_didhit(guess)
    return guess


#returns if the guess accurately guessed a ships location
def helper_didhit(guess):
    if guess in playerShipsCoordinates:
        tempArray = []
        tempArray.append((chr(ord(guess[0]) - 1), guess[1])) #adds cooridinate to down of initial hit to list
        tempArray.append((chr(ord(guess[0]) + 1), guess[1])) #adds cooridinate to up of initial hit to list
        tempArray.append((guess[0], guess[1] - 1)) #adds cooridinate left of initial hit to list
        tempArray.append((guess[0], guess[1] + 1)) #adds cooridinate right of initial hit to list
        for x in tempArray:
            if x in availableGuesses:
                smartToGuess.append(x)
        hitCoordinates.append(guess)
        #print("Hit!")
        return True
    else:
        #print("Miss")
        return False

#Logic controller function. Will decide what kind of guess to perform
def ai_turn():
    if not(len(smartToGuess) == 0):
        return helper_afterhitGuess()
    else:
        return helper_randomGuess()
    

print('my guess is ' + str(ai_turn()))
