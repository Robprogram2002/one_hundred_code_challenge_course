import random

words = ["Monday", "Party", "Canada", "Physics"]

x = random.randint(0, len(words) - 1)
target = list(words[x].lower())
string = ['_'] * len(target)
hearts = 5
correct_letters = 0

print(f"The word you must guess has {len(target)} letters, you have 5 hearts")
while hearts > 0 and correct_letters != len(target):
    print(" ".join(string) + "\t\t" + f"Hearts: {hearts}")
    user_char = input("Guess a letter: ").lower()
    if user_char == "":
        print("Please type a single character")
        continue
    if len(user_char) > 1:
        print("Please type a single character")
        continue

    if user_char in target:
        for i in range(len(target)):
            if target[i] == user_char:
                string[i], target[i] = target[i], None
                break
        correct_letters += 1
    else:
        hearts -= 1
        print(f"You guessed {user_char}, that's not in the word. You lose a heart.")

if hearts == 0:
    print("You lose !")
elif correct_letters == len(target):
    print("You win!")
