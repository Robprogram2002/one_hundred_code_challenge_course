# Tip group calculator

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? ")) / 100
people = int(input("How many people to split the bill? "))
tip = bill + percentage * bill
total = "{:.2f}".format(tip / people)
print(f"Each person should pay: ${total}")
