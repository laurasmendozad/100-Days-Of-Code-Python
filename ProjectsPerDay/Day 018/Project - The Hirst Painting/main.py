from turtle import Turtle, Screen, colormode,setworldcoordinates
from random import choice
import colorgram as c

number_of_colors = 7
colors = c.extract("image.png", number_of_colors)
colors_rgb = []

for c in range(1,number_of_colors):
    colors_rgb.append(tuple(colors[c].rgb))

d = Turtle()
colormode(255)
d.speed("fastest")
d.penup()
d.hideturtle()

size_dot = 20
distance = 50
dimention = 10

d.setheading(225)
d.forward((dimention/2)*distance)
d.setheading(0)

for i in range(0,dimention):
    for j in range(0,dimention):
        d.dot(size_dot,choice(colors_rgb))
        d.forward(distance)
    d.left(90)
    d.forward(distance)
    d.left(90)
    d.forward(distance*dimention)
    d.right(180)

# spot_painting(dot,size_dot,distance,dimention)

screen = Screen()
screen.exitonclick()