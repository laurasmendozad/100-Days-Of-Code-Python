""" Player Class """

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    '''Functions to control player'''
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_start()
        self.setheading(90)
        self.color('white')

    def go_start(self):
        '''Move the player to the starting position'''
        self.goto(STARTING_POSITION)

    def go_up(self):
        '''Move the player up'''
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def finish_line(self):
        '''Detect if the turtle is at finish line'''
        if self.ycor() > FINISH_LINE_Y:
            return True
