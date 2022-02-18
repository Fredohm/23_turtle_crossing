from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.speed("fastest")
        self.color("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.penup()
        self.goto(-280, 260)
        self.pendown()
        self.increase_score()
        self.write(f"Level: {self.score}", font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
