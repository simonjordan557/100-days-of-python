from turtle import Turtle, Screen
import random


# def draw_circle():
#     tim.clear()
#     tim.color(random_colour())
#     tim.pensize(15)
#     tim.circle(100)
#
#
# def w():
#     tim.forward(10)
#
#
# def s():
#     tim.back(10)
#
#
# def a():
#     tim.left(10)
#
#
# def d():
#     tim.right(10)
#
#
# def c():
#     tim.penup()
#     tim.home()
#     tim.clear()
#     tim.pendown()
#
#
# def random_colour():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b

def random_forward_motion(t):
    t.forward(random.randint(1, 10))


turtles_dic = {
    "red": "",
    "orange": "",
    "yellow": "",
    "green": "",
    "blue": "",
    "purple": "",
}

for k in turtles_dic:
    turtles_dic[k] = Turtle()
    turtles_dic[k].shape("turtle")
    turtles_dic[k].color(k)

screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)
bet = screen.textinput(title="Place Your Bet", prompt="Who will win the race? Enter a colour: ")

xpos = -230
ypos = -150
for v in turtles_dic.values():
    v.penup()
    v.goto(xpos, ypos)
    ypos += 60

race_is_on = True

while race_is_on:
    for k, v in turtles_dic.items():
        random_forward_motion(v)
        if v.xcor() >= 230:
            winner = k
            race_is_on = False

print(f"The winner is {winner}!")
if bet == winner:
    print("You bet correctly!")
else:
    print(f"You bet on {bet}, better luck next time.")



# screen.listen()
# screen.onkeypress(fun=a, key="a")
# screen.onkeypress(fun=w, key="w")
# screen.onkeypress(fun=s, key="s")
# screen.onkeypress(fun=d, key="d")
# screen.onkey(fun=c, key="c")

screen.exitonclick()
