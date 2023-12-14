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
        with open("data.txt", encoding="utf-8") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,270)
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", encoding="utf-8", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        '''Update the Score Board'''
        self.clear()
        self.write(f'Score: {self.score} - High Score: {self.high_score}',
                    align=ALIGNMENT, font=FONT_SCORE)

    def increase_score(self):
        '''Increase the Score and Update'''
        self.score += 1
        self.update_scoreboard()
