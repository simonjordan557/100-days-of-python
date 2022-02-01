# Day 16 - Object-Oriented Programming

from turtle import Turtle, Screen
from prettytable import PrettyTable, DOUBLE_BORDER

timmy = Turtle()
print(type(timmy))
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvwidth)
print(my_screen.canvheight)
my_screen.exitonclick()

table = PrettyTable()
table.set_style(DOUBLE_BORDER)
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Lightning", "Water", "Fire"])

table.align = "l"
print(table)
