from turtle import Turtle, Screen, colormode
from random import randint, choice

# ## Challenge 1 - Draw a Square
# c1 = Turtle()

# for i in range(4):
#     c1.right(90)
#     c1.forward(100)

# ## Challenge 2 - Draw a Dashed Line
# c2 = Turtle()

# for i in range(20):
#     c2.forward(10)
#     c2.penup()
#     c2.forward(10)
#     c2.pendown()

# ## Challenge 3 - Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
# def set_random_color(t):
#     R = randint(0,255)
#     G = randint(0,255)
#     B = randint(0,255)
#     t.color((R,G,B))

# c3 = Turtle()

# colormode(255)

# for i in range(3,11):
#     set_random_color(c3)

#     lon = 100
#     angle = 360/i
#     for _ in range(i):
#         c3.right(angle)
#         c3.forward(lon)

# ## Challenge 4 - Draw a Random Walk
# def set_random_color(t):
#     colormode(255)
#     R = randint(0,255)
#     G = randint(0,255)
#     B = randint(0,255)
#     t.color((R,G,B))

# def random_move(t,lon):
#     direction = [0,90,180,270]
#     angle = choice(direction)
#     t.setheading(angle)
#     t.forward(lon)

# c4 = Turtle()
# c4.pensize(10)
# c4.speed("normal")

# for _ in range(200):
#     set_random_color(c4)
#     random_move(c4,20)

# ## Challenge 5 - Make a Spirograph
# def set_random_color(t):
#     colormode(255)
#     R = randint(0,255)
#     G = randint(0,255)
#     B = randint(0,255)
#     t.color((R,G,B))

# c5 = Turtle()
# c5.speed("fastest")
# size_of_gap = 10

# for i in range(0,361,size_of_gap):
#     set_random_color(c5)
#     radius = 100
#     c5.circle(radius)
#     c5.setheading(i)

screen = Screen()
screen.exitonclick()
