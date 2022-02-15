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

screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
