#region VEXcode Generated Robot Configuration
#from gc import callbacks
import random
import math
from vex import *

    # Brain should be defined by default
brain=Brain()

    # Robot configuration code
brain_inertial = Inertial()



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

def callback_function(): 
    print("button pressed")
def buttonLeft_pressed():
    brain.screen.clear_screen()
    brain.screen.set_cursor(4,10)
    brain.screen.print("Easy")
    wait(2,SECONDS)
    brain.screen.clear_screen()

possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
gameBoard = [["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""],
            ["","","","","","",""], ["","","","","","",""]]
rows=6
cols=7

def gameBoardEasy():
    print("\n    A   B   C   D   E   F   G  ", end="")
    for x in range(rows):
        print("  +---+---+---+---+---+---+---+")
        print(x, " |", end="")
        for y in range(cols):
            if(gameBoard [x][y] == "x"):
                print("", gameBoard[x][y], end=" | " )
            elif(gameBoard[x][y] == "o"):
                print("", gameBoard[x][y], end=" | ")
            else:
                print("", gameBoard[x][y], end=" | ")
        print("")

brain.screen.print(gameBoardEasy())


def buttonRight_pressed():
    brain.screen.clear_screen()
    brain.screen.set_cursor(4,10)
    brain.screen.print("Medium")
    wait(2,SECONDS)
    brain.screen.clear_screen()
def buttonCheck_pressed():
    brain.screen.clear_screen()
    brain.screen.set_cursor(4,10)
    brain.screen.print("Hard")
    wait(2,SECONDS)
    brain.screen.clear_screen()

brain.buttonLeft.pressed(buttonLeft_pressed)
brain.buttonRight.pressed(buttonRight_pressed)
brain.buttonCheck.pressed(buttonCheck_pressed)

wait(5, SECONDS)
#brain.screen.clear_screen()
#brain.screen.draw_rectangle(8, 3, 145, 100)



#possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
#gameBoard = [["","","","","","",""], ["","","","","","",""], ["","","","","","",""], ["","","","","","",""], 
#            ["","","","","","",""], ["","","","","","",""]]
#rows=6
#cols=7

#def printGameBoardTest():

#    brain.screen.set_font(FontType.MONO12)
 #   brain.screen.set_cursor(0,0)
  #  print("\n     A     B     C     D     E     F     G  ", end="")
   # for x in range(rows):
    #    print("\n     +-----+-----+-----+-----+-----+-----+-----+")
     #   print(x, " |", end="")
      #  for y in range(cols):
       #     if(gameBoard [x][y] == "x"):
        #        print("", gameBoard[x][y], end=" |" )
         #   elif(gameBoard[x][y] == "o"):
          #      print("", gameBoard[x][y], end=" |")
           # else:
            #    print(" ", gameBoard[x][y], end=" |")
        #print("\n     +-----+-----+-----+-----+-----+-----+-----")

#printGameBoardTest()


