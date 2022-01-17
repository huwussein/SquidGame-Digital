# The following code runs the program: Squid Game
# Made by the Squid Game Dev Team A.K.A. Group 1

# Variables used throughout the code
currentScreen = 0
tutorialScreen = 0
manualScreen = 0
playerOne = 0
playerTwo = 0
playerThree = 0
playerFour = 0

# Basic requirments for the program
def setup():
    size(1000,600)
    textSize(15)
    background(0)
    
        
def draw():
    # Following function makes it possible to have multiple screens
    # currentScreen0 is the main menu screen
    # currentScreen1 is the playing screen
    # currentScreen3 is the manual for the game

    global currentScreen
    if currentScreen == 0:
        image(loadImage("Background.png"), 0, 0, 1000, 600)
        fill (255, 0, 186)
        rect(400, 300, 200, 100)
        rect(400, 450, 200, 100)

        fill(0)
        textSize(45)
        text("Play", 457,323,200,100)
        text("Tutorial", 417,473,200,100)
                

    elif currentScreen == 1:
        background(0)
        image(loadImage("Manual.png"), 900, 0, 100, 100)
        
        fill(255, 0, 186)
        rect(10, 10, 100, 50)
        fill(0)
        textSize(25)
        text("Back", 25,20,100,50)
        
        textSize(15)
        fill(255, 0, 186)
        rect(25, 300, 50, 50)
        rect(25, 375, 50, 50)
        rect(25, 450, 50, 50)
        rect(25, 525, 50, 50)
    
        rect(275, 300, 50, 50)
        rect(275, 375, 50, 50)
        rect(275, 450, 50, 50)
        rect(275, 525, 50, 50)
    
        rect(520, 300, 50, 50)
        rect(520, 375, 50, 50)
        rect(520, 450, 50, 50)
        rect(520, 525, 50, 50)
    
        rect(745, 300, 50, 50)
        rect(745, 375, 50, 50)
        rect(745, 450, 50, 50)
        rect(745, 525, 50, 50)
    
        fill(255, 0, 186)
        text(playerOne,150,300)
        text(playerTwo,400,300)
        text(playerThree,650,300)
        text(playerFour,880,300)
    
        fill(0, 0, 0)
        text("+500", 30, 325)
        text("-500", 30, 400)
        text("+100", 30, 475)
        text("-100", 30, 550)
    
        text("+500", 280, 325)
        text("-500", 280, 400)
        text("+100", 280, 475)
        text("-100", 280, 550)
    
        text("+500", 525, 325)
        text("-500", 525, 400)
        text("+100", 525, 475)
        text("-100", 525, 550)
    
        text("+500", 750, 325)
        text("-500", 750, 400)
        text("+100", 750, 475)
        text("-100", 750, 550)
        
    elif currentScreen == 2:
        background(0)
        
        global tutorialScreen
    
        if tutorialScreen == 0:
            background(0)
            image(loadImage("interactive_tutorial1.png"), 0, 0, 1000, 605)  
                
        elif tutorialScreen == 1:
            background(0)
            image(loadImage("interactive_tutorial2.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 2:
            background(0)
            image(loadImage("interactive_tutorial3.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 3:
            background(0)
            image(loadImage("interactive_tutorial4.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 4:
            background(0)
            image(loadImage("interactive_tutorial5.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 5:
            background(0)
            image(loadImage("interactive_tutorial6.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 6:
            background(0)
            image(loadImage("interactive_tutorial7.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 7:
            background(0)
            image(loadImage("interactive_tutorial8.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 8:
            background(0)
            image(loadImage("interactive_tutorial9.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 9:
            background(0)
            image(loadImage("interactive_tutorial10.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 10:
            background(0)
            image(loadImage("interactive_tutorial11.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 11:
            background(0)
            image(loadImage("interactive_tutorial12.png"), 0, 0, 1000, 605)
    
        elif tutorialScreen == 12:
            background(0)
            image(loadImage("interactive_tutorial13.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 13:
            background(0)
            image(loadImage("interactive_tutorial14.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 14:
            background(0)
            image(loadImage("interactive_tutorial15.png"), 0, 0, 1000, 605)
    
        elif tutorialScreen == 15:
            background(0)
            image(loadImage("interactive_tutorial16.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 16:
            background(0)
            image(loadImage("interactive_tutorial17.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 17:
            background(0)
            image(loadImage("interactive_tutorial18.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 18:
            background(0)
            image(loadImage("interactive_tutorial19.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 19:
            background(0)
            image(loadImage("interactive_tutorial20.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 20:
            background(0)
            image(loadImage("interactive_tutorial21.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 21:
            background(0)
            image(loadImage("interactive_tutorial22.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 22:
            background(0)
            image(loadImage("interactive_tutorial23.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 23:
            background(0)
            image(loadImage("interactive_tutorial24.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 24:
            background(0)
            image(loadImage("interactive_tutorial25.png"), 0, 0, 1000, 605)

        elif tutorialScreen == 25:
            background(0)
            image(loadImage("interactive_tutorial26.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 26:
            background(0)
            image(loadImage("interactive_tutorial27.png"), 0, 0, 1000, 605)
    
        elif tutorialScreen == 27:
            background(0)
            image(loadImage("interactive_tutorial28.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 28:
            background(0)
            image(loadImage("interactive_tutorial29.png"), 0, 0, 1000, 605)
    
        elif tutorialScreen == 29:
            background(0)
            image(loadImage("interactive_tutorial30.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 30:
            background(0)
            image(loadImage("interactive_tutorial31.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 31:
            background(0)
            image(loadImage("interactive_tutorial32.png"), 0, 0, 1000, 605)
        
        elif tutorialScreen == 32:
            background(0)
            image(loadImage("interactive_tutorial33.png"), 0, 0, 1000, 605)
            
        elif tutorialScreen >= 33:
            image(loadImage("Background.png"), 0, 0, 1000, 600)
            fill (255, 0, 186)
            rect(400, 300, 200, 100)
            rect(400, 450, 200, 100)

            fill(0)
            textSize(45)
            text("Play", 457,323,200,100)
            text("Tutorial", 417,473,200,100)
            


        
    elif currentScreen == 3:
        background(0)
        
        global manualScreen
    
        if manualScreen == 0:
            background(0)
            image(loadImage("Manual1.png"), 0, 0, 1000, 605)  
                
        elif manualScreen == 1:
            background(0)
            image(loadImage("Manual2.png"), 0, 0, 1000, 605)
            
        elif manualScreen >= 2:
            image(loadImage("Background.png"), 0, 0, 1000, 600)
            fill (255, 0, 186)
            rect(400, 300, 200, 100)
            rect(400, 450, 200, 100)

            fill(0)
            textSize(45)
            text("Play", 457,323,200,100)
            text("Tutorial", 417,473,200,100)
        
def mousePressed():
    global currentScreen
    if currentScreen == 0:
        if 400 < mouseX < 400+200 and 300 < mouseY < 300+100:
            currentScreen = 1
        
        global currentScreen
        if 400 < mouseX < 400+200 and 450 < mouseY < 450+100:
            currentScreen = 2
        
    global currentScreen
    if currentScreen == 1:
        if 900 < mouseX < 900+100 and 0 < mouseY < 0+100:
            currentScreen = 3
        
    global currentScreen
    if 10 < mouseX < 10+100 and 10 < mouseY < 10+50:
        currentScreen = 0
        
    global tutorialScreen
    if tutorialScreen >= 33:
        if 400 < mouseX < 400+200 and 300 < mouseY < 300+100:
            currentScreen = 1
            
        if 400 < mouseX < 400+200 and 450 < mouseY < 450+100:
            tutorialScreen = 1
            
    global manualScreen
    if manualScreen >= 2:
        if 400 < mouseX < 400+200 and 300 < mouseY < 300+100:
            currentScreen = 1
            
        if 400 < mouseX < 400+200 and 450 < mouseY < 450+100:
            tutorialScreen = 1

        
def mouseClicked(): 
    global playerOne
    if currentScreen == 1:
        if 25 < mouseX < 25+50 and 300 < mouseY < 300+50:
            playerOne = playerOne + 500
            
        if 25 < mouseX < 25+50 and 375 < mouseY < 375+50:
            playerOne = playerOne - 500
            
        if 25 < mouseX < 25+50 and 450 < mouseY < 450+50:
            playerOne = playerOne + 100
            
        if 25 < mouseX < 25+50 and 525 < mouseY < 525+50:
            playerOne = playerOne - 100
        
        
        
            global playerTwo
            
        if 275 < mouseX < 275+50 and 300 < mouseY < 300+50:
            playerTwo = playerTwo + 500
            
        if 275 < mouseX < 275+50 and 375 < mouseY < 375+50:
            playerTwo = playerTwo - 500
    
        if 275 < mouseX < 275+50 and 450 < mouseY < 450+50:
            playerTwo = playerTwo + 100
            
        if 275 < mouseX < 275+50 and 525 < mouseY < 525+50:
            playerTwo = playerTwo - 100
            
            
            
            global playerThree
        if 520 < mouseX < 520+50 and 300 < mouseY < 300+50:
            playerThree = playerThree + 500
            
        if 520 < mouseX < 520+50 and 375 < mouseY < 375+50:
            playerThree = playerThree - 500
    
        if 520 < mouseX < 520+50 and 450 < mouseY < 450+50:
            playerThree = playerThree + 100
            
        if 520 < mouseX < 520+50 and 525 < mouseY < 525+50:
            playerThree = playerThree - 100
            
            
            global playerFour
        if 745 < mouseX < 745+50 and 300 < mouseY < 300+50:
            playerFour = playerFour + 500
            
        if 745 < mouseX < 745+50 and 375 < mouseY < 375+50:
            playerFour = playerFour - 500
            
        if 745 < mouseX < 745+50 and 450 < mouseY < 450+50:
            playerFour = playerFour + 100
            
        if 745 < mouseX < 745+50 and 525 < mouseY < 525+50:
            playerFour = playerFour - 100
        
            
def keyPressed():
    global tutorialScreen
    tutorialScreen += 1
    
    global manualScreen
    manualScreen += 1
