""" Snake Class """
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
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
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        '''Add a segment to the snake'''
        new_segment = Turtle("square")
        new_segment.color("cyan")
        new_segment.penup()
        new_segment.goto(position)
        self.snake.append(new_segment)

    def move(self):
        '''Move the snake'''
        for s_num in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[s_num-1].xcor()
            new_y = self.snake[s_num-1].ycor()
            self.snake[s_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

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
        self.add_segment(self.snake[-1].position())
