import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.make_car()
    cars.drive()
    for car in cars.all_cars:
        if car.distance(player) < 30:
            scoreboard.game_over()
            game_is_on = False
    screen.update()
    if player.ycor() > 280:
        cars.faster()
        player.restart()
        scoreboard.update_score()

screen.exitonclick()
