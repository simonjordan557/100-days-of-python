# Imports
from turtle import Turtle
import time

# Constants

UP = 90.0
DOWN = 270.0
PADDLE_SPEED = 25
SCREEN_BOUNDARY = 280
SEGMENT_WIDTH = 20


# Class declaration & constructor
class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.speed(0)
        self.starting_x = x
        self.starting_y = y
        self.goto(self.starting_x, self.starting_y)

    def longer_paddle(self):
        upper_section_y = self.ycor() + SEGMENT_WIDTH
        lower_section_y = self.ycor() - SEGMENT_WIDTH
        paddle_up = Paddle(self.xcor(), upper_section_y)
        paddle_down = Paddle(self.xcor(), lower_section_y)
        self.paddle_as_list = [paddle_up, self, paddle_down]

    def move_up(self):
        if not self.paddle_as_list[0].ycor() >= SCREEN_BOUNDARY:
            for paddle in self.paddle_as_list:
                paddle.setheading(UP)
                paddle.forward(PADDLE_SPEED)

    def move_down(self):
        if not self.paddle_as_list[2].ycor() <= -SCREEN_BOUNDARY:
            for paddle in self.paddle_as_list:
                paddle.setheading(DOWN)
                paddle.forward(PADDLE_SPEED)


