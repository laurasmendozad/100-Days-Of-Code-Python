'''Scoreboard Class'''
from turtle import Turtle

ALIGNMENT = 'center'
FONT_SCORE = ('Courier', 80, 'normal')
FONT_GAME_OVER = ('Courier', 14, 'normal')

class Scoreboard(Turtle):
    '''Functions to control the food'''
    def __init__(self):
        super().__init__()
        self.left_score= 0
        self.right_score= 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        '''Update the Score Board'''
        self.goto(-100,200)
        self.write(f'{self.left_score}', align=ALIGNMENT, font=FONT_SCORE)
        self.goto(100,200)
        self.write(f'{self.right_score}', align=ALIGNMENT, font=FONT_SCORE)    

    def left_point(self):
        '''Increase the score to left'''
        self.clear()
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        '''Increase the score to right'''
        self.clear()
        self.right_score += 1
        self.update_scoreboard()
