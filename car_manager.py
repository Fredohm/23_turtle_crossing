from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(COLORS[randint(0, 5)])
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.hideturtle()
        self.setheading(180)
        self.goto(300, randint(-280, 280))
        self.showturtle()

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
        print(self.position())
