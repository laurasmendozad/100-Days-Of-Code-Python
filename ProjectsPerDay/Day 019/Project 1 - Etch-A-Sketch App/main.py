'''Etch-A-Sketch App'''

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    '''Move forward 10 steps'''
    tim.forward(10)

def move_backward():
    '''Move backward 10 steps'''
    tim.backward(10)

def turn_rigth():
    '''Turn right or clockwise 10 degrees'''
    tim.right(10)

def turn_left():
    '''Turn left or counter-clockwise 10 degrees'''
    tim.left(10)

def clear():
    '''Clear the screen and reset turtle'''
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_rigth)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
