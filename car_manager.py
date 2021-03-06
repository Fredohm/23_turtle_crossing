from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
STARTING_LOOP_COUNTER = 6


class CarManager:

    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.loop_counter = STARTING_LOOP_COUNTER
        self.cars = []
        self.add_car()

    def add_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.color(choice(COLORS))
            car.shapesize(stretch_len=2)
            car.penup()
            car.setheading(180)
            car.goto(300, randint(-250, 250))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
        if self.loop_counter > 0:
            self.loop_counter -= 1
