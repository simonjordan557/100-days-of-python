# Day 10 - Calculator


def format_name(inName):
  nameAsList = inName.lower().split(" ")
  for word in nameAsList:
    first = word[0].upper()
    last = word[1:]
    nameAsList[nameAsList.index(word)] = first + last
  return " ".join(nameAsList)

userName = input("Enter your name: ")
print(f"Hello, {format_name(userName)}.")

def is_leap(year):
  """A function to return whether a given year is a leap year"""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(inYear, inMonth):
  """Returns the number of days in a given month"""
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if inMonth == 2 and is_leap(inYear):
    return 29
  else:
    return month_days[inMonth - 1]
  
  
# Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)