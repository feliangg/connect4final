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
    # Begin project code
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


def update_column(grid, column_selected=3, piecetype=1):
    for i in range(5, -1, -1):
        if grid[i][column_selected] == 0:
            grid[i][column_selected] = piecetype
            break

def controllercontrol():
    global selected_column
    if controller.axisC.position() > 5:
        selected_column = selected_column =+ 1
        brain.screen.clear_row(1)
        brain.screen.set_cursor(1,selected_column)
        brain.screen.print("V")
    elif controller.axisC.position() < -5:
        selected_column = selected_column =- 1
        brain.screen.clear_row(1)
        brain.screen.set_cursor(1,selected_column)
        brain.screen.print("V")


def threethings(value):
    if (value == 0):
        return ("_")
    elif (value == 1):
        return ("o")
    elif (value == 2):
        return ("x")
    
def isSpaceAvailable(intendedCoordinate):
  if(grid[intendedCoordinate[0]][intendedCoordinate[1]] == "o"):
    return False
  elif(grid[intendedCoordinate[0]][intendedCoordinate[1]] == "x"):
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

   
#def robotPickEasy():
   

selected_column = 1

grid = [
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ],
    [0 ,0 ,0 ,0 ,0 ,0 ,0 ]
]

new_value = 2

def callback_function(): 
    print("button pressed")

def buttonLeft_pressed():
    brain.screen.clear_screen()
    brain.screen.set_cursor(4,10)
    brain.screen.print("Easy")
    wait(2,SECONDS)
    brain.screen.clear_screen()
    for i in range(6):
        brain.screen.set_font(FontType.MONO15)
        for j in range(7):
            brain.screen.set_cursor(i+2,j+5)
            brain.screen.print((grid[i][j]))
    brain.screen.set_cursor(1,selected_column)
    brain.screen.print("V")
    column_index = controllercontrol()
    update_column(grid, column_selected=column_index, piecetype=new_value)

def buttonRight_pressed():
    brain.screen.clear_screen()
    brain.screen.set_cursor(4,10)
    brain.screen.print("Medium")
    wait(2,SECONDS)
    brain.screen.clear_screen()
    gameBoard()

def buttonCheck_pressed():
    brain.screen.clear_screen()
    brain.screen.set_cursor(4,10)
    brain.screen.print("Hard")
    wait(2,SECONDS)
    brain.screen.clear_screen()
    gameBoard()
    
brain.buttonLeft.pressed(buttonLeft_pressed)
brain.buttonRight.pressed(buttonRight_pressed)
brain.buttonCheck.pressed(buttonCheck_pressed)
wait(5, SECONDS)

while True:
    controllercontrol()

#brain.screen.clear_screen()
#brain.screen.draw_rectangle(8, 3, 145, 100)