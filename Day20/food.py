from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(0)
        self.color("red")
        self.shapesize(0.5)
        self.change_location()

    def change_location(self):
        self.penup()
        self.goto(random.choice(range(-280, 290, 10)), random.choice(range(-280, 290, 10)))
        self.pendown()




