# Day 9 - Secret Auction

# Dictionaries and Nesting

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#  Don't change the code above 

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.
for key in student_scores:
    if student_scores[key] >= 91:
        student_grades[key] = "Outstanding"
    elif student_scores[key] >= 81:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

    

# Don't change the code below 
print(student_grades)

travel_log = {
    "France": {"Ctiies Visited: ": ["Paris", "Lille", "Dijon"]},
    "Germany": {"Cities Visited: ": ["Hamburg", "Berlin"]}
    }

print(travel_log)

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
# Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 
def add_new_country(nation, trips, towns):
    travel_log.append({"country": nation, "visits": trips, "cities": towns})




# Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

import os
import art
print(art.logo)
print("Welcome to the Secret Auction!")

bids = {}
noMoreBidders = False

while not noMoreBidders:
  bidName = input("What is your name? ")
  bidAmount = int(input("What is your highest bid? "))
  bids[bidName] = bidAmount
  if input("Any more bidders (Y/N)? ").lower() == "n":
    noMoreBidders = True
  os.system("cls")

highestBid = 0
highestBidder = {}

for bidder in bids:
  if bids[bidder] > highestBid:
    highestBid = bids[bidder]
    highestBidder = {}
    highestBidder[bidder] = bids[bidder]

for k, v in highestBidder.items():
  print(f"{k} wins with a bid of ${v}!")