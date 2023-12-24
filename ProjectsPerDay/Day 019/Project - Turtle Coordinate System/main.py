'''Turtle Coordinate System'''

from turtle import Turtle, Screen
import random
import os

os.system('cls')

RACE_ON = False
colors = ['red','orange','yellow','green','blue','purple']
WS = 500     # Width of the screen
HS = 400     # Height of the screen
ST = 40      # Size of the turtle

screen = Screen()
screen.setup(width=WS, height=HS)
user_bet = screen.textinput(title='Make Your Bet',
                            prompt='Which turtle will win the race? Enter the color: ')

while user_bet.lower() not in colors:
    user_bet = screen.textinput(title="Make Your Bet",
                                prompt="The color don't exist. Try again. Enter the color: ")
RACE_ON = True

all_turtles = []
for i, _ in enumerate(colors):
    turtle = Turtle(shape='turtle')
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x = -WS/2 + ST/2, y = -HS/4 + ST*i)
    all_turtles.append(turtle)

while RACE_ON:
    for turtle in all_turtles:
        turtle.forward(random.randint(0,10))  
        if turtle.position()[0] > (WS/2 - ST/2):
            RACE_ON = False
            win_turtle_color = turtle.pencolor()
            if win_turtle_color == user_bet:
                print(f"You've won! The {win_turtle_color} turtle is the winner!")
            else:
                print(f"You've lose! The {win_turtle_color} turtle is the winner!")

screen.exitonclick()
