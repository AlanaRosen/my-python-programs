import turtle                               #import necessary module

wn = turtle.Screen()                        #set up screen on which to run your turtles
wn.bgcolor("gray")                       #set up the aesthetics of your window

jess = turtle.Turtle()                      #name your turtles
tray = turtle.Turtle()
jess.shape("classic")                       #define your turtles' line shapes
tray.shape("classic")
jess.pensize(2)                             #define how thick your lines will be
tray.pensize(2)

def draw_circle(t):                         #define a function to draw the circle with the equidistant lines inside
    tray.up()                               #make sure tray doesn't make any marks
    tray.goto(0,-100)                       #send tray to his starting destination
    tray.down()                             #allow tray to draw again
    tray.circle(100)                        #tell tray you want him to make a circle with a radius of 100
    tray.goto(0,0)                          #send tray back to the center of the circle, drawing your first inside line
    for x in range(20):                     #there are 20 lines needed inside the circle
        tray.forward(100)                   #send tray forward to draw the line
        tray.forward(-100)                  #send tray back to the center
        tray.left(18)                       #rotate tray (360 degrees divided by 20)
        
draw_circle(tray)                           #execute tray's circle program


def rotate_squares(t):
    jess.

def draw_square(x):                        #define a function for drawing five squares, each one 72 degrees left of the previous one
    for x in range (4):
        jess.forward(200)                   
        jess.left(90)

jess.up()
jess.goto(-100,-100)
jess.down()
draw_square(jess)
rotate_squares(jess)
draw_square(jess)

    






draw_square(jess)

wn.exitonclick() 