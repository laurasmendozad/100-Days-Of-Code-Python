
'''The Turtle Crossing Capstone'''
import os
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

os.system('cls')

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('The Turtle Crossing Game')
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

GAME_ON = True
while GAME_ON:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision to the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            GAME_ON = False
            scoreboard.game_over()

    # Detect successful crossing
    if player.finish_line():
        player.go_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
