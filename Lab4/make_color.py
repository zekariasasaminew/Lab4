"""
Name(s): Sujay Zekarias
CSC 201
Lab 4--make_color.py

Enter red, green, and blue components to mix a color,
then fill the rectangle with that color

Did you complete this lab file during the class period (yes or no)?

If no, leave the one that applies. If yes, delete this entire section!
    
    I completed random_make_color.py with my partner from class.

    Document any assistance you get if you complete the lab after the class period:
    
"""
from graphics2 import *

def main():
    #create window and show directions
    window = GraphWin("What's the color?", 600, 600)
    window.setBackground('white')
    directions = Text(Point(300, 30), "Enter the amounts of red, green, and blue.")
    directions.draw(window)
    clickDirections = Text(Point(300, 60), "Click mouse when done.")
    clickDirections.draw(window)
    
    #draw the rectangle
    colorRect = Rectangle(Point(100, 250), Point(500, 550))
    colorRect.draw(window)
    
    #setup labels and entry boxes for input
    redLabel = Text(Point(100, 150), "red")
    blueLabel = Text(Point(470,150),'blue')
    greenLabel = Text(Point(270,150),'green')
    redLabel.draw(window)
    blueLabel.draw(window)
    greenLabel.draw(window)
    inputRed = Entry(Point(150, 150), 5)
    inputRed.setTextColor('red')
    inputRed.draw(window)
    inputGreen = Entry(Point(330, 150), 5)
    inputGreen.setTextColor('blue')
    inputGreen.draw(window)
    inputBlue = Entry(Point(520, 150), 5)
    inputBlue.setTextColor('red')
    inputBlue.draw(window)
    
    


    
    
    #get numbers from entry boxes to mix the color
    window.getMouse()
    red = int(inputRed.getText())
    green = int(inputGreen.getText())
    blue = int(inputBlue.getText())
    
    
    
    # make color from red, green, blue numbers
   
    color = color_rgb(red, green, blue)
    
    
    
    # add the color to the rectangle that is already drawn
    colorRect.setFill(color)




    
main()