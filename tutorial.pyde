currentScreen = 0

def setup():
    size(1000,600)
    textSize(15)
    background(0)
    
def draw():

    global currentScreen
    if currentScreen == 0:
        background(0)
        image(loadImage("InkedBackground1_LI.jpg"), 0, 0, 1000, 600)
        
    elif currentScreen == 1:
        background(0)
        image(loadImage("Background1.png"), 0, 0, 1000, 600)
        
    elif currentScreen == 2:
        background(0)
        image(loadImage("Background1 - kopie.png"), 0, 0, 1000, 600)


def keyPressed():
    global currentScreen
    currentScreen = currentScreen + 1
