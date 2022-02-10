# Imports
from turtle import Turtle
import random

# Constants
SCREEN_BOUNDARY = 280
OUT_OF_BOUNDS = 310
COLLISION_RANGE = 40
HEADINGS_AS_LIST = [45.0, 135.0, 225.0, 315.0]
WALL_HEADINGS = {
    45.0: 315.0,
    135.0: 225.0,
    225.0: 135.0,
    315.0: 45.0,
}

PADDLE_HEADINGS = {
    45.0: 135.0,
    135.0: 45.0,
    225.0: 315.0,
    315.0: 225.0,
}

# Class declaration
class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.penup()
        self.color("white")
        self.speed(0)
        self.reset_ball()
        self.velocity = 10

    def reset_ball(self):
        self.hideturtle()
        self.goto(0, random.randint(-240, 240))
        self.setheading(random.choice(HEADINGS_AS_LIST))
        self.showturtle()
        self.velocity = 10

    def move(self):
        self.forward(self.velocity)

    def hit_paddle(self, other):
        return self.distance(other) < COLLISION_RANGE

    def hit_wall_top(self):
        return self.ycor() >= SCREEN_BOUNDARY

    def hit_wall_bottom(self):
        return self.ycor() <= -SCREEN_BOUNDARY

    def bounce_wall_top(self):
        if self.heading() == 45.0 or self.heading() == 135.0:
            self.setheading(WALL_HEADINGS[round(self.heading())])

    def bounce_wall_bottom(self):
        if self.heading() == 225.0 or self.heading() == 315.0:
            self.setheading(WALL_HEADINGS[round(self.heading())])

    def bounce_paddle_left(self):
        if self.heading() == 135.0 or self.heading() == 225.0:
            self.setheading(PADDLE_HEADINGS[round(self.heading())])
            self.velocity += 1

    def bounce_paddle_right(self):
        if self.heading() == 45.0 or self.heading() == 315.0:
            self.setheading(PADDLE_HEADINGS[round(self.heading())])
            self.velocity += 1

    def out_of_bounds_left(self):
        return self.xcor() < -OUT_OF_BOUNDS

    def out_of_bounds_right(self):
        return self.xcor() > OUT_OF_BOUNDS
