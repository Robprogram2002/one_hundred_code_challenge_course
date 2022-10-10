import random
import pandas

# For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# List Comprehension
new_list = [n + 1 for n in numbers]

# String as List
name = "Angela"
letters_list = [letter for letter in name]

# Range as List
range_list = [n * 2 for n in range(1, 5)]

# Conditional List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

upper_case_names = [name.upper() for name in names if len(name) > 4]

# Dictionary Comprehension

student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)

# Ej1:  write a List Comprehension to create a new list containing every number squared.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]
print(squared_numbers)

# Ej2: write a List Comprehension to create a new list called result. This new list should only contain the even numbers
# from the list numbers.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers if n % 2 == 0]

print(result)

# Ej3: create a list called result which contains the numbers that are common in both files file1.txt and file2.txt .
with open("file1.txt") as file:
    list_A = file.readlines()

with open("file2.txt") as file:
    list_B = file.readlines()

result = [int(n.strip()) for n in list_A if n in list_B]

print(result)

# Ej4: use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence
# and calculates the number of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split(" ")}

print(result)

# Ej5: use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees
# Celsius and converts it into degrees Fahrenheit.

# (temp_c * 9/5) + 32 = temp_f

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key: val * 9 / 5 + 32 for (key, val) in weather_c.items()}

print(weather_f)

# How to iterate over the rows of a pandas DF

students = {
    "Student": ["Angela", "James", "Lili"],
    "Score": [65, 72, 94]
}

student_df = pandas.DataFrame(students)
print(student_df)

print("\n")
for (index, row) in student_df.iterrows():
    print(f"{index}. {row.Student}: {row.Score}")
