# Imports
from turtle import Turtle
from datetime import *

# Constants
XPOS = 250
YPOS = 170
PENCOLOUR = "black"
URGENT_COLOUR = "red"
ALIGN = "center"
FONT = ("courier", 16, "bold")
FULL_TIMER = timedelta(minutes=10)

# Class declaration
class Timer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.pencolor(PENCOLOUR)
        self.goto(XPOS, YPOS)
        self.pendown()

    def start_timer(self):
        self.start_time = datetime.now()

    def calculate_remaining_time(self):
        self.elapsed_time = datetime.now() - self.start_time
        self.time_left = FULL_TIMER - self.elapsed_time

    def is_timer_expired(self):
        return self.time_left <= timedelta(seconds=0)

    def display_time(self):
        self.clear()
        if self.time_left < timedelta(minutes=2):
            self.pencolor(URGENT_COLOUR)
        self.write(f"{self.time_left.seconds // 60}:{self.time_left.seconds % 60}", align=ALIGN, font=FONT)

    def reset_timer(self):
        self.clear()
        self.start_time = None
        self.elapsed_time = None
        self.time_left = FULL_TIMER
        self.pencolor(PENCOLOUR)


