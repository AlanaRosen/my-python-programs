Turtle Race Using the For Loop:

import turtle
import random
wn = turtle.Screen()
wn.bgcolor("gray")

alli = turtle.Turtle()
jax = turtle.Turtle()
alli.shape("turtle")
alli.pen(pencolor = "hot pink", pensize = 9)
jax.shape("turtle")
jax.pen(pencolor = "magenta", pensize = 9)

alli.up()
alli.goto(-100,50)
alli.down()

jax.up()
jax.goto(-100,-50)
jax.down()

for x in [alli,jax]:
    x.forward(random.randrange(1,250))
    x.speed(random.randrange(1,11))

wn.exitonclick()








Turtle Race Using Simple Forward Command:

import turtle              
import random
wn = turtle.Screen()       
wn.bgcolor('lightblue')

lance = turtle.Turtle()    
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()                 
lance.up()
andy.goto(-100,20)
lance.goto(-100,-20)

speed_a = random.randrange(1,11)
speed_l = random.randrange(1,11)
distance_a = random.randrange(1,250)
distance_l = random.randrange(1,250)

andy.down()
lance.down()
andy.speed(speed_a)
andy.forward(distance_a)
lance.speed(speed_l)
lance.forward(distance_l)

wn.exitonclick()

