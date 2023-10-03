# For loops
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

# The range function
for number in range(1, 31, 3):
    print(number)

# Ej1: write a program that calculates the average student height from a List of heights.
student_heights = input("Input a list of student heights ").split()
count = 0

for n in range(0, len(student_heights)):
    count += int(student_heights[n])

print(round(count / len(student_heights)))

# Ej2: write a program that calculates the highest score from a List of scores.
student_scores = input("Input a list of student scores ").split()
max_score = int(student_scores[0])
for n in range(1, len(student_scores)):
    score = int(student_scores[n])
    if score > max_score:
        max_score = score
print(f"The highest score in the class is: {max_score}")

# Ej3: write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would
# be 2 and the last one is 100

sum_res = 0
for n in range(1, 101):
    if n % 2 == 0:
        sum_res += n
print(sum_res)

# Ej4:  write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
