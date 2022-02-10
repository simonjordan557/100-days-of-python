# Imports
from turtle import Turtle
from spawnManager import Spawnmanager

# Constants

STARTING_X = 0
STARTING_Y = -280
STARTING_HEADING = 90.0
MOVE_DISTANCE = 40
WIN_THRESHOLD = 280

# Class declaration
class Player(Turtle):
    def __init__(self, spawner):
        super().__init__(shape="turtle")
        self.penup()
        self.color("green")
        self.speed(0)
        self.setheading(STARTING_HEADING)
        self.goto(STARTING_X, STARTING_Y)
        self.spawner = spawner

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def player_won(self):
        return self.ycor() >= WIN_THRESHOLD

    def player_died(self):
        for car in self.spawner.current_cars:
            if self.distance(car) <= car.length / 2 and round(self.ycor()) == round(car.ycor()):
                return True
        return False

    def reset_player(self):
        self.goto(STARTING_X, STARTING_Y)

