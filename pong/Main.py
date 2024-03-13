from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")

paddle1 = Paddle()
paddle1.goto(-240, 0)
screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")

paddle2 = Paddle()
paddle2.goto(240, 0)
screen.listen()
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle2) < 50 and ball.xcor() > 340 or ball.distance(paddle1) < 50 and ball.xcor() < -340:
        ball.bounce_x()

screen.exitonclick()


