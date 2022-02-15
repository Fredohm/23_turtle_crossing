from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    STARTING_POSITION = None

    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.hideturtle()
        self.goto(0, -260)
        self.setheading(90)
        self.showturtle()
        self.goto(position)

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
