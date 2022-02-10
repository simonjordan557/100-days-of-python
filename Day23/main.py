# Imports
import time
from turtle import Screen, Turtle
from player import Player
from scoreboard import Scoreboard
from spawnManager import Spawnmanager

# Constants
UPDATE_INTERVAL = 0.1
SCREEN_DIMENSION = 600

# Initialise screen
screen = Screen()
screen.setup(height=SCREEN_DIMENSION, width=SCREEN_DIMENSION)
screen.tracer(0)

# Draw Background
screen.bgcolor("grey")
brush = Turtle()
brush.penup()
brush.speed(0)
brush.pensize(40)
brush.color("lime")
brush.goto(300, -280)
brush.pendown()
brush.setheading(180)
brush.forward(600)
brush.penup()
brush.goto(300, 280)
brush.pendown()
brush.forward(600)
brush.penup()
brush.color("white")
brush.pensize(2)
for i in range(-220, 221, 40):
    brush.goto(300, i)
    for j in range(12):
        brush.forward(25)
        brush.pendown()
        brush.forward(75)
        brush.penup()

# Initialise player, scoreboard, spawn manager
spawnmanager = Spawnmanager()
player = Player(spawnmanager)
scoreboard = Scoreboard()

# Event listener
screen.listen()
screen.onkey(player.move_player, "Up")

# Functions
def reset_spawn_delay():
    return spawnmanager.spawn_delay / UPDATE_INTERVAL

# Variables
game_is_on = True
spawn_delay = reset_spawn_delay()

# Initialise first run
scoreboard.display_score()

# Main loop
while game_is_on:
    time.sleep(UPDATE_INTERVAL)
    screen.update()
    for car in spawnmanager.current_cars:
        car.move_car()
    spawn_delay -= 1
    if spawn_delay <= 0:
        spawnmanager.send_car()
        spawn_delay = spawnmanager.spawn_delay / UPDATE_INTERVAL

    if player.player_won():
        scoreboard.increase_score()
        scoreboard.display_score()
        spawnmanager.level_up()
        player.reset_player()
        spawn_delay = spawnmanager.spawn_delay / UPDATE_INTERVAL
        time.sleep(1.5)

    if player.player_died():
        game_is_on = False
        scoreboard.display_game_over()
        spawnmanager.level_up()

screen.exitonclick()
