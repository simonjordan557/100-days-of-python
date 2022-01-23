# Day 8 - Caesar Cipher

def greet():
  print("Hi!")
  print("Nice to meet you!")
  print("Hello world!")

def greetWithName(name):
  print(f"Hi {name}!")
  print(f"Nice to meet you, {name}!")
  print("Hello world!")

def greetWithNameLocation(name, location):
  print(f"Hi {name}!")
  print(f"Nice to meet you, {name}!")
  print(f"Hello {location}!")

greet()
greetWithName("Simon")
greetWithNameLocation(location="England", name="Simon")


#Write your code below this line 

import math

def paint_calc(height, width, cover):
    area = height * width
    cans = math.ceil(area / cover)
    print(f"You'll need {cans} cans of paint.")

#Write your code above this line 
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)



#Write your code below this line 
def prime_checker(number):
    if number % 2 == 0 and number != 2:
        print("It's not a prime number.")
    else:
        prime = True
        for i in range(3, number // 2, 2):
            if number % i == 0:
                prime = False
                break
        if prime:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")
       

#Write your code above this line 
    
#Do NOT change any of the code below
n = int(input("Check this number: "))
prime_checker(number=n)

from art import logo

def caesar(direction, text, shift):
    if shift > 25:
        shift = shift % 26
    output = ""
    offset = 26
    if direction == "decode":
        shift *= -1;
        offset *= -1

    for letter in text:
        if letter.isalpha():
            if alphabet.index(letter) + shift > 25:
                output += alphabet[(alphabet.index(letter) + shift) % offset]
            else:
                output += alphabet[alphabet.index(letter) + shift]
        else:
            output += letter

    print(f"The {direction}d text is {output}.")

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
wantsToExit = False

while not wantsToExit:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)

    if input("Have another go? (Y/N): ").lower() == "n":
        wantsToExit = True
