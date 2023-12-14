'''Scoreboard Class'''
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    '''Functions to control the food'''
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        '''Update the Score Board'''
        self.goto(-290,260)
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def increase_level(self):
        '''Increase the level number'''
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        '''Print Game Over'''
        self.goto(0,0)
        self.write("Game Over", align='center', font=FONT)
