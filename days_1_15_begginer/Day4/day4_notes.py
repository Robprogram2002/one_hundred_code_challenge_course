# Random module
import random

# generate a random integer between rwo numbers inclusive
print(random.randint(100, 200))
# generate a random float number between 0 and 1
print(random.random())
# we can expand tje range to 0 to any number by
print(random.random() * 5)

# these are pseudo random numbers, so we must specify a seed
random.seed(64)
x = random.randint(0, 1)
if x == 1:
    print("Heads")
else:
    print("Tails")

# Lists


# Ej1: Given a list of names enter by the user select at random one to pay the meal

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

x = random.randint(0, len(names) - 1)

print(f"{names[x]} is going to buy the meal today!")

# Ej2: Mark the treasure with an x
row1 = ["⬜️", "⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️", "⬜️", "⬜️️"]
mapping = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

x = int(position[0]) - 1
y = int(position[1]) - 1

mapping[y][x] = 'X'

print(f"{row1}\n{row2}\n{row3}")
