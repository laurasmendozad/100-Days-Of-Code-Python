''' Final Project - Higher or Lower URLs '''
from random import randint
from flask import Flask

app = Flask(__name__)
number = randint(0,9)
print(number)

@app.route('/')
def home():
    ''' Home Page '''
    return '<h1>Guess a number between 0 and 9</h1>' \
        '<img src="https://media.giphy.com/media/IsfrRWvbUdRny/giphy.gif">'

@app.route('/<int:num>')
def game(num):
    ''' Logic of the game '''
    if num == number:
        return '<h1 style="color: green;">You found me!</h1>' \
            '<img src="https://media.giphy.com/media/nDSlfqf0gn5g4/giphy.gif">'
    if num < number:
        return '<h1 style="color: blue;">Too low, try again</h1>' \
            '<img src="https://media.giphy.com/media/tvU9iTev6uBIQ/giphy.gif">'
    if num > number:
        return '<h1 style="color: red;">Too high, try again</h1>' \
            '<img src="https://media.giphy.com/media/qcR6H0Xp5EF3E8r7lw/giphy.gif">'

if __name__=="__main__":
    app.run(debug=True)
