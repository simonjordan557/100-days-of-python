from turtle import Turtle
import time

STARTING_POSITIONS = [(0.0, 0.0), (-20.0, 0.0), (-40.0, 0.0)]
MOVEMENT_DISTANCE = 20
HEADINGS = {
    "E": 0.0,
    "N": 90.0,
    "W": 180.0,
    "S": 270.0,
}


class Snake:

    def __init__(self):
        # Create a list of snake segments

        self.movement_delay = 0.03

        self.snake_body = []
        for i in STARTING_POSITIONS:
            t = Turtle(shape="square")
            t.color("green", "white")
            t.penup()
            t.goto(i)
            self.snake_body.append(t)

        self.head = self.snake_body[0]

        # Set up a record of previous coordinates for subsequent segments to follow
        self.position_tracker = []
        for i in range(len(STARTING_POSITIONS)):
            xpos = self.snake_body[i].xcor()
            ypos = self.snake_body[i].ycor()
            self.position_tracker.append([xpos, ypos])

    def move_snake(self):
        self.head.forward(MOVEMENT_DISTANCE)
        time.sleep(self.movement_delay)
        self.position_tracker.insert(0, [self.head.xcor(), self.head.ycor()])
        for i in range(1, len(self.snake_body)):
            self.snake_body[i].goto(self.position_tracker[i][0], self.position_tracker[i][1])
            time.sleep(self.movement_delay)

    def up(self):
        if self.head.heading() != HEADINGS["S"]:
            self.head.setheading(HEADINGS["N"])

    def down(self):
        if self.head.heading() != HEADINGS["N"]:
            self.head.setheading(HEADINGS["S"])

    def left(self):
        if self.head.heading() != HEADINGS["E"]:
            self.head.setheading(HEADINGS["W"])

    def right(self):
        if self.head.heading() != HEADINGS["W"]:
            self.head.setheading(HEADINGS["E"])

    def trim_positions(self):
        for i in range(len(self.snake_body) + 1, len(self.position_tracker)):
            self.position_tracker.pop(i)

    def hit_wall(self):
        if self.head.xcor() >= 300 or self.head.ycor() >= 300 or \
                self.head.xcor() <= -300 or self.head.ycor() <= -300:
            return True
        else:
            return False

    def eaten_tail(self):
        for i in range(1, len(self.snake_body)):

            if round(self.head.xcor()) == round(self.snake_body[i].xcor()) and \
                    round(self.head.ycor()) == round(self.snake_body[i].ycor()):
                return True
        return False

    def eaten_food(self):
        t = Turtle(shape="square")
        t.color("green", "white")
        t.penup()
        self.snake_body.append(t)

    def speed_up(self):
        if self.movement_delay > 0.01:
            self.movement_delay -= 0.005



