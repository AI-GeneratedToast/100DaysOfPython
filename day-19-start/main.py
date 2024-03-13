import random
import turtle
from turtle import Turtle, Screen
new_turtle = Turtle()
screen = Screen()
"""""
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
    
    
screen.listen()
screen.onkey(key="space",fun=move_forward)
screen.exitonclick()

"""""

"""""
def forwards():
    tim.forward(10)


def backwards():
    tim.forward(-10)


def clockwise():
    tim.left(45)


def counter_clockwise():
    tim.right(45)


def clear():
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear)
"""""

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -175
x = -230
all_turtles = []

for i in range(len(colors)):
    new_turtle.color(colors[i])
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    y += 50
    new_turtle.goto(x, y)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
