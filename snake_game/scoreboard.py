from turtle import Turtle


class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = (self.read_high_score())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def read_high_score(self):
        with open("data.txt") as file:
            self.high_score = file.read()
            return self.high_score

    def write_high_score(self):
        with open("data.txt", mode="w") as file:
            my_score = str(self.score)
            file.write(my_score)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   move=False, align="center", font=('Arial', 24, 'normal'))

    def reset(self):
        if str(self.score) > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()

    """""
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Arial', 24, 'normal'))
    """""

    def add_score(self):
        self.score += 1
        self.update_scoreboard()
