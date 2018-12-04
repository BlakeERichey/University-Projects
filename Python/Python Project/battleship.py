# import necessary classes
import random

flagUserTurn = 0;
flagAITurn = 0;

# establish all possible points
battlefield = [('a', 1), ('a', 2), ('a', 3), ('a', 4), ('a', 5), ('a', 6), ('a', 7), ('a', 8), ('a', 9), ('a', 10), ('b', 1), ('b', 2), ('b', 3), ('b', 4), ('b', 5), ('b', 6), ('b', 7), ('b', 8), ('b', 9), ('b', 10), ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5), ('c', 6), ('c', 7), ('c', 8), ('c', 9), ('c', 10), ('d', 1), ('d', 2), ('d', 3), ('d', 4), ('d', 5), ('d', 6), ('d', 7), ('d', 8), ('d', 9), ('d', 10), ('e', 1), ('e', 2), ('e', 3), ('e', 4), ('e', 5), ('e', 6), ('e', 7), ('e', 8), ('e', 9), ('e', 10), ('f', 1), ('f', 2), ('f', 3), ('f', 4), ('f', 5), ('f', 6), ('f', 7), ('f', 8), ('f', 9), ('f', 10), ('g', 1), ('g', 2), ('g', 3), ('g', 4), ('g', 5), ('g', 6), ('g', 7), ('g', 8), ('g', 9), ('g', 10), ('h', 1), ('h', 2), ('h', 3), ('h', 4), ('h', 5), ('h', 6), ('h', 7), ('h', 8), ('h', 9), ('h', 10), ('i', 1), ('i', 2), ('i', 3), ('i', 4), ('i', 5), ('i', 6), ('i', 7), ('i', 8), ('i', 9), ('i', 10), ('j', 1), ('j', 2), ('j', 3), ('j', 4), ('j', 5), ('j', 6), ('j', 7), ('j', 8), ('j', 9), ('j', 10)]

# establishing necessary variables
ships = [('carrier', 5), ('battleship', 4), ('cruiser', 3), ('submarine', 3), ('destroyer', 2)] # standard battleship names and sizes
enemyCarrier = []
enemyBattleship = []
enemyCruiser = []
enemySubmarine = []
enemyDestroyer = []
enemyLocs = [] # to be altered later
userCarrier = []
userBattleship = []
userCruiser = []
userSubmarine = []
userDestroyer = []
userLocs = [] # to be altered later

# setting up each ship location
def setEnemyShipLocations():
    # placing the carrier within boundaries
    enemyCarrier = setShipLocations(battlefield, ships[0][1])
    # ammending the complete list of coordinates
    enemyLocs = enemyCarrier[:]
    # placing the battleship within boundaries
    enemyBattleship = setShipLocations(battlefield, ships[1][1])
    # checking that the battleship does not overlap any previous ships
    enemyBattleship = enemyChecker(enemyLocs, enemyBattleship, ships[1][1])
    # ammedning the complete list of coordinates
    enemyLocs += enemyBattleship
    # placing the cruiser within boundaries
    enemyCruiser = setShipLocations(battlefield, ships[2][1])
    # checking that the cruiser does not overlap any previous ships
    enemyCruiser = enemyChecker(enemyLocs, enemyCruiser, ships[2][1])
    # ammedning the complete list of coordinates
    enemyLocs += enemyCruiser
    # placing the submarine within boundaries
    enemySubmarine = setShipLocations(battlefield, ships[3][1])
    # checking that the submarine does not overlap any previous ships
    enemySubmarine = enemyChecker(enemyLocs, enemySubmarine, ships[3][1])
    # ammedning the complete list of coordinates
    enemyLocs += enemySubmarine
    # placing the destroyer within boundaries
    enemyDestroyer = setShipLocations(battlefield, ships[4][1])
    # checking that the destroyer does not overlap any previous ships
    enemyDestroyer = enemyChecker(enemyLocs, enemyDestroyer, ships[4][1])
    # ammedning the complete list of coordinates
    enemyLocs += enemyDestroyer
    # returning complete list and individual coordinates
    return enemyLocs, enemyCarrier, enemyBattleship, enemyCruiser, enemySubmarine, enemyDestroyer

# placing a single ship when called. takes in all possible points and how many points needed
def setShipLocations(battlefield, shipLength):
    # establishing necessary variables
    counter = 1 # how many points have been placed
    directions = ['left','up','right','down'] # directions to place points
    shipLocation = [] # ship points
    # chosing a random point from all possible points
    placement = list(random.choice(battlefield))
    # chosing a random direction to move the point
    direction = random.choice(directions)
    # adding the chosen point to the list
    shipLocation.append(tuple(placement))
    # while loop until all points have been added to list
    while counter < shipLength:
        # left placements
        if direction == 'left':
            # checking to see if point is at edge of board
            if placement[1] != 1:
                # if no, moves point one to the left and adds to list of points
                placement[1] = placement[1] - 1
                counter += 1
                shipLocation.append(tuple(placement))
            else:
                # if yes, moves point two over and changes the direction 
                placement[1] += (counter - 1)
                direction = 'right'
        # up placements
        if direction == 'up':
            # checking to see if point is at edge of board
            if placement[0] != 'a':
                # if no, moves point one up (using ascii incrementation) and adds to list of points
                x = ord(placement[0])
                x -= 1
                x = chr(x)
                placement[0] = x
                counter += 1
                shipLocation.append(tuple(placement))
            else:
                # if yes, moves point two over and changes the direction
                x = ord(placement[0])
                x += (counter - 1)
                x = chr(x)
                placement[0] = x
                direction = 'down'
        # right placements
        if direction == 'right':
            # checking to see if point is at edge of board
            if placement[1] != 10:
                placement[1] = placement[1] + 1
                counter += 1
                shipLocation.append(tuple(placement))
            else:
                # if yes, moves point two over and changes the direction
                placement[1] -= (counter - 1)
                direction = 'left'
        # down placements
        if direction == 'down':
            # checking to see if point is at edge of board
            if placement[0] != 'j':
                # if no, moves point one down (using ascii incrementation) and adds to list of points
                x = ord(placement[0])
                x += 1
                x = chr(x)
                placement[0] = x
                counter += 1
                shipLocation.append(tuple(placement))
            else:
                # if yes, moves point two over and changes the direction
                x = ord(placement[0])
                x -= (counter - 1)
                x = chr(x)
                placement[0] = x
                direction = 'up'
    return shipLocation

# ensures the coordinates of the ships do not overlap
def enemyChecker(setLocations, tester, length):
    # checks each individual point
    for i in tester:
        # against coordinates that have already been taken
        if i in setLocations:
            # if there is an overlap, the ship is set again
            tester = setShipLocations(battlefield, length)
            # and rechecked
            tester = enemyChecker(setLocations, tester, length)
    return tester

# setting up each ship location
def setUserShipLocations():
    # placing the carrier within boundaries
    userCarrier = setShipLocations(battlefield, ships[0][1])
    # ammending the complete list of coordinates
    userLocs = userCarrier[:]
    # placing the battleship within boundaries
    userBattleship = setShipLocations(battlefield, ships[1][1])
    # checking that the battleship does not overlap any previous ships
    userBattleship = userChecker(userLocs, userBattleship, ships[1][1])
    # ammedning the complete list of coordinates
    userLocs.append(userBattleship)
    # placing the cruiser within boundaries
    userCruiser = setShipLocations(battlefield, ships[2][1])
    # checking that the cruiser does not overlap any previous ships
    userCruiser = userChecker(userLocs, userCruiser, ships[2][1])
    # ammedning the complete list of coordinates
    userLocs.append(userCruiser)
    # placing the submarine within boundaries
    userSubmarine = setShipLocations(battlefield, ships[3][1])
    # checking that the submarine does not overlap any previous ships
    userSubmarine = userChecker(userLocs, userSubmarine, ships[3][1])
    # ammedning the complete list of coordinates
    userLocs.append(userSubmarine)
    # placing the destroyer within boundaries
    userDestroyer = setShipLocations(battlefield, ships[4][1])
    # checking that the destroyer does not overlap any previous ships
    userDestroyer = userChecker(userLocs, userDestroyer, ships[4][1])
    # ammedning the complete list of coordinates
    userLocs.append(userDestroyer)
    # returning complete list and individual coordinates
    return userLocs, userCarrier, userBattleship, userCruiser, userSubmarine, userDestroyer

# ensures the coordinates of the ships do not overlap
def userChecker(setLocations, tester, length):
    # checks each individual point
    for i in tester:
        # against coordinates that have already been taken
        if i in setLocations:
            # if there is an overlap, the ship is set again
            tester = setShipLocations(battlefield, length)
            # and rechecked
            tester = userChecker(setLocations, tester, length)

# this is the users turn, triggered by a flag
def userTurn(allPossiblePoints, c5Loc, b4Loc, c3Loc, s3Loc, d2Loc):
    # resets replacement variable - needed because tuples
    replacement = []
    # takes in the user's guess
    coordinate = helper_userGuess()
    print("Firing...")
    # determines if the guess is where an enemy has placed a ship
    hitOrMiss = helper_hitOrMiss(allPossibleEnemyPoints, c5Loc, b4Loc, c3Loc, s3Loc, d2Loc, coordinate)
    # if hit, returns which ship hit for feedback
    if hitOrMiss == "car":
      # removes the user's guess from the ships unhit coordinates
      for i in c5Loc:
        if i != coordinate:
          replacement.append(i)
      c5Loc = replacement
      if c5Loc != []:
        print("You hit the enemies Carrier!")
      else:
        print("You sunk the enemies Carrier!")
        c5Loc = []
      return c5Loc, b4Loc, c3Loc, s3Loc, d2Loc
    elif hitOrMiss == "bat":
      # removes the user's guess from the ships unhit coordinates
      for i in b4Loc:
        if i != coordinate:
          replacement.append(i)
      b4Loc = replacement
      if b4Loc != []:
        print("You hit the enemies Battleship!")
      else:
        print("You sunk the enemies Battleship!")
        b4Loc = []
      return c5Loc, b4Loc, c3Loc, s3Loc, d2Loc
    elif hitOrMiss == "cru":
      # removes the user's guess from the ships unhit coordinates
      for i in c3Loc:
        if i != coordinate:
          replacement.append(i)
      c3Loc = replacement
      if c3Loc != []:
        print("You hit the enemies Cruiser!")
      else:
        print("You sunk the enemies Cruiser!")
        c3Loc = []
      return c5Loc, b4Loc, c3Loc, s3Loc, d2Loc
    elif hitOrMiss == "sub":
      # removes the user's guess from the ships unhit coordinates
      for i in s3Loc:
        if i != coordinate:
          replacement.append(i)
      s3Loc = replacement
      if s3Loc != []:
        print("You hit the enemies Submarine!")
      else:
        print("You sunk the enemies Submarine!")
        s3Loc = []
      return c5Loc, b4Loc, c3Loc, s3Loc, d2Loc
    elif hitOrMiss == "des":
      # removes the user's guess from the ships unhit coordinates
      for i in d2Loc:
        if i != coordinate:
          replacement.append(i)
      d2Loc = replacement
      if d2Loc != []:
        print("You hit the enemies Destroyer!")
      else:
        print("You sunk the enemies Destroyer!")
        d2Loc = []
      return c5Loc, b4Loc, c3Loc, s3Loc, d2Loc
    else:
      # if the user misses, no changes are made
      print("Miss! Try Again")
      return c5Loc, b4Loc, c3Loc, s3Loc, d2Loc
        
# takes in the users input
def helper_userGuess():
    coordinate = input("Where would you like to aim? ")
    # checks that the imput is valid
    coordinate = helper_userGuessCheck(coordinate)
    # returns valid input as a tuple
    return tuple(coordinate)
        
# checks that user input is within boundaries
def helper_userGuessCheck(userInput):
    # turns string into list
    coordinate = list(userInput)
    # changes letter into ascii
    letter = ord(coordinate[0])
    # verifies second input is an integer
    try:
      number = int(coordinate[1])
    except:
      # if the sceond input is not valid, takes another input
      print("Invalid coordinate, please try again.")
      helper_userGuess()
    # if letter is valid, continue
    if letter > 96 and letter < 107:
        pass
    # takes valid letters and makes them lowercase
    elif letter > 64 and letter < 75:
        letter += 32
        letter = chr(letter)
    # first input was not a letter, asks for another input
    else:
        print("Invalid coordinate, please try again.")
        helper_userGuess()
    # checks for a valid number 
    if 0 <= number <= 9:
        if number == 0:
            number = 10
    #if number is not valid, then takes another input
    else:
        print("Invalid coordinate, please try again.")
        helper_userGuess()
    # ensures the second imput( the number) is an integer
    coordinate[1] = int(number)
    # returns the coordinates as a tuple
    return  coordinate

# checks if the user input hits the enemy's ships
def helper_hitOrMiss(allPossiblePoints, c5Loc, b4Loc, c3Loc, s3Loc, d2Loc, coord):
    # user hits a ship
    if coord in allPossiblePoints:
        # user hits the carrier
        if coord in c5Loc:
          return "car"
        # user hits the carrier
        elif coord in b4Loc:
            return "bat"
        # user hits the carrier
        elif coord in c3Loc:
            return "cru"
        # user hits the carrier
        elif coord in s3Loc:
            return "sub"
        # user hits the carrier
        elif coord in d2Loc:
            return "des"
    # user hits nothing
    else:
        return "miss"



# sets all enemy ships on the board
enemyLocs, enemyCarrier, enemyBattleship, enemyCruiser, enemySubmarine, enemyDestroyer = setEnemyShipLocations()
userLocs, userCarrier, userBattleship, userCruiser, userSubmarine, userDestroyer = setUserShipLocations()
# combines the ship coordinates into one list
allPossibleEnemyPoints = enemyCarrier + enemyBattleship + enemyCruiser + enemySubmarine + enemyDestroyer
allPossibleUserPoints = userCarrier[:]
allPossibleUserPoints.append(userBattleship)
allPossibleUserPoints.append(userCruiser)
allPossibleUserPoints.append(userSubmarine)
allPossibleUserPoints.append(userDestroyer)
#for testing purposes
##while allPossibleEnemyPoints != []:
##  #this is the line of code you would input to call users turn
##  enemyCarrier, enemyBattleship, enemyCruiser, enemySubmarine, enemyDestroyer = userTurn(allPossibleEnemyPoints, enemyCarrier, enemyBattleship, enemyCruiser, enemySubmarine, enemyDestroyer)
##  # updating allPossibleEnemyPoints
##  allPossibleEnemyPoints = enemyCarrier[:]
##  allPossibleEnemyPoints.append(enemyBattleship)
##  allPossibleEnemyPoints.append(enemyCruiser)
##  allPossibleEnemyPoints.append(enemySubmarine)
##  allPossibleEnemyPoints.append(enemyDestroyer)
##  # for quick testing purposes
##  print(allPossibleEnemyPoints)



##AI EXECUTION
playerShipsCoordinates = []
for x in enemyCarrier:
    playerShipsCoordinates.append(x)
for x in enemyBattleship:
    playerShipsCoordinates.append(x)
for x in enemyCruiser:
    playerShipsCoordinates.append(x)
for x in enemySubmarine:
    playerShipsCoordinates.append(x)
for x in enemyDestroyer:
    playerShipsCoordinates.append(x)

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
hitCoordinates = []
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
        print("The AI hit with a guess of ", guess)
        return True
    else:
        print("The AI missed with a guess of ", guess)
        return False

#Logic controller function. Will decide what kind of guess to perform
def ai_turn():
    if not(len(smartToGuess) == 0):
        return helper_afterhitGuess()
    else:
        return helper_randomGuess()
    print('AI guessed: ' + str(ai_turn()))

#print(playerShipsCoordinates)

answer = random.randint(1, 100)
compguess = random.randint(1,100)
userguess = None

##determine initial turn
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
    flagUserTurn = 1
    print("you win! you'll go first")
elif userdiff > compdiff:
    flagAITurn = 1
    print("you lose! the computer will go first")
else:
    flagUserTurn = 1
    print("it was a tie! you'll go first")

#toggle turns
def turnController():
    global flagAITurn, flagUserTurn, enemyCarrier, enemyBattleship, enemyCruiser, enemySubmarine, enemyDestroyer
    if flagAITurn == 1:
        ai_turn()
        flagAITurn = 0
        flagUserTurn = 1
    elif (flagUserTurn == 1):
        print(enemyCarrier)
        enemyCarrier, enemyBattleship, enemyCruiser, enemySubmarine, enemyDestroyer = userTurn(allPossibleEnemyPoints, enemyCarrier, enemyBattleship, enemyCruiser, enemySubmarine, enemyDestroyer)
        flagUserTurn = 0
        flagAITurn = 1

while True:
    turnController()
