'''
'Author: Joseph Loporto
Please comment any adjustments here as this is a critical file

Usage: This script prints the first argument given to it by command line into a turtle window and additionally contains
turtlePRINT function and turtleSETUP()
'''

import turtle
import joeyL,ryanBilash,alexYou,shaunG
import sys




def turtlePRINT(inputStr):
    assert isinstance(inputStr, str), "Non-String Input"

    def turtleNEXTLINE():
        turtle.penup()
        turtle.setpos(-630, turtle.ycor() - 60)
        turtle.pendown()

    STR = inputStr.upper()
    for index, CHAR in enumerate(STR):
        turtleNEXTLINE() if turtle.xcor() >= 600 else 1

        ryanBilash.turtleA() if CHAR == "A" else 1
        ryanBilash.turtleB() if CHAR == "B" else 1
        ryanBilash.turtleC() if CHAR == "C" else 1
        ryanBilash.turtleD() if CHAR == "D" else 1
        ryanBilash.turtleE() if CHAR == "E" else 1
        ryanBilash.turtleF() if CHAR == "F" else 1
        ryanBilash.turtleG() if CHAR == "G" else 1
        ryanBilash.turtleH() if CHAR == "H" else 1
        ryanBilash.turtleI() if CHAR == "I" else 1
        ryanBilash.turtleJ() if CHAR == "J" else 1

        alexYou.turtleK() if CHAR == "K" else 1
        alexYou.turtleL() if CHAR == "L" else 1
        alexYou.turtleM() if CHAR == "M" else 1
        alexYou.turtleN() if CHAR == "N" else 1
        alexYou.turtleO() if CHAR == "O" else 1
        alexYou.turtleP() if CHAR == "P" else 1
        alexYou.turtleQ() if CHAR == "Q" else 1
        alexYou.turtleR() if CHAR == "R" else 1
        alexYou.turtleS() if CHAR == "S" else 1
        alexYou.turtleT() if CHAR == "T" else 1
        alexYou.turtleU() if CHAR == "U" else 1
        alexYou.turtleV() if CHAR == "V" else 1
        alexYou.turtleW() if CHAR == "W" else 1
        alexYou.turtleX() if CHAR == "X" else 1

        joeyL.turtleY() if CHAR == "Y" else 1
        joeyL.turtleZ() if CHAR == "Z" else 1
        joeyL.turtleSPACE() if CHAR == " " else 1
        joeyL.turtleDIAMOND() if CHAR == "*" else 1
        joeyL.turtleSELFBOX() if CHAR == "#" else 1
        joeyL.turtleSMILE() if CHAR == "!" else 1
        joeyL.turtleFROWN() if CHAR == "@" else 1
        #TODO Add Seans's numbers and file

        shaunG.turtle0() if CHAR == "0" else 1
        shaunG.turtle1() if CHAR == "1" else 1
        shaunG.turtle2() if CHAR == "2" else 1
        shaunG.turtle3() if CHAR == "3" else 1
        shaunG.turtle4() if CHAR == "4" else 1
        shaunG.turtle5() if CHAR == "5" else 1
        shaunG.turtle6() if CHAR == "6" else 1
        shaunG.turtle7() if CHAR == "7" else 1
        shaunG.turtle8() if CHAR == "8" else 1
        shaunG.turtle9() if CHAR == "9" else 1



def turtleSETUP(speed = 100):
    assert isinstance(speed,int)
    turtle.setup(1280, 720, 0, 0)
    turtle.reset()
    turtle.penup()
    turtle.speed(speed)
    turtle.setpos(-630, 300) #Start in upper left, 10px by 10px margin
    turtle.pendown()

if __name__ == '__main__':
    turtleSETUP()

    if len(sys.argv) >= 2:
        turtlePRINT(sys.argv[1])
    else:
        turtlePRINT(input('Please input string to turtle-print:'))

    turtle.mainloop()




