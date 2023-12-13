'''Pong Game'''
import os
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

os.system('cls')

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()

GAME_ON = True
while GAME_ON:
    time.sleep(ball.speed_movement)
    screen.update()
    ball.move()

    # Detect collision to the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision to the paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.left_point()

    # Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.right_point()

screen.exitonclick()
