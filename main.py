import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle crossing")
screen.tracer(0)

screen.listen()

scoreboard = Scoreboard()
player = Player(STARTING_POSITION)
car_manager = CarManager()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    car_manager.add_car()

    car_manager.move()

    # detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            player.hideturtle()
            game_is_on = False
            scoreboard.game_over()

    # detect successful crossing
    if player.is_at_finish_line():
        player.go_to_starting_position()
        car_manager.increase_speed()
        scoreboard.increase_level()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
