# Day 4 - RockPaperScissors
# Randomisation and lists

import random
import myModule

randomInteger = random.randint(1, 10)
print(randomInteger)

randomFloat = random.random()
print(randomFloat)
print(randomFloat * 5)

print(f"My age is {myModule.myAge}.")

#  Don't change the code below 
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)	 
#Write the rest of your code below this line 

if random.randint(0, 1) == 0:
    print("Tails")
else:
    print("Heads")

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#  Don't change the code above 

#Write your code below this line 
victim = names[random.randint(0, len(names) - 1)]
print(f"{victim} is going to buy the meal today!")

# RockPaperScissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 
graphics = [rock, paper, scissors]

playerMove = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if playerMove < 0 or playerMove > 2:
    print("Invalid selection - YOU LOSE!")
else:

    computerMove = random.randint(0, 2)

    print(graphics[playerMove])
    print("\nCOMPUTER CHOSE:\n")
    print(graphics[computerMove])

    if playerMove == computerMove:
        print("A DRAW!")
    elif playerMove == computerMove + 1 or playerMove == computerMove - 2:
        print("YOU WIN!")
    else:
        print("YOU LOSE!")



