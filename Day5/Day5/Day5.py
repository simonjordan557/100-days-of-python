# Day 5 - PasswordGenerator

# Loops

import random



student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Don't change the code above 


#Write your code below this row 

totalHeight = 0
listLength = 0

for height in student_heights:
    totalHeight += height
    listLength += 1

print(round(totalHeight / listLength))

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# Don't change the code above 

#Write your code below this row 

maximum = 0

for n in student_scores:
    if n > maximum:
        maximum = n

print(f"The highest score in the class is: {maximum}")

total = 0

for i in range(0, 101, 2):
    total += i

print(total)

#Write your code below this row 

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Password Generator
        
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

passwordList = []

for i in range(0, nr_letters):
  passwordList.append(letters[random.randint(0, len(letters) - 1)])
for i in range(0, nr_numbers):
  passwordList.append(numbers[random.randint(0, len(numbers) - 1)])
for i in range(0, nr_symbols):
  passwordList.append(symbols[random.randint(0, len(symbols) - 1)])

randomisedPasswordList = []

for i in range(len(passwordList)):
  char = passwordList[random.randint(0, len(passwordList) - 1)]
  passwordList.remove(char)
  randomisedPasswordList.append(char)

password = "".join(randomisedPasswordList)

print(password)