# Data types

# String : They are formed by putting characters together enclosed by " or '
word = "Hello"

# we can subscribe characters from a string
print(word[1])

# Integer
n = 123
print(n + 100)

# Float
pi = 3.14159
print(pi * 2)
# Note: division always return a float type
print(6 / 3)
# If we want the integer part, we can use float division
print(8 // 3)

# Boolean
boo = False
print(boo)

# Type conversion / casting

# The type function tell us what data type is store in a variable
print(type(boo))

# we can use the built-in functions: str, int, float to convert a variable from one data type to another

# Ej1: Write a program that adds the digits in a two-digit number

two_digit_number = input("Type a two digit number: ")
a, b = two_digit_number
print(int(a) + int(b))

# Ej2: Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
print(round(weight / height ** 2, 1))

# Ej3 : Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live
# until 90 years old. It will take your current age as the input

age = int(input("What is your current age?"))

expected_days = 90 * 365
expected_weeks = 90 * 52
expected_months = 90 * 12

current_days = age * 365
current_weeks = age * 52
current_months = age * 12

days_left = expected_days - current_days
weeks_left = expected_weeks - current_weeks
months_left = expected_months - current_months

# result = "You have {} days, {} weeks, and {} months left".format(days_left, weeks_left, months_left)
result = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left"  # f-strings
print(result)
