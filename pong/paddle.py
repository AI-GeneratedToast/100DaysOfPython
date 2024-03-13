from turtle import Turtle


class Paddle (Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1, 4)
        self.setheading(90)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)


