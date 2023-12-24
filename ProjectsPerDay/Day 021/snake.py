""" Snake Class """
from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    '''Functions to control snake'''
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        '''Create the snake'''
        for i in range(3):
            square = Turtle(shape='square')
            square.color('cyan')
            square.penup()
            square.goto(x = -20*i, y = 0)
            self.snake.append(square)

    def move(self):
        '''Move the snake'''
        for s_num in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[s_num-1].xcor()
            new_y = self.snake[s_num-1].ycor()
            self.snake[s_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
        # self.snake[0].left(90)

    def up(self):
        '''Move the snake up'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        '''Move the snake dowm'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        '''Move the snake left'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        '''Move the snake right'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        '''Extend snake size'''
        
