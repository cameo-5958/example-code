#!program-flow-day-3.py
# Creates a program that asks for the
# user's age and password, and displays
# a custom print for both

print("Good morning!")
print("How old are you?")
age = int(input())

if age < 0: 
  print("Who gave you a computer?")

elif 0 <= age <= 14:
  print("Go back to preschool you midget")

elif 14 < age < 19:
  print("Shouldn't you be in school?")

elif 19 <= age < 65:
  print("Why aren't you working?")

else:
  print("Hi grandpa")

print("Please input your password.")
PASSWORD = "Password123"
attempt = input()

while attempt != PASSWORD:
  print("Wrong.")
  print("Please input your password.")
  attempt = input()

