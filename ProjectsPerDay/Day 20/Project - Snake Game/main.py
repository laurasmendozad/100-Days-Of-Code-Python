'''Snake Game'''

import time
import os
from turtle import Screen
from snake import Snake

os.system('cls')

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

GAME_ON = True

while GAME_ON:
    screen.update()
    time.sleep(0.1)   
    snake.move()

screen.exitonclick()
