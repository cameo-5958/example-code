# Exploring input and output

print("Hello world!")
print("My name is Kunru. What's yours?") 

# Get user input
name = input()
print("So your name is", name, "? That's cool!")

print("How old are you?")
age = input()
age = int(age) # Cast input to integer
to_fifty = 50 - age

print("It will be", to_fifty,"years until you are fifty years old.
