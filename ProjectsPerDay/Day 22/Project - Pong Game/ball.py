""" Ball Class """

from turtle import Turtle

class Ball(Turtle):
    '''Functions to control paddle'''
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.speed_movement = 0.1

    def create_ball(self):
        '''Create the paddle'''
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        '''Move the ball'''
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        '''Bounce the ball'''
        self.y_move *= -1
        self.speed_movement *= 0.9

    def bounce_x(self):
        '''Bounce the ball'''
        self.x_move *= -1

    def reset_ball(self):
        '''Reset the position and the movement of the ball'''
        self.goto(0,0)
        self.bounce_x()
        self.speed_movement = 0.1
