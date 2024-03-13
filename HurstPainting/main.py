"""""
from colorgram import colorgram

rgb_colors=[]
colors = colorgram.extract('image.jpg', 30)

for colors in colors:
    r = colors.rgb.r
    g = colors.rgb.g
    b = colors.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)
"""""
import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)

color_list = [(176, 155, 18), (31, 112, 165), (150, 55, 123),
 (191, 7, 36), (24, 132, 123), (18, 91, 50), (213, 183, 62), (223, 206, 97), (118, 170, 196), (16, 70, 40),
 (34, 155, 195), (199, 135, 164), (129, 177, 165), (41, 58, 114), (183, 92, 122), (76, 153, 146), (235, 166, 186),
 (231, 200, 16), (158, 210, 201), (104, 119, 165), (147, 210, 224), (125, 134, 29), (176, 186, 218), (29, 45, 89),
 (10, 109, 111), (228, 171, 167)]

t = Turtle()
t.hideturtle()
t.penup()
x=50
y=0
i=0


def random_color():
    color = random.randint(0, len(color_list)-1)
    return color_list[color]


while i < 10:
    e = 0
    x = 0

    while e < 10:
        x += 50
        t.setx(x)
        t.dot(20, random_color())
        e += 1

    y += 50
    t.sety(y)
    i += 1

screen = Screen()
screen.exitonclick()
