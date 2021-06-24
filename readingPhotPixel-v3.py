#reading photo pixel v3

'''
================================
Reading photo pixel
created by: Yuliya Vaskiv
Date: 06/23/2021
..................................

This app opens the picture on user preference.
The picture pops out in seperate window
and app runs through each pixel,
checking the color and tranfer them into turtle.
The turtle takes the color and draws
square with represented color.
The square are drawn next to each other creating the
actual picture, that might be pixalated.

The user can change how pixalated picture can be.
1 give the most accurate image.

The app transfer image into turtle.

==========================================================

Notes:
This app can be modified in a way
that on turtle picture can be centered
06/23/2021
'''

from cImage import *
import turtle

t = turtle.Turtle()
t.speed(0.001)

#main() variable
def openImage(fileName, size, density):

    origImage = FileImage(fileName)#finds particular file

    #dimesnsions for picture
    width = origImage.getWidth()
    height = origImage.getHeight()

    #opens the actual window with picture
    myWin = ImageWin("readingPixels", width + 10, height + 10)
    origImage.draw(myWin)


    #variables 
    k = 0
    listColors = []
    
    verNum = 200 #x and y start point
    horNum = -200


    #looks through every pixel on photo
    for row in range(0, height, density):
        #fix x and y coordinates for turtle
        verNum = verNum - size
        k = horNum
        
        for col in range(0, width, density):
            origPixel = origImage.getPixel(col, row) #take RGB number
            #calls variable that change RGB for turtle use
            #and the sqaure is drawn that represent pixel
            listPixel = countPixels(origPixel, listColors, verNum, k, size)

            #x coordinate change
            k = k + size

    #exits window with image
    myWin.exitOnClick()

    
def countPixels(pix, lis, x, y, size):

    #change RGB values to be used in turtle
    color = []
    maxColor = 255
    rounding2 = 1
    red = round(pix.getRed() / maxColor, rounding2)
    green = round(pix.getGreen() / maxColor, rounding2)
    blue = round(pix.getBlue() / maxColor, rounding2)

    
    #draws actual sqaures with inscribes color from above
    t.up()
    t.goto(y, x)
    t. down()
    
    t.color(red, green, blue)
    t.fillcolor(red, green, blue)
    t.begin_fill()
    
    for i in range(4):
        t.forward(size)
        t.right(90)

    t.end_fill()


    #puts color into the list
    #! can not be used for t.color from the list
    nPix = Pixel(red, green, blue)
    lis.append(nPix)
    
    return lis


'''=========================================================='''
size = 10
density = 20
name = "AliceInJar.gif"
openImage(name, size, density)
