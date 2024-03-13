import random
import turtle
from turtle import Turtle, Screen

"""""
from turtle import Turtle, Screen

tim= Turtle()
tim.shape("turtle")
tim.color("red")

tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(100)
                          
screen = Screen()         
screen.exitonclick()      

"""""

#import turtle as t

#tim = t.Turtle()

#import heroes
#print(heroes.gen())


"""""
tim = Turtle()
tim.shape("turtle")
tim.color("red")


for i in range(3):
    tim.down()
    tim.forward(100)
    tim.penup()
    tim.forward(100)

"""""
"""""
tim = Turtle()
tim.shape("arrow")

#Triangle
tim.color("red")
for i in range(3):
    tim.forward(100)
    tim.right(120)

#Square
tim.color("black")
for i in range(4):
    tim.forward(100)
    tim.right(90)
#Pentagon
tim.color("blue")
for i in range(5):
    tim.forward(100)
    tim.right(72)
#Hexagon
for i in range(6):
    tim.color("green")
    tim.forward(100)
    tim.right(60)
#Heptagon
for i in range(7):
    tim.color("pink")
    tim.forward(100)
    tim.right(51.43)
#Octagon
for i in range(8):
    tim.color("purple")
    tim.forward(100)
    tim.right(45)
# nonagon
for i in range(9):
    tim.color("lime")
    tim.forward(100)
    tim.right(40)
#Decagon
for i in range(10):
    tim.color("yellow")
    tim.forward(100)
    tim.right(36)
"""""

"""""
from random import Random
distance = random.randint(0, 100)
move = random.randint(0, 360)
tim = Turtle()
tim.shape("arrow")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_tuple = (r,g,b)
    return rgb_tuple

directions=[0,90,180,270]
tim.pensize(15)
tim.speed("fastest")

for i in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
"""""

"""""
from random import Random

tim = Turtle()
tim.shape("arrow")
tim.speed("fastest")
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_tuple = (r, g, b)
    return rgb_tuple

for i in range(360):
    tim.circle(100)
    tim.right(5)
    tim.color(random_color())
"""""




screen = Screen()
screen.exitonclick()



