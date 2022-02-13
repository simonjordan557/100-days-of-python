# Imports
import pandas
from turtle import Screen
from textwriter import TextWriter
from scoreboard import Scoreboard
from timer import Timer
import time

# Constants
SCREEN_HEIGHT = 491
SCREEN_WIDTH = 725
BG_PATH = "./us-states-game-start/us-states-game-start/blank_states_img.gif"
DATA_PATH = "./us-states-game-start/us-states-game-start/50_states.csv"

# Initialise screen
screen = Screen()
screen.title("U.S. States Game")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgpic(BG_PATH)

# Initialise text elements
textwriter = TextWriter()
scoreboard = Scoreboard()
timer = Timer()

# Import data
data = pandas.read_csv(DATA_PATH)
data_dict = {}
for state in data.state:
    row = data[data.state == state]
    data_dict[state] = (row.x.to_list()[0], row.y.to_list()[0])

# Variables
states_pool = []
states_guessed = []
game_is_on = True


# Functions
def reset_states():
    states_guessed.clear()
    states_pool.clear()
    for state in data_dict.keys():
        states_pool.append(state)


def get_player_input():
    return screen.textinput(f"{len(states_pool)} states left", "Name a state: ").title()


def check_unguessed_state(toCheck):
    if toCheck in states_pool:
        return True
    return False


def correct_answer_actions(correct_answer):
    states_pool.remove(correct_answer)
    states_guessed.append(correct_answer)
    textwriter.write_text(data_dict[correct_answer][0], data_dict[correct_answer][1], correct_answer)


def display_missed_states():
    textwriter.color("red")
    for state in states_pool:
        textwriter.write_text(data_dict[state][0], data_dict[state][1], state)
    textwriter.color("black")
    time.sleep(5)


def end_game():
    global game_is_on
    display_missed_states()
    timer.reset_timer()
    scoreboard.reset_scoreboard()
    textwriter.reset_screen()
    output_csv()
    reset_states()
    game_is_on = False


def output_csv():
    missed_states = pandas.DataFrame({"States you missed:": states_pool})
    missed_states.to_csv("missed_states.csv")

# Initialise game
timer.start_timer()
reset_states()

# Main loop
while game_is_on:
    scoreboard.update_scoreboard()
    if len(states_guessed) == 50:
        textwriter.write_text(0, 200, "YOU WIN!!!!")
        end_game()
        continue
    timer.calculate_remaining_time()
    timer.display_time()
    if timer.is_timer_expired():
        end_game()
        continue

    guess = get_player_input()
    if guess.lower() == "exit":
        end_game()
    if not check_unguessed_state(guess):
        continue
    else:
        correct_answer_actions(guess)
        scoreboard.increase_score()


screen.exitonclick()

# import csv
# import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

#
# def average(data_in):
#     return sum(data_in) // len(data_in)
#
#
# def c_to_f(temp):
#     return (temp * 1.8) + 32
#
#
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(f"Average temperature: {average(temp_list)} degrees.")
# print(f"Max temperature this week: {data['temp'].max()} degrees.")
#
# print(data[data.temp == data.temp.max()])
#
# print(data.index)
# print(data.columns)
# print(data[["day", "condition"]])
# s = data.loc[3:5]
# print(s)
# print(s[s.temp == s.temp.min()])
#
# monday = data.loc[0]
# print(f"Monday's temperature was {c_to_f(monday.temp)} degrees F.")
#
# custom_data_dict = {
#     "Artist": ["Phil Collins", "Michael Jackson", "Pink Floyd"],
#     "Title":  ["In The Air Tonight", "Dangerous", "Learning To Fly"]
# }
#
# custom_data = pandas.DataFrame(custom_data_dict, index=["First", "Second", "Third"])
# print(custom_data)
# custom_data.to_csv("charts.csv")

# Squirrel stuff!
#
# squirrel_data = pandas.read_csv("squirrel_data.csv")
#
#
# def get_num_each_colour(colour):
#     return len(squirrel_data[squirrel_data["Primary Fur Color"] == colour])
#
#
# output_dict = {}
# colours = ["Gray", "Cinnamon", "Black"]
# frequencies = []
# for colour in colours:
#     frequencies.append(get_num_each_colour(colour))
#
# output_dict["Fur Colour"] = colours
# output_dict["Count"] = frequencies
#
# output = pandas.DataFrame(output_dict)
# print(output)
# output.to_csv("squirrel_colours.csv")


# sq = squirrel_data.loc[35:40]
# adults = (sq[sq.Age == "Adult"])
# key_info = (adults[["Unique Squirrel ID", "Shift", "Primary Fur Color"]])
# key_info_dict = key_info.to_dict()
# print(key_info_dict)
# for k, v in key_info_dict['Primary Fur Color'].items():
#     key_info_dict["Primary Fur Color"][k] = "Lime Green"
# key_info_updated = pandas.DataFrame(key_info_dict)
# print(key_info_updated)
# key_info_updated.to_csv("lime_green_squirrels.csv")
