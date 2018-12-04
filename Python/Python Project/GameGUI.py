import pygame, time

def run_game():
    pygame.init()

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    background = (230, 230, 230)
    backgroundImage=pygame.image.load('./resources/background.jpg')

    display_width = 1200
    display_height = 700

    Battlefield = pygame.image.load('./resources/Battlefield.png')
    
    ##NUMPAD COMPONENT
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




    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Uber Fantastic Mega Amazing Ultra Devastating Battleship Experience')
    clock = pygame.time.Clock()
    gameDisplay.fill(background)

    #gameDisplay.blit(shipImg, (400, 400))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #Monitor when mouse is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                #get position of mouse and save it ss mx and my
                mx, my = pygame.mouse.get_pos()

                #button 1 is pressed
                if ((mx > 1100) and (my < 150 and my > 100)):
                    print("1")
                

        gameDisplay.blit(backgroundImage, (0, 0))

        #player battlefield
        gameDisplay.blit(Battlefield, (100, 200))

        #ai battlefield
        gameDisplay.blit(Battlefield, (550, 200))
        
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
        
        time.sleep(0.03)
        pygame.display.update()
        
run_game()
