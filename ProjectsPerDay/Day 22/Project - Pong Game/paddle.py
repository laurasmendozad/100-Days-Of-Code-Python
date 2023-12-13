""" Paddle Class """

from turtle import Turtle

class Paddle(Turtle):
    '''Functions to control paddle'''
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self,position):
        '''Create the paddle'''
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        '''Move the paddle up'''
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        '''Move the paddle down'''
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
