""" Car Manager Class """

from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    '''Functions to control car'''
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        '''Create the car'''
        if random.randint(1,6) == 1:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(300,random.randint(-250, 250))
            self.all_cars.append(car)

    def move_car(self):
        '''Move the car'''
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        '''Set the speed every level up'''
        self.car_speed += MOVE_INCREMENT
