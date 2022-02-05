# Day 18 - Turtle Graphics

from turtle import Turtle, Screen
import random


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def square():
    for i in range(4):
        tim.forward(100)
        tim.right(90)

def broken_line():
    for i in range(15):
        tim.forward(10)
        if tim.isdown():
            tim.penup()
        else:
            tim.pendown()

def increasingly_complex_shapes(highest_number_of_sides, starting_sides = 3):

    tim.pendown()

    sides = starting_sides
    angle = 360 / sides


    tim.color(random_colour())
    for i in range(sides):
        tim.forward(100)
        tim.right(angle)

    if sides < highest_number_of_sides:
        sides += 1
        increasingly_complex_shapes(highest_number_of_sides, sides)
    return


def random_walk():
    headings = [0, 90, 180, 270]
    tim.pensize(10)
    tim.speed(9)
    while True:
        direction = random.choice(headings)
        tim.setheading(direction)
        tim.color(random_colour())
        tim.forward(25)

def circle():
    tim.clear()
    tim.speed(10)
    for i in range(0, 360, 6):
        tim.setheading(i)
        tim.color(random_colour())
        tim.circle(100)


tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("lime", "magenta")
square()
tim.color("red", "pink")
tim.clear()
broken_line()
tim.clear()
tim.home()
screen.colormode(255)
print(screen.colormode())
tim.speed(5)
increasingly_complex_shapes(20)
tim.clear()
tim.home()
circle()
tim.clear()
tim.home()
random_walk()
screen.exitonclick()
