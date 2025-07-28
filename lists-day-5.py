# Create a list for cars
cars = ["Toyota", "Honda", "Tesla", "Ferrari"]

# Print the cars
print("My favourite car is", cars[3])

# Create a list for pizza toppings
toppings = []

# Add toppings while there isn't blank pizza
query = ""
while query != "":
  print("What topping are you using?") 
  query = input()

  toppings.append(query)

print("Making a pizza!")
for topping in toppings:
  print("Adding topping:", topping)

print("Done!")
