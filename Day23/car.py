# Imports
from turtle import Turtle
import time

# Constants

STARTING_X = 350
DIRECTION = 180.0

# Class Declaration
class Car(Turtle):
    def __init__(self, y, length, colour, speed):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed(0)
        self.setheading(DIRECTION)
        self.color(colour)
        self.velocity = speed
        self.length = length * 20
        self.shapesize(stretch_len=length)
        self.start_y = y
        self.goto(STARTING_X, self.start_y)

    def move_car(self):
        self.forward(self.velocity)

    def reset_car(self):
        self.forward(0)
        self.goto(STARTING_X, self.start_y)


