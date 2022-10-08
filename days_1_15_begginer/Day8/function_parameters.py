import math


# Functions with parameters

# parameter is the name (or variable) that we assign in our function header
# argument is the actual value that is pass to the function by the program

# Simple Function
def greet():
    print("Hello Angela")
    print("How do you do Jack Bauer?")
    print("Isn't the weather nice today?")


greet()


# Function that allows for input
# 'name' is the parameter.
# 'Jack Bauer' is the argument.
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")


# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


# Calling greet_with() with Positional Arguments
greet_with("Jack Bauer", "Nowhere")
# vs.
greet_with("Nowhere", "Jack Bauer")

# Calling greet_with() with Keyword Arguments
greet_with(location="London", name="Angela")


# Ej1: You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of
# wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

def paint_calc(height, width, cover):
    area = height * width
    answer = math.ceil(area / cover)
    print(f"You'll need {answer} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# Ej2: Prime numbers are numbers that can only be cleanly divided by themselves and 1. You need to write a function
# that checks whether if the number passed into it is a prime number or not.


def prime_checker(number):
    result = True
    for n in range(2, number):
        if number % n == 0:
            result = False
            break
    if result:
        print("It's a prime number.")
    else:
        print("It's not a prime number")


n = int(input("Check this number: "))
prime_checker(number=n)


