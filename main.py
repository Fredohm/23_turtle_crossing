import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)

screen.listen()

player = Player(STARTING_POSITION)
car_manager = CarManager()

screen.onkey(player.move, "Up")

loop_counter = 0
game_is_on = True
while game_is_on:
    if loop_counter == 0:
        car_manager.add_car()

    loop_counter += 1
    if loop_counter > 6:
        loop_counter = 0

    car_manager.move()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
