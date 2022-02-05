import colorgram
import random
from turtle import Turtle, Screen


# Get colour palette

colours = colorgram.extract("hirst.jfif", 32)
colour_list = []
for i in range(1, len(colours)):
    if colours[i].rgb.r < 235 or colours[i].rgb.g < 235 or colours[i].rgb.b < 235:
        colour_list.append(colours[i].rgb)


def random_colour():
    return random.choice(colour_list)


# Set turtle parameters

tim = Turtle()
tim.hideturtle()
tim.pensize(20)
tim.speed(0)
tim.penup()
screen = Screen()
screen.colormode(255)


for i in range(-400, 400, 50):
    for j in range(-400, 400, 50):
        tim.color(random_colour())
        tim.setpos(j, i)
        tim.pendown()
        tim.forward(1)
        tim.penup()


screen.exitonclick()
