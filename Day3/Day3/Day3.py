# Day 3 - TreasureIsland

# Control flow and logical operators

print("Welcome to the rollercoaster!")
height = int(input("What is your height? "))

if height > 120:
    print("You can ride!")
    age = int(input("What is your age? "))
    if age < 12:
        price = 5
    elif age <= 18:
        price = 7
    elif age >= 45 and age <= 55:
        price = 0 
    else:
        price = 12

    photo = input("Do you want a photo (Y/N)? ")

    if photo.upper() == "Y":
        price += 3

    print(f"Please pay ${price}.")
else:
    print("Sorry, you're not tall enough.")

number = int(input("Which number do you want to check? "))
#  Don't change the code above 

#Write your code below this line 

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# Don't change the code above 

#Write your code below this line 

bmi = round(weight / (height ** 2))

if bmi < 18.5:
    msg = "are underweight"
elif bmi < 25:
    msg = "have a normal weight"
elif bmi < 30:
    msg = "are slightly overweight"
elif bmi < 35:
    msg = "are obese"
else:
    msg = "are clinically obese"

print(f"Your BMI is {bmi}, you {msg}.")

year = int(input("Which year do you want to check? "))
#  Don't change the code above 

#Write your code below this line 

if year % 4 != 0:
    print("Not leap year.")
else:
    if year % 100 == 0 and year % 400 != 0:
        print("Not leap year.")
    else:
        print("Leap year.")

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
#  Don't change the code above 

#Write your code below this line 

if size == "S":
    if add_pepperoni == "Y":
        price = 17
    else:
        price = 15
elif size == "M":
    if add_pepperoni == "Y":
        price = 23
    else:
        price = 20
else:
    if add_pepperoni == "Y":
        price = 28
    else:
        price = 25

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}.")

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
#  Don't change the code above 

#Write your code below this line 

combinedName = name1.lower() + name2.lower()
firstDigit = 0
secondDigit = 0

for s in "true":
    firstDigit += combinedName.count(s)
for s in "love":
    secondDigit += combinedName.count(s)

score = int(str(firstDigit) + str(secondDigit))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

# Treasure Island

print("Welcome to Treasure Island.")

firstChoice = input("You wash up on a path across a sandy beach. head 'Left' or 'Right'? ").lower()

if firstChoice == "right":
    print("You head right and feel the beach give way beneath your feet. As you slide below the quicksand you realise this is GAME OVER!")
else:
    secondChoice = input("You emerge at a huge oasis with a temple atop a central island. Will you 'Wait' for a boat, or 'Swim'? ").lower()

    if secondChoice == "swim":
        print("Already tired from your harrowing journey, you quickly realise you underestimated the vastness of the oasis. Sinking beneath the water, you realise this is GAME OVER!")
    else:
        thirdChoice = input("A boat takes you to the 3 painted doors of the temple. 'Yellow', 'Red', or 'Blue'?").lower()

        if thirdChoice == "yellow":
            print("The doors' yellow colour was the gleam of gold! you sail the boat home to enjoy your riches.")
        else:
            print("RNG finally turns against you, the door leads to an unending pit! As you tumble to oblivion, you realise this is GAME OVER!")
