"""
Name(s):Sujay Zekarias
CSC 201
Lab 4--donut_shop.py

When completed, the user will click in the window 3 times
to draw 3 donuts (with sprinkles if you got to the bonus!).

Did you complete this lab file during the class period (yes or no)?

If no, leave the one that applies. If yes, delete this entire section!
    
    I completed donut_shop.py with my partner from class.

    Document any assistance you get if you complete the lab after the class period:
    
"""

from graphics2 import *
import random
import math

COLOR_LIST = ['red','blue','lime','black', 'magenta', 'darkviolet', 'deeppink3', 'dodgerblue1', 'firebrick2']
NUM_SPRINKLES = 150
SPRINKLE_RADIUS = 3
HOLE_RATIO = 1/3

def drawOneDonut(window, glazeColor, backgroundColor, radius, center):
    """
    The function draws one donut with color, size, and placement given by the parameters.
    
    Parameters:
    window (GraphWin): the window to draw the donut in
    glazeColor (str): a string for the color of the donut
    backgroundColor (str): a string for the color of the background used to draw the hole
    radius (int): the outer radius of the donut
    center (Point): the center point of the donut
    """
    pass
        
    x = center.getX()
    y = center.getY()
    mainCircle = Circle(Point(x,y),radius)
    mainCircle.setFill(glazeColor)
    mainCircle.draw(window)
    mainCircle.setOutline(backgroundColor)
    smallCircle = Circle(Point(x,y),(HOLE_RATIO*radius))
    smallCircle.setFill(backgroundColor)
    smallCircle.draw(window)
    smallCircle.setOutline(backgroundColor)


def drawSprinkles(window, donut):
    """
    The function draws sprinkles(circles) with a randomly chosen color and position
    so that all are draw on the donut's surface.
    
    Parameters:
    window (GraphWin): the window to draw the sprinkles in
    donut (Circle): the large circle making the donut
    """
    pass

        



def main():
    # create window
    window = GraphWin("Donut Shop", 500, 500)
    backgroundColor = 'cyan'
    window.setBackground(backgroundColor)
    headingText = Text(Point(250, 50), 'Click three times to get your donuts!')
    headingText.draw(window)
    
    
    center = window.getMouse()
    # draw donuts in window
    drawOneDonut(window, 'pink', backgroundColor ,100, center)
    center = window.getMouse()
    drawOneDonut(window, 'brown', backgroundColor ,85, center)
    center = window.getMouse()
    drawOneDonut(window, 'yellow', backgroundColor ,75, center)
    

main()