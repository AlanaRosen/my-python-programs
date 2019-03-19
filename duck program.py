import turtle
wn = turtle.Screen()
wn.bgcolor("gray")

tray = turtle.Turtle()
tray.shape("classic")

def draw_circle(t):
    tray.up()
    tray.goto(0,-100)
    tray.down()
    tray.circle(100)
    tray.goto(0,0)
    for x in range(20):
        tray.forward(100)
        tray.forward(-100)
        tray.left(18)
        
draw_circle(tray)

jess = turtle.Turtle()
jess.shape("classic")
jess.pensize(2)

turtle.register_shape("square", ((-100,-100),(100,-100),(100,100),(-100,100)))
jess.shape("square")
jess.fillcolor("")

for x in range(5):
    jess.left(36)
    jess.stamp()

wn.exitonclick()
    