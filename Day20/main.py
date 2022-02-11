from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from os.path import exists

# Set up screen
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Set up game
snake = Snake()
food = Food()
scoreboard = Scoreboard()
score = 0
highscore =0
game_is_on = True

# Check for high score
if not exists("highscore.txt"):
    with open("highscore.txt", "w") as f:
        f.write(str(highscore))
else:
    with open("highscore.txt", "r") as f:
        highscore = int(f.readline())
scoreboard.update_score(score, highscore)

# Listen for keyboard input
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main loop
while game_is_on:

    snake.move_snake()
    screen.update()
    snake.trim_positions()
    if snake.hit_wall() or snake.eaten_tail():
        game_is_on = False
        scoreboard.game_over(score, highscore)
        if score > highscore:
            highscore = score
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
    if snake.head.distance(food) <= 15:
        food.change_location()
        snake.eaten_food()
        score += 1
        if score > highscore:
            highscore = score
        scoreboard.update_score(score, highscore)
        snake.speed_up()

screen.exitonclick()
