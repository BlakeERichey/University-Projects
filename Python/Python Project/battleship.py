# import necessary classes
import random

flagUserTurn = 0;
flagAITurn = 1;
PLAYERWINS=False
AIWINS=False

AIHitList = []
AIMissList = []

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
coordinate = ""

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

def checkForWinner():
    global playerShipsCoordinates, enemyLocs, AIWINS, PLAYERWINS
    if playerShipsCoordinates == []:
        AIWINS=True
        return True
    elif enemyLocs == []:
        PLAYERWINS=True
        return True
    else:
        return False

def setUserShipLocations():
    global userCarrier, userBattleship, userCruiser, userSubmarine, userDestroyer, userLocs
    # placing the carrier within boundaries
    userCarrier = setShipLocations(battlefield, ships[0][1])
    userLocs = userCarrier[:]
    # placing the battleship within boundaries
    userBattleship = setShipLocations(battlefield, ships[1][1])
    userBattleship = userChecker(userLocs, userBattleship, ships[1][1])
    for s in userBattleship:
        userLocs.append(s)
    # placing the cruiser within boundaries
    userCruiser = setShipLocations(battlefield, ships[2][1])
    userCruiser = userChecker(userLocs, userCruiser, ships[2][1])
    for s in userCruiser:
        userLocs.append(s)
    # placing the submarine within boundaries
    userSubmarine = setShipLocations(battlefield, ships[3][1])
    userSubmarine = userChecker(userLocs, userSubmarine, ships[3][1])
    for s in userSubmarine:
        userLocs.append(s)
    # placing the destroyer within boundaries
    userDestroyer = setShipLocations(battlefield, ships[4][1])
    userDestroyer = userChecker(userLocs, userDestroyer, ships[4][1])
    for s in userDestroyer:
        userLocs.append(s)
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
    return tester

# this is the users turn, triggered by a flag
def userTurn(allPossiblePoints, c5Loc, b4Loc, c3Loc, s3Loc, d2Loc, coordinate):
    # resets replacement variable - needed because tuples
    replacement = []
    # takes in the user's guess
    coordinate = helper_userGuessCheck(coordinate)
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
    global coordinate
    #coordinate = input("Where would you like to aim? ")
    # checks that the imput is valid
    coordinate = helper_userGuessCheck(coordinate)
    # returns valid input as a tuple
    return tuple(coordinate)
        
# checks that user input is within boundaries
def helper_userGuessCheck(userInput):
    global coordinate
    # turns string into list
    coordinate = list(userInput)
    #changes 0 into 10
    if coordinate[1] == '0':
        coordinate[1] = 10
    # returns the coordinates as a tuple
    coordinate = tuple(coordinate)
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
print(userCarrier, userBattleship, userCruiser, userSubmarine, userDestroyer)
for x in userCarrier:
    playerShipsCoordinates.append(x)
for x in userBattleship:
    playerShipsCoordinates.append(x)
for x in userCruiser:
    playerShipsCoordinates.append(x)
for x in userSubmarine:
    playerShipsCoordinates.append(x)
for x in userDestroyer:
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
availableGuesses = playerBattlefield

#for use with afterHitGuess() to make more intelligent decisions
hitCoordinates = []
smartToGuess = []
smartGuessed = []

#Guesses randomly a location on the board that has not been chosen yet.
#then shortens the list of remaining available guesses and
#appends the list of already guessed guesses
#guess is the current guess, returned after verifying the guess is valid.
def helper_randomGuess():
    global availableGuesses, hitCoordinates, smartToGuess, smartGuessed
    if (len(availableGuesses) == 0):
        return "No more guesses left"
    guess = random.choice(availableGuesses)
    availableGuesses.remove(guess)
    alreadyGuessed.append(guess)
    helper_didhit(guess)
    return guess

def helper_afterhitGuess():
    global availableGuesses, hitCoordinates, smartToGuess, smartGuessed
    guess = None #give guess function scope
    guess = random.choice(smartToGuess)
    smartToGuess.remove(guess)
    if guess in availableGuesses:
        print("testing... guess is" + str(guess))
        smartGuessed.append(guess)
        availableGuesses.remove(guess)
        alreadyGuessed.append(guess)
        helper_didhit(guess)
        return guess
    else:
        helper_afterhitGuess()

#returns if the guess accurately guessed a ships location
def helper_didhit(guess):
    global availableGuesses, hitCoordinates, smartToGuess, smartGuessed, playerShipsCoordinates, AIHitList, AIMissList
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
        playerShipsCoordinates.remove(guess)
        AIHitList.append(guess)
        print("Hit!", guess)
        #return True
    else:
        AIMissList.append(guess)
        print("Miss", guess)
        #return False

#Logic controller function. Will decide what kind of guess to perform
def helper_attack():
    global availableGuesses, hitCoordinates, smartToGuess, smartGuessed
    if not(len(smartToGuess) == 0):
        return helper_afterhitGuess()
    else:
        return helper_randomGuess()
    

#print(playerShipsCoordinates)

answer = random.randint(1, 100)
compguess = random.randint(1,10)
userguess = None

##determine initial turn
def userMiniGameGuess():
    global userguess, flagAITurn, flagUserTurn
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
    global flagAITurn, flagUserTurn
    if flagAITurn == 1:
        helper_attack()
        flagAITurn = 0
        flagUserTurn = 1

##GUI Main Game
import pygame, time
gamePadCoordinate = ""

def run_game():
    pygame.init()

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    background = (230, 230, 230)
    backgroundImage=pygame.image.load('./resources/background.jpg')
    backgroundTitle=pygame.image.load('./resources/TitleScreen.jpg')
    howTo1=pygame.image.load('./resources/HowTo1.png')
    howTo2=pygame.image.load('./resources/HowTo2.png')
    howTo3=pygame.image.load('./resources/HowTo3.png')
    cheatScreen=pygame.image.load('./resources/CheatsScreen.jpg')
    backgroundHighScores=pygame.image.load('./resources/ScoresScreen.jpg')
    hitIcon=pygame.image.load('./resources/hitIcon.png')
    missIcon=pygame.image.load('./resources/missIcon.png')
    WinScreen=pygame.image.load('./resources/Win.jpg')
    GameOverScreen=pygame.image.load('./resources/GameOver.jpg')
    minigame=pygame.image.load('./resources/minigame.jpg')

    
    display_width = 1200
    display_height = 700
    Battlefield = pygame.image.load('./resources/Battlefield.png')

    numPad1 = pygame.image.load('./resources/numPad1.png')
    numPad2 = pygame.image.load('./resources/numPad2.png')
    numPad3 = pygame.image.load('./resources/numPad3.png')
    numPad4 = pygame.image.load('./resources/numPad4.png')
    numPad5 = pygame.image.load('./resources/numPad5.png')
    numPad6 = pygame.image.load('./resources/numPad6.png')
    numPad7 = pygame.image.load('./resources/numPad7.png')
    numPad8 = pygame.image.load('./resources/numPad8.png')
    numPad9 = pygame.image.load('./resources/numPad9.png')
    numPad10 = pygame.image.load('./resources/numPad10.png')
    numPadA = pygame.image.load('./resources/numPadA.png')
    numPadB = pygame.image.load('./resources/numPadB.png')
    numPadC = pygame.image.load('./resources/numPadC.png')
    numPadD = pygame.image.load('./resources/numPadD.png')
    numPadE = pygame.image.load('./resources/numPadE.png')
    numPadF = pygame.image.load('./resources/numPadF.png')
    numPadG = pygame.image.load('./resources/numPadG.png')
    numPadH = pygame.image.load('./resources/numPadH.png')
    numPadI = pygame.image.load('./resources/numPadI.png')
    numPadJ = pygame.image.load('./resources/numPadJ.png')
    numPadFire = pygame.image.load('./resources/numPadFire.png')
    VCarSprite = pygame.image.load('./resources/CarrierA.png')
    VBatSprite = pygame.image.load('./resources/BattleshipA.png')
    VCruSprite = pygame.image.load('./resources/CruiserA.png')
    VSubSprite = pygame.image.load('./resources/SubmarineA.png')
    VDesSprite = pygame.image.load('./resources/DestroyerA.png')
    HCarSprite = pygame.image.load('./resources/CarrierB.png')
    HBatSprite = pygame.image.load('./resources/BattleshipB.png')
    HCruSprite = pygame.image.load('./resources/CruiserB.png')
    HSubSprite = pygame.image.load('./resources/SubmarineB.png')
    HDesSprite = pygame.image.load('./resources/DestroyerB.png')

    


    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Amazing Brilliantly/Creatively Developed Eccentric Fabulous GUI for BattleShip PC!')
    clock = pygame.time.Clock()
    gameDisplay.fill(background)

    #gameDisplay.blit(shipImg, (400, 400))
    pygame.display.update()

    hitList= []
    missList = []

    Title = True
    mainGame = False
    miniGame = False
    HowTo1 = False
    HowTo2 = False
    HowTo3 = False
    CheatMenu = False
    CheatReveal = False
    GameOver=False
    Win=False

    while True:
        global flagUserTurn, flagAITurn
        while Title:
         for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                #Monitor when mouse is pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #get position of mouse and save it ss mx and my
                    mx, my = pygame.mouse.get_pos()

                    #play
                    if ((mx < 155  and mx > 40) and (my < 400 and 365 < my)):
                        #userMiniGameGuess()
                        Title = False
                        if flagAITurn == 1:
                            miniGame = True
                        else:
                            mainGame=True

                    #How to play
                    if ((mx < 375  and mx > 40) and (my < 495 and my > 445)):
                        Title=False
                        HowTo1=True
                        print("How to play")

                    #Cheats
                    if ((mx < 200  and mx > 40) and (my < 575 and my > 535)):
                        Title=False
                        CheatMenu=True
                        

                gameDisplay.fill(background)

                gameDisplay.blit(backgroundTitle, (0, 0))
                time.sleep(.03)
                pygame.display.update()

        while Win:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
                #Monitor when mouse is pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #get position of mouse and save it ss mx and my
                    mx, my = pygame.mouse.get_pos()

                gameDisplay.fill(background)

                gameDisplay.blit(WinScreen, (0, 0))
                time.sleep(.03)
                pygame.display.update()

        while GameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
                #Monitor when mouse is pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #get position of mouse and save it ss mx and my
                    mx, my = pygame.mouse.get_pos()

                gameDisplay.fill(background)

                gameDisplay.blit(GameOverScreen, (0, 0))
                time.sleep(.03)
                pygame.display.update()
                
        while HowTo1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()       

            gameDisplay.fill(background)

            gameDisplay.blit(howTo1, (0, 0))
            pygame.display.update()
            time.sleep(5)
            HowTo1=False
            HowTo2=True
                
        while HowTo2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()       

            gameDisplay.fill(background)

            gameDisplay.blit(howTo2, (0, 0))
            pygame.display.update()
            time.sleep(5)
            HowTo2=False
            HowTo3=True

        while HowTo3:
##            for event in pygame.event.get():
##                if event.type == pygame.QUIT:
##                    pygame.quit()
##                    quit()       

            gameDisplay.fill(background)

            gameDisplay.blit(howTo3, (0, 0))
            pygame.display.update()
            time.sleep(5)
            HowTo3=False
            Title=True
                
        while CheatMenu:
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                #Monitor when mouse is pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #get position of mouse and save it ss mx and my
                    mx, my = pygame.mouse.get_pos()

                    #return to main menu
                    if ((mx < 108  and mx > 70) and (my < 70 and my > 52)):
                        CheatMenu=False
                        Title=True
                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                         flagAITurn = 0
                         flagUserTurn = 1
                         
                    if event.key == pygame.K_r:
                        CheatReveal = True
                          

                gameDisplay.fill(background)

                gameDisplay.blit(cheatScreen, (0, 0))
                time.sleep(.03)
                pygame.display.update()

        while miniGame:
            global userguess
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
                #Monitor when mouse is pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #get position of mouse and save it ss mx and my
                    mx, my = pygame.mouse.get_pos()

                gameDisplay.fill(background)

                gameDisplay.blit(minigame, (0, 0))
                #render buttons
                gameDisplay.blit(numPad1, (550, 100))
                gameDisplay.blit(numPad2, (550, 150))
                gameDisplay.blit(numPad3, (550, 200))
                gameDisplay.blit(numPad4, (550, 250))
                gameDisplay.blit(numPad5, (550, 300))
                gameDisplay.blit(numPad6, (550, 350))
                gameDisplay.blit(numPad7, (550, 400))
                gameDisplay.blit(numPad8, (550, 450))
                gameDisplay.blit(numPad9, (550, 500))
                gameDisplay.blit(numPad10, (550, 550))

                if userguess == None:
                    #button 1 is pressed
                    if ((550 < mx < 650) and (my < 150 and my > 100)):
                        userguess = 1
                    #button 2 is pressed
                    if ((550 < mx < 650) and (my < 200 and my > 150)):
                        userguess = 2
                    #button 3 is pressed
                    if ((550 < mx < 650) and (my < 250 and my > 200)):
                        userguess = 3
                    #button 4 is pressed
                    if ((550 < mx < 650) and (my < 300 and my > 250)):
                        userguess = 4
                    #button 5 is pressed
                    if ((550 < mx < 650) and (my < 350 and my > 300)):
                        userguess = 5
                    #button 6 is pressed
                    if ((550 < mx < 650) and (my < 400 and my > 350)):
                        userguess = 6
                    #button 7 is pressed
                    if ((550 < mx < 650) and (my < 450 and my > 400)):
                        userguess = 7
                    #button 8 is pressed
                    if ((550 < mx < 650) and (my < 500 and my > 450)):
                        userguess = 8
                    #button 9 is pressed
                    if ((550 < mx < 650) and (my < 550 and my > 500)):
                        userguess = 9
                    #button 0 is pressed
                    if ((550 < mx < 650) and (my < 600 and my > 550)):
                        userguess = 10

                if not(userguess == None):
                    userMiniGameGuess()
                    miniGame = False
                    mainGame= True
                    
                time.sleep(.03)
                pygame.display.update()
            

        while mainGame:
            global enemyCarrier, enemyBattleship, enemyCruiser, enemySubmarine, enemyDestroyer, gamePadCoordinate, enemyLocs, playerShipsCoordinates,  AIHitList, AIMissList
            global userCarrier, userDestroyer, userBattleship, userSubmarine, userCruiser, AIWINS, PLAYERWINS

            turnController()
    
            if checkForWinner():
                if AIWINS == True:
                    mainGame=False
                    GameOver=True
                elif PLAYERWINS == True:
                    mainGame = False
                    Win = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                #Monitor when mouse is pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #get position of mouse and save it ss mx and my
                    mx, my = pygame.mouse.get_pos()

##                    if ((mx < 30 and mx > 187) and (my < 77 and my > 22)):
##                        init();
##                        exit();


                    if len(gamePadCoordinate) == 0:
                        #button a is pressed
                        if ((mx < 1090 and mx > 1000) and (my < 150 and my > 100)):
                            gamePadCoordinate += "a"
                        #button b is pressed
                        if ((mx < 1090 and mx > 1000) and (my < 200 and my > 150)):
                            gamePadCoordinate += "b"                    
                        #button c is pressed
                        if ((mx < 1090 and mx > 1000) and (my < 250 and my > 200)):
                            gamePadCoordinate += "c" 
                        #button d is pressed
                        if ((mx < 1090 and mx > 1000) and (my < 300 and my > 250)):
                            gamePadCoordinate += "d"
                        #button e is pressed
                        if ((mx < 1090 and mx > 1000) and (my < 350 and my > 300)):
                            gamePadCoordinate += "e"
                        #button f is pressed
                        if ((mx < 1090 and mx > 1000) and (my < 400 and my > 350)):
                            gamePadCoordinate += "f"
                        #button g is pressed
                        if ((mx < 1090 and mx > 1000) and (my < 450 and my > 400)):
                            gamePadCoordinate += "g"
                        #button h is pressed
                        if ((mx < 1090 and mx > 1000) and (my < 500 and my > 450)):
                            gamePadCoordinate += "h"
                        #button i is pressed
                        if ((mx < 1090 and mx > 1000) and (my < 550 and my > 500)):
                            gamePadCoordinate += "i"
                        #button j is pressed
                        if ((mx < 1090 and mx > 1000) and (my < 600 and my > 550)):
                            gamePadCoordinate += "j"
                    
                        
                    elif (len(gamePadCoordinate) == 1):
                        #button 1 is pressed
                        if ((mx > 1090) and (my < 150 and my > 100)):
                            gamePadCoordinate += "1"
                        #button 2 is pressed
                        if ((mx > 1090) and (my < 200 and my > 150)):
                            gamePadCoordinate += "2"
                        #button 3 is pressed
                        if ((mx > 1090) and (my < 250 and my > 200)):
                            gamePadCoordinate += "3"
                        #button 4 is pressed
                        if ((mx > 1090) and (my < 300 and my > 250)):
                            gamePadCoordinate += "4"
                        #button 5 is pressed
                        if ((mx > 1090) and (my < 350 and my > 300)):
                            gamePadCoordinate += "5"
                        #button 6 is pressed
                        if ((mx > 1090) and (my < 400 and my > 350)):
                            gamePadCoordinate += "6"
                        #button 7 is pressed
                        if ((mx > 1090) and (my < 450 and my > 400)):
                            gamePadCoordinate += "7"
                        #button 8 is pressed
                        if ((mx > 1090) and (my < 500 and my > 450)):
                            gamePadCoordinate += "8"
                        #button 9 is pressed
                        if ((mx > 1090) and (my < 550 and my > 500)):
                            gamePadCoordinate += "9"
                        #button 0 is pressed
                        if ((mx > 1090) and (my < 600 and my > 550)):
                            gamePadCoordinate += "0"

                    if flagUserTurn == 1 and len(gamePadCoordinate)==2:
                        if ((mx > 1000) and (my < 700 and my > 600)):
                            #guess = "('" + gamePadCoordinate[0] + "', " + gamePadCoordinate[1] + ")"
                            guess=list(gamePadCoordinate)
                            guess[1] = int(guess[1])
                            if guess[1] == 0:
                                guess[1] = 10
                            guess = tuple(guess)
    
                            if guess in enemyLocs:
                                hitList.append(gamePadCoordinate)
                                enemyLocs.remove(guess)
                            else:
                                missList.append(gamePadCoordinate);
                            enemyCarrier, enemyBattleship, enemyCruiser, enemySubmarine, enemyDestroyer = userTurn(allPossibleEnemyPoints, enemyCarrier, enemyBattleship, enemyCruiser, enemySubmarine, enemyDestroyer, gamePadCoordinate)
                            flagUserTurn = 0
                            flagAITurn = 1
                            gamePadCoordinate = ""
        
                    
                        
            gameDisplay.fill(background)

            gameDisplay.blit(backgroundImage, (0, 0))

            #player battlefield
            gameDisplay.blit(Battlefield, (100, 200))

            ##render Player ships
            if userCarrier[0][0] == userCarrier[1][0]: #means ship is horizontal
                userCarrier.sort(key = lambda x: int(x[1])) #sort by horizontal
                xcoord=32*(userCarrier[0][1] - 1)+137
                ycoord=32*(ord(userCarrier[0][0])%96 - 1)+237
                pixels = []
                pixels.append(xcoord)
                pixels.append(ycoord)
                pixels = tuple(pixels)
                gameDisplay.blit(HCarSprite, pixels)
            else:
                userCarrier.sort(key = lambda x: x[0]) #sort by vertical
                xcoord=32*(userCarrier[0][1] - 1)+137
                ycoord=32*(ord(userCarrier[0][0])%96 - 1)+237
                pixels = []
                pixels.append(xcoord)
                pixels.append(ycoord)
                pixels = tuple(pixels)
                gameDisplay.blit(VCarSprite, pixels)

            if userBattleship[0][0] == userBattleship[1][0]:
                userBattleship.sort(key = lambda x: int(x[1])) #sort by horizontal
                xcoord=32*(userBattleship[0][1] - 1)+137
                ycoord=32*(ord(userBattleship[0][0])%96 - 1)+237
                pixels = []
                pixels.append(xcoord)
                pixels.append(ycoord)
                pixels = tuple(pixels)
                gameDisplay.blit(HBatSprite, pixels)
            else:
                userBattleship.sort(key = lambda x: x[0]) #sort by vertical
                xcoord=32*(userBattleship[0][1] - 1)+137
                ycoord=32*(ord(userBattleship[0][0])%96 - 1)+237
                pixels = []
                pixels.append(xcoord)
                pixels.append(ycoord)
                pixels = tuple(pixels)
                gameDisplay.blit(VBatSprite, pixels)

            if userCruiser[0][0] == userCruiser[1][0]:
                userCruiser.sort(key = lambda x: int(x[1])) #sort by horizontal
                xcoord=32*(userCruiser[0][1] - 1)+137
                ycoord=32*(ord(userCruiser[0][0])%96 - 1)+237
                pixels = []
                pixels.append(xcoord)
                pixels.append(ycoord)
                pixels = tuple(pixels)
                gameDisplay.blit(HCruSprite, pixels)
            else:
                userCruiser.sort(key = lambda x: x[0]) #sort by vertical
                xcoord=32*(userCruiser[0][1] - 1)+137
                ycoord=32*(ord(userCruiser[0][0])%96 - 1)+237
                pixels = []
                pixels.append(xcoord)
                pixels.append(ycoord)
                pixels = tuple(pixels)
                gameDisplay.blit(VCruSprite, pixels)
                
            if userSubmarine[0][0] == userSubmarine[1][0]:
                userSubmarine.sort(key = lambda x: int(x[1])) #sort by horizontal
                xcoord=32*(userSubmarine[0][1] - 1)+137
                ycoord=32*(ord(userSubmarine[0][0])%96 - 1)+237
                pixels = []
                pixels.append(xcoord)
                pixels.append(ycoord)
                pixels = tuple(pixels)
                gameDisplay.blit(HSubSprite, pixels)
            else:
                userSubmarine.sort(key = lambda x: x[0]) #sort by vertical
                xcoord=32*(userSubmarine[0][1] - 1)+137
                ycoord=32*(ord(userSubmarine[0][0])%96 - 1)+237
                pixels = []
                pixels.append(xcoord)
                pixels.append(ycoord)
                pixels = tuple(pixels)
                gameDisplay.blit(VSubSprite, pixels)

            if userDestroyer[0][0] == userDestroyer[1][0]:
                userDestroyer.sort(key = lambda x: int(x[1])) #sort by horizontal
                xcoord=32*(userDestroyer[0][1] - 1)+137
                ycoord=32*(ord(userDestroyer[0][0])%96 - 1)+237
                pixels = []
                pixels.append(xcoord)
                pixels.append(ycoord)
                pixels = tuple(pixels)
                gameDisplay.blit(HDesSprite, pixels)
            else:
                userDestroyer.sort(key = lambda x: x[0]) #sort by vertical
                xcoord=32*(userDestroyer[0][1] - 1)+137
                ycoord=32*(ord(userDestroyer[0][0])%96 - 1)+237
                pixels = []
                pixels.append(xcoord)
                pixels.append(ycoord)
                pixels = tuple(pixels)
                gameDisplay.blit(VDesSprite, pixels)

            #ai battlefield
            gameDisplay.blit(Battlefield, (550, 200))

            ##Render AI ships
            if CheatReveal:
                if enemyCarrier[0][0] == enemyCarrier[1][0]: #means ship is horizontal
                    enemyCarrier.sort(key = lambda x: int(x[1])) #sort by horizontal
                    xcoord=32*(enemyCarrier[0][1] - 1)+587
                    ycoord=32*(ord(enemyCarrier[0][0])%96 - 1)+237
                    pixels = []
                    pixels.append(xcoord)
                    pixels.append(ycoord)
                    pixels = tuple(pixels)
                    gameDisplay.blit(HCarSprite, pixels)
                else:
                    enemyCarrier.sort(key = lambda x: x[0]) #sort by vertical
                    xcoord=32*(enemyCarrier[0][1] - 1)+587
                    ycoord=32*(ord(enemyCarrier[0][0])%96 - 1)+237
                    pixels = []
                    pixels.append(xcoord)
                    pixels.append(ycoord)
                    pixels = tuple(pixels)
                    gameDisplay.blit(VCarSprite, pixels)

                if enemyBattleship[0][0] == enemyBattleship[1][0]:
                    enemyBattleship.sort(key = lambda x: int(x[1])) #sort by horizontal
                    xcoord=32*(enemyBattleship[0][1] - 1)+587
                    ycoord=32*(ord(enemyBattleship[0][0])%96 - 1)+237
                    pixels = []
                    pixels.append(xcoord)
                    pixels.append(ycoord)
                    pixels = tuple(pixels)
                    gameDisplay.blit(HBatSprite, pixels)
                else:
                    enemyBattleship.sort(key = lambda x: x[0]) #sort by vertical
                    xcoord=32*(enemyBattleship[0][1] - 1)+587
                    ycoord=32*(ord(enemyBattleship[0][0])%96 - 1)+237
                    pixels = []
                    pixels.append(xcoord)
                    pixels.append(ycoord)
                    pixels = tuple(pixels)
                    gameDisplay.blit(VBatSprite, pixels)

                if enemyCruiser[0][0] == enemyCruiser[1][0]:
                    enemyCruiser.sort(key = lambda x: int(x[1])) #sort by horizontal
                    xcoord=32*(enemyCruiser[0][1] - 1)+587
                    ycoord=32*(ord(enemyCruiser[0][0])%96 - 1)+237
                    pixels = []
                    pixels.append(xcoord)
                    pixels.append(ycoord)
                    pixels = tuple(pixels)
                    gameDisplay.blit(HCruSprite, pixels)
                else:
                    enemyCruiser.sort(key = lambda x: x[0]) #sort by vertical
                    xcoord=32*(enemyCruiser[0][1] - 1)+587
                    ycoord=32*(ord(enemyCruiser[0][0])%96 - 1)+237
                    pixels = []
                    pixels.append(xcoord)
                    pixels.append(ycoord)
                    pixels = tuple(pixels)
                    gameDisplay.blit(VCruSprite, pixels)
                    
                if enemySubmarine[0][0] == enemySubmarine[1][0]:
                    enemySubmarine.sort(key = lambda x: int(x[1])) #sort by horizontal
                    xcoord=32*(enemySubmarine[0][1] - 1)+587
                    ycoord=32*(ord(enemySubmarine[0][0])%96 - 1)+237
                    pixels = []
                    pixels.append(xcoord)
                    pixels.append(ycoord)
                    pixels = tuple(pixels)
                    gameDisplay.blit(HSubSprite, pixels)
                else:
                    enemySubmarine.sort(key = lambda x: x[0]) #sort by vertical
                    xcoord=32*(enemySubmarine[0][1] - 1)+587
                    ycoord=32*(ord(enemySubmarine[0][0])%96 - 1)+237
                    pixels = []
                    pixels.append(xcoord)
                    pixels.append(ycoord)
                    pixels = tuple(pixels)
                    gameDisplay.blit(VSubSprite, pixels)

                if enemyDestroyer[0][0] == enemyDestroyer[1][0]:
                    enemyDestroyer.sort(key = lambda x: int(x[1])) #sort by horizontal
                    xcoord=32*(enemyDestroyer[0][1] - 1)+587
                    ycoord=32*(ord(enemyDestroyer[0][0])%96 - 1)+237
                    pixels = []
                    pixels.append(xcoord)
                    pixels.append(ycoord)
                    pixels = tuple(pixels)
                    gameDisplay.blit(HDesSprite, pixels)
                else:
                    enemyDestroyer.sort(key = lambda x: x[0]) #sort by vertical
                    xcoord=32*(enemyDestroyer[0][1] - 1)+587
                    ycoord=32*(ord(enemyDestroyer[0][0])%96 - 1)+237
                    pixels = []
                    pixels.append(xcoord)
                    pixels.append(ycoord)
                    pixels = tuple(pixels)
                    gameDisplay.blit(VDesSprite, pixels)

            for miss in AIMissList:
                num=int(miss[1])
                if num == 0:
                    num = 10
                xcoord=32*(num - 1)+137
                ycoord=32*(ord(miss[0])%96 - 1)+237
                gameDisplay.blit(missIcon, (xcoord, ycoord))
                
            for hit in AIHitList:
                num=int(hit[1])
                if num == 0:
                    num = 10
                xcoord=32*(num - 1)+137
                ycoord=32*(ord(hit[0])%96 - 1)+237
                gameDisplay.blit(hitIcon, (xcoord, ycoord))

            for miss in missList:
                num=int(miss[1])
                if num == 0:
                    num = 10
                xcoord=32*(num - 1)+587
                ycoord=32*(ord(miss[0])%96 - 1)+237
                gameDisplay.blit(missIcon, (xcoord, ycoord))
                
            for hit in hitList:
                num=int(hit[1])
                if num == 0:
                    num = 10
                xcoord=32*((num) - 1)+587
                ycoord=32*(ord(hit[0])%96 - 1)+237
                gameDisplay.blit(hitIcon, (xcoord, ycoord))
            
            
            #render keypad
            gameDisplay.blit(numPadA, (1000, 100))
            gameDisplay.blit(numPadB, (1000, 150))
            gameDisplay.blit(numPadC, (1000, 200))
            gameDisplay.blit(numPadD, (1000, 250))
            gameDisplay.blit(numPadE, (1000, 300))
            gameDisplay.blit(numPadF, (1000, 350))
            gameDisplay.blit(numPadG, (1000, 400))
            gameDisplay.blit(numPadH, (1000, 450))
            gameDisplay.blit(numPadI, (1000, 500))
            gameDisplay.blit(numPadJ, (1000, 550))
            gameDisplay.blit(numPad1, (1100, 100))
            gameDisplay.blit(numPad2, (1100, 150))
            gameDisplay.blit(numPad3, (1100, 200))
            gameDisplay.blit(numPad4, (1100, 250))
            gameDisplay.blit(numPad5, (1100, 300))
            gameDisplay.blit(numPad6, (1100, 350))
            gameDisplay.blit(numPad7, (1100, 400))
            gameDisplay.blit(numPad8, (1100, 450))
            gameDisplay.blit(numPad9, (1100, 500))
            gameDisplay.blit(numPad10, (1100, 550))
            gameDisplay.blit(numPadFire, (1000, 600))

            
            
            time.sleep(.03)
            pygame.display.update()
        
run_game()
