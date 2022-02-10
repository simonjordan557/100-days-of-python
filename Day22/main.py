# Imports
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
LINE_INTERVAL = 20
SCORE_START_X = 100
PL_START_X = 280
PL_START_Y = 0

# Initialise game

# Set up screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

# Set up turtle to draw middle line
turtle = Turtle()
turtle.hideturtle()
turtle.speed(0)
turtle.color("white")
turtle.penup()
turtle.goto(0, (SCREEN_HEIGHT * -0.5))
turtle.setheading(90.0)

# Draw line
for i in range(20):
    turtle.pendown()
    turtle.forward(LINE_INTERVAL)
    turtle.penup()
    turtle.forward(LINE_INTERVAL)

# Create 2 paddles
p1_paddle = Paddle(-PL_START_X, PL_START_Y)
p1_paddle.longer_paddle()
p2_paddle = Paddle(PL_START_X, PL_START_Y)
p2_paddle.longer_paddle()

# Create 2 scoreboards
p1_score = Scoreboard(-SCORE_START_X)
p2_score = Scoreboard(SCORE_START_X)

# Create ball

ball = Ball()

# Capture keyboard inputs
screen.listen()

screen.onkeypress(p1_paddle.move_up, "w")
screen.onkeypress(p1_paddle.move_down, "s")
screen.onkeypress(p2_paddle.move_up, "Up")
screen.onkeypress(p2_paddle.move_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.033)
    ball.move()
    screen.update()
    if ball.hit_paddle(p1_paddle):
        ball.bounce_paddle_left()
    elif ball.hit_paddle(p2_paddle):
        ball.bounce_paddle_right()
    elif ball.hit_wall_top():
        ball.bounce_wall_top()
    elif ball.hit_wall_bottom():
        ball.bounce_wall_bottom()
    elif ball.out_of_bounds_left():
        p2_score.increase_score()
        time.sleep(2)
        ball.reset_ball()
    elif ball.out_of_bounds_right():
        p1_score.increase_score()
        time.sleep(2)
        ball.reset_ball()

    if p1_score.score >= 10:
        p1_score.clear()
        p2_score.clear()
        p2_score.game_over("1")
        game_is_on = False
    elif p2_score.score >= 10:
        p1_score.clear()
        p2_score.clear()
        p2_score.game_over("2")
        game_is_on = False


screen.exitonclick()
