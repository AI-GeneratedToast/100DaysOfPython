from turtle import Turtle


class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def add_score1(self):
        self.score1 += 1

    def add_score2(self):
        self.score2 += 1

    def update_scoreboard(self):
        self.write(f"{self.score2} : {self.score2}", move=False, align='center', font=('Arial', 24, 'normal'))