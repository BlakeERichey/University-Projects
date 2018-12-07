# import necessary classes
import random

# establish all possible points
enemyBattlefield = [('a', 1), ('a', 2), ('a', 3), ('a', 4), ('a', 5), ('a', 6), ('a', 7), ('a', 8), ('a', 9), ('a', 10), ('b', 1), ('b', 2), ('b', 3), ('b', 4), ('b', 5), ('b', 6), ('b', 7), ('b', 8), ('b', 9), ('b', 10), ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5), ('c', 6), ('c', 7), ('c', 8), ('c', 9), ('c', 10), ('d', 1), ('d', 2), ('d', 3), ('d', 4), ('d', 5), ('d', 6), ('d', 7), ('d', 8), ('d', 9), ('d', 10), ('e', 1), ('e', 2), ('e', 3), ('e', 4), ('e', 5), ('e', 6), ('e', 7), ('e', 8), ('e', 9), ('e', 10), ('f', 1), ('f', 2), ('f', 3), ('f', 4), ('f', 5), ('f', 6), ('f', 7), ('f', 8), ('f', 9), ('f', 10), ('g', 1), ('g', 2), ('g', 3), ('g', 4), ('g', 5), ('g', 6), ('g', 7), ('g', 8), ('g', 9), ('g', 10), ('h', 1), ('h', 2), ('h', 3), ('h', 4), ('h', 5), ('h', 6), ('h', 7), ('h', 8), ('h', 9), ('h', 10), ('i', 1), ('i', 2), ('i', 3), ('i', 4), ('i', 5), ('i', 6), ('i', 7), ('i', 8), ('i', 9), ('i', 10), ('j', 1), ('j', 2), ('j', 3), ('j', 4), ('j', 5), ('j', 6), ('j', 7), ('j', 8), ('j', 9), ('j', 10)]

# establishing necessary variables
ships = [('carrier', 5), ('battleship', 4), ('cruiser', 3), ('submarine', 3), ('destroyer', 2)] # standard battleship names and sizes
enemyCarrier = []
enemyBattleship = []
enemyCruiser = []
enemySubmarine = []
enemyDestroyer = []
enemyLocs = [] # to be altered later

# setting up each ship location
def setEnemyShipLocations():
    # placing the carrier within boundaries
    enemyCarrier = setShipLocations(enemyBattlefield, ships[0][1])
    # ammending the complete list of coordinates
    enemyLocs = enemyCarrier[:]
    # placing the battleship within boundaries
    enemyBattleship = setShipLocations(enemyBattlefield, ships[1][1])
    # checking that the battleship does not overlap any previous ships
    enemyBattleship = checker(enemyLocs, enemyBattleship, ships[1][1])
    # ammedning the complete list of coordinates
    enemyLocs += enemyBattleship
    # placing the cruiser within boundaries
    enemyCruiser = setShipLocations(enemyBattlefield, ships[2][1])
    # checking that the cruiser does not overlap any previous ships
    enemyCruiser = checker(enemyLocs, enemyCruiser, ships[2][1])
    # ammedning the complete list of coordinates
    enemyLocs += enemyCruiser
    # placing the submarine within boundaries
    enemySubmarine = setShipLocations(enemyBattlefield, ships[3][1])
    # checking that the submarine does not overlap any previous ships
    enemySubmarine = checker(enemyLocs, enemySubmarine, ships[3][1])
    # ammedning the complete list of coordinates
    enemyLocs += enemySubmarine
    # placing the destroyer within boundaries
    enemyDestroyer = setShipLocations(enemyBattlefield, ships[4][1])
    # checking that the destroyer does not overlap any previous ships
    enemyDestroyer = checker(enemyLocs, enemyDestroyer, ships[4][1])
    # ammedning the complete list of coordinates
    enemyLocs += enemyDestroyer
    # returning complete list and individual coordinates
    return enemyLocs, enemyCarrier, enemyBattleship, enemyCruiser, enemySubmarine, enemyDestroyer

# placing a single ship when called. takes in all possible points and how many points needed
def setShipLocations(enemyBattlefield, shipLength):
    # establishing necessary variables
    counter = 1 # how many points have been placed
    directions = ['left','up','right','down'] # directions to place points
    shipLocation = [] # ship points
    # chosing a random point from all possible points
    placement = list(random.choice(enemyBattlefield))
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
def checker(setLocations, tester, length):
    # checks each individual point
    for i in tester:
        # against coordinates that have already been taken
        if i in setLocations:
            # if there is an overlap, the ship is set again
            tester = setShipLocations(enemyBattlefield, length)
            # and rechecked
            tester = checker(setLocations, tester, length)
    return tester
    
# this is the users turn, triggered by a flag
def userTurn(allPossiblePoints, c5Loc, b4Loc, c3Loc, s3Loc, d2Loc):
    # resets replacement variable - needed because tuples
    replacement = []
    # takes in the user's guess
    coordinate = helper_userGuess()
    print("Firing...")
    # determines if the guess is where an enemy has placed a ship
    hitOrMiss = helper_hitOrMiss(allPossiblePoints, c5Loc, b4Loc, c3Loc, s3Loc, d2Loc, coordinate)
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
    if 1 <= number <= 10:
        pass
    #if number is not valid, then takes another input
    else:
        print("Invalid coordinate, please try again.")
        helper_userGuess()
    # ensures the second imput( the number) is an integer
    coordinate[1] = int(number)
    # returns the coordinates as a tuple
    return coordinate

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
# combines the ship coordinates into one list
allPossiblePoints = enemyCarrier + enemyBattleship + enemyCruiser + enemySubmarine + enemyDestroyer
#for testing purposes
while allPossiblePoints != []:
  #this is the line of code you would input to call users turn
  enemyCarrier, enemyBattleship, enemyCruiser, enemySubmarine, enemyDestroyer = userTurn(allPossiblePoints, enemyCarrier, enemyBattleship, enemyCruiser, enemySubmarine, enemyDestroyer)
  # updating allPossiblePoints
  allPossiblePoints = enemyCarrier[:]
  allPossiblePoints.append(enemyBattleship)
  allPossiblePoints.append(enemyCruiser)
  allPossiblePoints.append(enemySubmarine)
  allPossiblePoints.append(enemyDestroyer)
  # for quick testing purposes
  print(allPossiblePoints)

  print("carrier", enemyCarrier)
