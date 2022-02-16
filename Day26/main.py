numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

#Write your 1 line code 👇 below:

squared_numbers = [n ** 2 for n in numbers]

#Write your code 👆 above:

print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [n for n in numbers if n % 2 == 0]

#Write your code 👆 above:

print(result)

with open("file1.txt") as f:
    list_1 = f.readlines()

with open("file2.txt") as f:
    list_2 = f.readlines()

result =[int(n) for n in list_1 if n in list_2]

# Write your code above 👆

print(result)
import random
names = ["Alfie", "Bob", "Charlie", "Dora", "Edna", "Freddie"]

scores = {name: random.randint(1, 100) for name in names}
print(scores)

passed_students = {name: score for (name, score) in scores.items() if score >= 60}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

sentence_list = sentence.split()
result = {word: len(word) for word in sentence_list}

print(result)
