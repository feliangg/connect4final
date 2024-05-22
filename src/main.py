#region VEXcode Generated Robot Configuration
#from gc import callbacks
import random
from vex import *

    # Brain should be defined by default
brain=Brain()

    # Robot configuration code
brain_inertial = Inertial()
controller = Controller()



    # Make random actually random
def setRandomSeedUsingAccel():
    wait(100, MSEC)
    xaxis = brain_inertial.acceleration(XAXIS) * 1000
    yaxis = brain_inertial.acceleration(YAXIS) * 1000
    zaxis = brain_inertial.acceleration(ZAXIS) * 1000
    random.seed(int(xaxis + yaxis + zaxis))
        
    # Set random seed 
setRandomSeedUsingAccel()

    #endregion VEXcode Generated Robot Configuration

    # ------------------------------------------
    # 
    # 	Project:      VEXcode Project
    # 	Author:       VEX
    # 	Created:
    # 	Description:  VEXcode IQ Python Project
    # 
    # ------------------------------------------

    # Library imports
from vex import *
import random
    # Begin project code
row_index = 5
column_index = 6
column_selected = 0
column = 0
piecetype = 0
roboPick = 2
grid = [
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ]
]

def gameBoard():
    brain.screen.draw_rectangle(0, 0, 15, 15)
    brain.screen.draw_rectangle(15, 0, 15, 15)
    brain.screen.draw_rectangle(30, 0, 15, 15)
    brain.screen.draw_rectangle(45, 0, 15, 15)
    brain.screen.draw_rectangle(60, 0, 15, 15)
    brain.screen.draw_rectangle(75, 0, 15, 15)
    brain.screen.draw_rectangle(90, 0, 15, 15)

    brain.screen.draw_rectangle(0, 15, 15, 15)
    brain.screen.draw_rectangle(0, 30, 15, 15)
    brain.screen.draw_rectangle(0, 45, 15, 15)
    brain.screen.draw_rectangle(0, 60, 15, 15)
    brain.screen.draw_rectangle(0, 75, 15, 15)

    brain.screen.draw_rectangle(15, 15, 15, 15)
    brain.screen.draw_rectangle(15, 30, 15, 15)
    brain.screen.draw_rectangle(15, 45, 15, 15)
    brain.screen.draw_rectangle(15, 60, 15, 15)
    brain.screen.draw_rectangle(15, 75, 15, 15)

    brain.screen.draw_rectangle(30, 15, 15, 15)
    brain.screen.draw_rectangle(30, 30, 15, 15)
    brain.screen.draw_rectangle(30, 45, 15, 15)
    brain.screen.draw_rectangle(30, 60, 15, 15)
    brain.screen.draw_rectangle(30, 75, 15, 15)

    brain.screen.draw_rectangle(45, 15, 15, 15)
    brain.screen.draw_rectangle(45, 30, 15, 15)
    brain.screen.draw_rectangle(45, 45, 15, 15)
    brain.screen.draw_rectangle(45, 60, 15, 15)
    brain.screen.draw_rectangle(45, 75, 15, 15)

    brain.screen.draw_rectangle(60, 15, 15, 15)
    brain.screen.draw_rectangle(60, 30, 15, 15)
    brain.screen.draw_rectangle(60, 45, 15, 15)
    brain.screen.draw_rectangle(60, 60, 15, 15)
    brain.screen.draw_rectangle(60, 75, 15, 15)

    brain.screen.draw_rectangle(75, 15, 15, 15)
    brain.screen.draw_rectangle(75, 30, 15, 15)
    brain.screen.draw_rectangle(75, 45, 15, 15)
    brain.screen.draw_rectangle(75, 60, 15, 15)
    brain.screen.draw_rectangle(75, 75, 15, 15)

    brain.screen.draw_rectangle(90, 15, 15, 15)
    brain.screen.draw_rectangle(90, 30, 15, 15)
    brain.screen.draw_rectangle(90, 45, 15, 15)
    brain.screen.draw_rectangle(90, 60, 15, 15)
    brain.screen.draw_rectangle(90, 75, 15, 15)

def update_grid():
    for i in range(5, -1, -1):
        print(i)
        print("  ")
        print(grid[1][column_selected])
        if grid[i][column_selected] == 0: #index out of range
                grid[i][column_selected] = piecetype
                break

#i is row, j is column 

def columnchoosing():
    global column, column_selected, piecetype
    tempcolumn = 0
    while not controller.buttonRDown.pressing():
        if controller.buttonLDown.pressing():
            brain.screen.clear_row(1)
            tempcolumn =  1
            brain.screen.set_cursor(1, tempcolumn)
            brain.screen.print("V")
            
        elif controller.buttonLUp.pressing():
            brain.screen.clear_row(1)
            tempcolumn = 2
            brain.screen.set_cursor(1, tempcolumn)
            brain.screen.print("V")
            
        elif controller.buttonEUp.pressing():
            brain.screen.clear_row(1)
            tempcolumn = 3
            brain.screen.set_cursor(1, tempcolumn)
            brain.screen.print("V")
            
        elif controller.buttonEDown.pressing():
            brain.screen.clear_row(1)
            tempcolumn = 4
            brain.screen.set_cursor(1, tempcolumn)
            brain.screen.print("V")

        elif controller.buttonFDown.pressing():
            brain.screen.clear_row(1)
            tempcolumn = 5
            brain.screen.set_cursor(1, tempcolumn)
            brain.screen.print("V")

        elif controller.buttonFUp.pressing():
            brain.screen.clear_row(1)
            tempcolumn = 6
            brain.screen.set_cursor(1, tempcolumn)
            brain.screen.print("V")

        elif controller.buttonRUp.pressing():
            brain.screen.clear_row(1)
            tempcolumn = 7
            brain.screen.set_cursor(1, tempcolumn)
            brain.screen.print("V")
        else:
            pass
        wait(100, MSEC)
    
    column_selected = tempcolumn - 1
    piecetype = 1   
    wait(20, MSEC)

# not supposed to check so many index, cuz that would cause the index to become out of range

def checkPlayerWinner(grid):    
    #horizontal
    for j in range(5):
        for i in range(0, 3):
            if grid[i][j] == 1 and grid[i+1][j] == 1 and grid[i+2][j] == 1 and grid[i+3][j] == 1:
                print("\nGame over", 1, "winner: player)")
                return True
    #vertical
    for i in range(6):
        for j in range(0, 2):
            if grid[i][j] == 1 and grid[i][j+1] == 1 and grid[i][j+2] == 1 and grid[i][j+3] == 1:
                print("\nGame over", 1, "winner:)")
                return True
    #positive diagonal
    for i in range(3):
        for j in range(3, 5):
            if grid[i][j] == 1 and grid[i+1][j-1] == 1 and grid[i+2][j-2] == 1 and grid[i+3][j-3] == 1:
                print("\nGame over", 1, "winner:)")
                return True
    #negativ diagonal
    for i in range(-3):
        for j in range(0, 2):
            if grid[i][j] == 1 and grid[i+1][j+1] == 1 and grid[i+2][j+2] == 1 and grid[i+3][j+3] == 1:
                print("\nGame over", 1, "winner)")
                return True
    return False
def checkRobotWinner(grid):    
    #horizontal
    for j in range(5):
        for i in range(0, 3):
            if grid[i][j] == 2 and grid[i+1][j] == 2 and grid[i+2][j] == 2 and grid[i+3][j] == 2:
                print("\nGame over", 2, "winner: player)")
                return True
    #vertical
    for i in range(6):
        for j in range(0, 2):
            if grid[i][j] == 2 and grid[i][j+1] == 2 and grid[i][j+2] == 2 and grid[i][j+3] == 2:
                print("\nGame over", 2, "winner:)")
                return True
    #positive diagonal
    for i in range(3):
        for j in range(3, 5):
            if grid[i][j] == 2 and grid[i+1][j-1] == 2 and grid[i+2][j-2] == 2 and grid[i+3][j-3] == 2:
                print("\nGame over", 2, "winner:)")
                return True
    #negativ diagonal
    for i in range(-3):
        for j in range(0, 2):
            if grid[i][j] == 2 and grid[i+1][j+1] == 2 and grid[i+2][j+2] == 2 and grid[i+3][j+3] == 2:
                print("\nGame over", 2, "winner)")
                return True
    return False

def isSpaceAvailable(intendedCoordinate):
  if(grid[intendedCoordinate[0]][intendedCoordinate[1]] == 1):
    return False
  elif(grid[intendedCoordinate[0]][intendedCoordinate[1]] == 2):
    return False
  else:
    return True

def pieceChecker(intendedCoordinate):                                   
  ### Calculate space below
  spaceBelow = [None] * 2
  spaceBelow[0] = intendedCoordinate[0] + 1
  spaceBelow[1] = intendedCoordinate[1]
  ### Is the coordinate at ground level
  if(spaceBelow[0] == 6):
    return True
  ### Check if there's a token below
  if(isSpaceAvailable(spaceBelow) == False):
    return True
  
  return False

def robotPickEasy():
    global piecetype, roboPick, column_selected
    column_selected = roboPick
    piecetype = 2

def robotPickMedium():
    global piecetype, roboPick, column_selected
    roboPick = random.randint(0, 6)
    column_selected = roboPick
    piecetype = 2

def robotPickHard():
    global piecetype, roboPick, column_selected
    #if console sees 3 ones in diagonal, veritcal, or horizontal, block it (smth like that, make it a function) 
    # also need it to be able to find a way to block it and avoid placing pieces???? wtf aint no way. 
    column_selected = roboPick
    piecetype = 2


def buttonLeft_pressed():
    #global selected_column
    brain.screen.clear_screen()
    brain.screen.set_cursor(4,10)
    brain.screen.print("Easy")
    wait(2,SECONDS)
    brain.screen.clear_screen()
    playEasy()

def buttonRight_pressed():
    brain.screen.clear_screen()
    brain.screen.set_cursor(4,10)
    brain.screen.print("Medium")
    wait(2,SECONDS)
    brain.screen.clear_screen()
    playMedium()

def buttonCheck_pressed():
    brain.screen.clear_screen()
    brain.screen.set_cursor(4,10)
    brain.screen.print("Hard")
    wait(2,SECONDS)
    brain.screen.clear_screen()
    playHardLmao()

def printScreen():
    brain.screen.clear_screen()
    for i in range(6):
        brain.screen.set_font(FontType.MONO15)
        for j in range(7):
            brain.screen.set_cursor(i+2,j+1)
            brain.screen.print((grid[i][j]))

def playEasy():
    while True:
        printScreen()
        columnchoosing()
        print("column selected")
        update_grid()
        print("grid updated")
        printScreen()
        wait(1,SECONDS)
        robotPickEasy()
        update_grid()
        printScreen()
        wait(.5,SECONDS)
        if checkPlayerWinner(grid) == True:
            break
        brain.screen.clear_screen()
        brain.screen.print("YOU WON")
        if checkRobotWinner(grid) == True:
            break
        brain.screen.clear_screen()
        brain.screen.print("robot won tsk")

def playMedium():
    while True:
        printScreen()
        columnchoosing()
        print("column selected")
        update_grid()
        print("grid updated")
        printScreen()
        wait(1,SECONDS)
        robotPickMedium()
        update_grid()
        printScreen()
        wait(.5,SECONDS)
        if checkPlayerWinner(grid) == True:
            break
        brain.screen.clear_screen()
        brain.screen.print("player winds")
        if checkRobotWinner(grid) == True:
            break
        brain.screen.clear_screen()
        brain.screen.print("robot wins?!")

def playHardLmao():
    while True:
        printScreen()
        columnchoosing()
        print("column selected")
        update_grid()
        print("grid updated")
        printScreen()
        wait(1,SECONDS)
        robotPickHard()
        update_grid()
        printScreen()
        wait(.5,SECONDS)
        if checkWinner(grid, piecetype) == True:
            break
    brain.screen.clear_screen()
    brain.screen.print("poop 3")

brain.screen.set_cursor(3,5)
brain.screen.print("connect 4")
wait(1, SECONDS)
brain.screen.clear_screen()
brain.screen.set_cursor(3, 2)
brain.screen.set_font(FontType.MONO15)
brain.screen.print("Select difficulty")
wait(1, SECONDS)
brain.screen.clear_screen()
brain.screen.set_cursor(2, 3)
brain.screen.print("Left = Easy")
brain.screen.set_cursor(4, 3)
brain.screen.print("Right = Medium")
brain.screen.set_cursor(6,3)
brain.screen.print("Check = Hard")

brain.buttonLeft.pressed(buttonLeft_pressed)
brain.buttonRight.pressed(buttonRight_pressed)
brain.buttonCheck.pressed(buttonCheck_pressed)


#brain.screen.clear_screen()
#brain.screen.draw_rectangle(8, 3, 145, 100)