# Conditional operators

"""
if condition :
    do this
else:
    do this
"""

# Ej1: Write a program that works out whether if a given number is an odd or even number.

number = int(input("Which number do you want to check? "))
result = ""
if number % 2 == 0:
    result = "even"
else:
    result = "odd"

# result = "even" if number % 2 == 0 else "odd" (using ternary operator)
print(f"This is an {result} number.")

# Ej2: Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight / height ** 2

result = ""
if bmi < 18.5:
    result = "are underweight"
elif bmi < 25:
    result = "have a normal weight"
elif bmi < 30:
    result = "are slightly overweight"
elif bmi < 35:
    result = "are obese"
else:
    result = "are clinically obese"

print(f"Your BMI is {round(bmi)}, you {result}")

# Ej3: Write a program that works out whether if a given year is a leap year
"""
This is how you work out whether if a particular year is a leap year.

on every year that is evenly divisible by 4 
**except** every year that is evenly divisible by 100 
**unless** the year is also evenly divisible by 400
"""

year = int(input("Which year do you want to check? "))
result = False
if year % 4 == 0:
    result = True
    if year % 100 == 0 and year % 400 != 0:
        result = False

print("Leap year" if result else "Not leap year")

# Ej4:  build an automatic pizza order program.  Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

cost = 0
if size == "L":
    if add_pepperoni == 'Y':
        cost += 3
    cost += 25
elif size == "M":
    if add_pepperoni == 'Y':
        cost += 3
    cost += 20
elif size == "S":
    if add_pepperoni == 'Y':
        cost += 2
    cost += 15

if extra_cheese == 'Y':
    cost += 1

print(f"Your final bill is: ${cost}")

# Ej5: A rollercoaster

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45 <= age <= 55:  # age >= 45 and age <= 55
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

# Ej6:  write a program that tests the compatibility between two people.
# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs.
# Then combine these numbers to make a two-digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

a = 0
b = 0
string = name1.lower() + name2.lower()
a += string.count('t')
a += string.count('r')
a += string.count('u')
a += string.count('e')

b += string.count('l')
b += string.count('o')
b += string.count('v')
b += string.count('e')

score = int(str(a) + str(b))
result = f"Your score is {score}, "
if score < 10 or score > 90:
    print(result + "you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(result + "you are alright together")
else:
    print(result)
