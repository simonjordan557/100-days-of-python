from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

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
scoreboard.update_score(score)
game_is_on = True


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
        scoreboard.game_over(score)
    if snake.head.distance(food) <= 15:
        food.change_location()
        snake.eaten_food()
        score += 1
        scoreboard.update_score(score)
        snake.speed_up()

screen.exitonclick()
