# Day 12 - Scope and Number Guessing Game

enemies = 1

def increase_enemies():
  print(enemies)
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

import random, art

def Win():
    global gameIsOver
    print(f"Congratulations! {targetNumber} was the correct number. ")
    gameIsOver = True

def WrongGuess():
    global attempts
    attempts -= 1
    if attempts < 1:
        Lose()

def Lose():
    global gameIsOver
    print(f"Sorry, you lose. The correct number was {targetNumber}.")
    gameIsOver = True


# Initialise Game

print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
targetNumber = random.randint(1, 100)
difficulty = input("Do you want to play (E)asy or (H)ard? ").lower()
if difficulty == "e":
    attempts = 10
else:
    attempts = 5

gameIsOver = False

# Core Gameplay Loop

while not gameIsOver:
    guessedNumber = int(input(f"You have {attempts} lives remaining. Guess a number: "))
    if guessedNumber == targetNumber:
        Win()
    elif guessedNumber < targetNumber:
        print(f"Too low.")
        WrongGuess()
    else:
        print("Too high.")
        WrongGuess()



