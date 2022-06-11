import colorgram
from turtle import Turtle, Screen, colormode
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     rgb_colors.append(rgb_color)
#
# print(rgb_colors)
color_list = [(124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83),
              (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
              (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
              (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190),
              (40, 72, 82), (46, 73, 62), (47, 66, 82)]

screen = Screen()
colormode(255)

tim = Turtle()
tim.speed(1)
tim.pu()
y = -250.00
tim.setpos(-250.00, y)

for dot_y in range(10):
    for dot_x in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    y += 50.00
    tim.setpos(-250.00, y)

screen.exitonclick()

