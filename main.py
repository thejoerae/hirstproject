# import colorgram
#
# colors = colorgram.extract("image.jpg", 2 ** 32)
# color_palette = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_palette.append(new_color)
#
# print(color_palette)
from turtle import Turtle, Screen, colormode
import random

color_list = [(1, 12, 31), (53, 25, 17), (218, 127, 106), (10, 104, 159), (242, 213, 68), (149, 83, 39), (215, 87, 63), (155, 6, 24), (165, 162, 31), (157, 62, 102), (10, 64, 33), (206, 74, 104), (11, 96, 57), (95, 6, 20), (174, 135, 163), (1, 61, 145), (7, 172, 216), (3, 213, 207), (159, 33, 24), (8, 140, 85), (145, 227, 217), (122, 193, 147), (220, 177, 216), (100, 218, 229), (117, 171, 192), (79, 135, 178), (252, 197, 0), (29, 84, 92), (228, 174, 166), (186, 190, 201), (73, 73, 39)]

timmy = Turtle()
colormode(255)
timmy.penup()

timmy.setposition(-300, -300)
x = -300
y = -300

for move in range(10):
    for _ in range(10):
        timmy.setposition(x, y)
        timmy.dot(20, (random.choice(color_list)))
        x += 50
    x = -300
    y += 50

timmy.hideturtle()
screen = Screen()
screen.exitonclick()