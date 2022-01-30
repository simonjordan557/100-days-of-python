# Day 14 - Higher Or Lower

from art import logo, vs
from gameData import data
import random, os

# Functions : display screen, get user input, check answer, update score, assign random person

def DisplayScreen(a, b):
    print(logo)
    print(message)
    if not gameOver:
        print(f"{a['name']}, a {a['description']} from {a['country']}")
        print(vs)
        print(f"{b['name']}, a {b['description']} from {b['country']}")

def PickNextPerson():
    return data.pop(random.randint(0, len(data) - 1))

def PersonBToPersonA(a, b):
    a = b
    return a

def GetUserInput():
    return input("Who has more followers, A or B? ").lower()

def CheckUserAnswer(answer):
    if personA["follower_count"] > personB["follower_count"]:
        if answer == "a":
            return False
        else:
            return True

def UpdateScore(score):
    score += 1
    return score

def UpdateMessage(score):
    if gameOver:
        return f"You lose! You scored {score}."
    else:
        return f"That's correct! Your current score is {score}."
    
       
# Set up global variables and initial screen on first run

gameOver = False
message = ""
currentScore = 0
personA = PickNextPerson();
personB = PickNextPerson();
DisplayScreen(personA, personB) 


# Gameplay loop

while not gameOver:                      
    userGuess = GetUserInput()                          # Get answer
    gameOver = CheckUserAnswer(userGuess)               # Is it correct? set flag for whether to keep running the loop
    if not gameOver:                                    # If so:
        currentScore = UpdateScore(currentScore)            # Increase score
        personA = PersonBToPersonA(personA, personB)        # Make person B person A
        personB = PickNextPerson()                          # Get a new person B

    message = UpdateMessage(currentScore)               # Update message to either "You lose" or "You win"
    DisplayScreen(personA, personB)                     # Display updated info. Game ends if last answer was wrong.

