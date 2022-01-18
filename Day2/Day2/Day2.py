# Day 2 - TipCalculator

# Data Types

# String

print("Hello"[0])
print("Hello"[4])
print("123" + "345")

# Integer

print(123 + 345)
print(1_111 + 2_222)

# Float

print(3.14 + 3.14)

# Boolean

print(True and False)
print(True or False)

# Exercise 1

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
a = int(two_digit_number[0])
b = int(two_digit_number[1])

sum = a + b
print(str(sum))

# Exercise 2

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(int(float(weight) / (float(height) ** 2)))

# Rounding

print(8 / 3)
print(8 // 3)
print(round(2.666666666, 2))
print(8 % 3)

# f-strings

# use f as you'd use $ in C# string

score = 7
fraction = 0.5
isWinning = True

print(f"Your score is {score} multiplied by {fraction}, which is {score * fraction}. It is {isWinning} that you are winning!")

# Exercise 3

# Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left = 90 - (int(age))

print(f"You have {years_left * 365} days, {years_left * 52} weeks, and {years_left * 12} months left.")

# Tip Calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 

print("Welcome to the tip calculator!")
totalBill = float(input("What was the total bill?\n"))
percentageTip = int(input("What percent tip would you like to give?\n"))
numberOfDiners = int(input("How many people are splitting the bill?\n"))

eachPersonPays = (totalBill * (percentageTip / 100 + 1)) / numberOfDiners

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

result = "{:.2f}".format(eachPersonPays)

print(f"Each person should pay ${result}.")

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.
