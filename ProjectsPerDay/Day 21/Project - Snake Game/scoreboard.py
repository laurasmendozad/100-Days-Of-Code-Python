'''Scoreboard Class'''
from turtle import Turtle

ALIGNMENT = 'center'
FONT_SCORE = ('Arial', 12, 'normal')
FONT_GAME_OVER = ('Arial', 14, 'normal')

class Scoreboard(Turtle):
    '''Functions to control the food'''
    def __init__(self):
        super().__init__()
        self.score= 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        '''Update the Score Board'''
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT_SCORE)

    def increase_score(self):
        '''Increase the Score and Update'''
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        '''Print Game Over'''
        self.goto(0,0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT_GAME_OVER)
