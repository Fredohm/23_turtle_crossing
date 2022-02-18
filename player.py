from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.hideturtle()
        self.go_to_starting_position()
        self.setheading(90)
        self.showturtle()
        self.goto(position)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def go_to_starting_position(self):
        self.goto(STARTING_POSITION)
