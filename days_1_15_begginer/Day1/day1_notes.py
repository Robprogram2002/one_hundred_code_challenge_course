# The print function

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")   # Remember that you must use single quotes inside double quotes

# Another way of doing this is using the backslash and n character
print("\n")
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")

# Concatenation
print("\n")
print("String Concatenation is done with the " "+" " sign.")
print("Hello" + " " + "Friend")

# The input function is used to ask the user to enter data in the console

# input("What is your name?:")
print("Hello" + " " + input("What is your name?:"))

# Variables
# They are used to storing information for later use
name = input("What is your name? ")
print("Your name has " + str(len(name)) + " characters")

# we can make simultaneous variable assignments, for example we can switch the values of two variables like this
a = "Hello"
b = "Bye"
b, a = a, b

print(a)
print(b)
