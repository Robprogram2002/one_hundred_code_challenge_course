import random
import arts
import words

stages = arts.stages
x = random.randint(0, len(words.word_list) - 1)
target = list(words.word_list[x].lower())
string = ['_'] * len(target)
hearts = 6
correct_letters = 0

print(arts.logo)
print(f"The word you must guess has {len(target)} letters, you have {hearts} hearts")


def update_target(char: str, score: int):
    new_score = score
    for i in range(len(target)):
        if target[i] == char:
            string[i], target[i] = target[i], None
            new_score += 1
    return new_score


def fail_input():
    print("Please type a single character")


def print_status():
    print(" ".join(string) + "\t\t" + stages[hearts])


while hearts > 0 and correct_letters != len(target):
    print_status()
    user_char = input("Guess a letter: ").lower()

    if user_char == "" or len(user_char) > 1:
        fail_input()
        continue

    if user_char in target:
        correct_letters = update_target(user_char, correct_letters)
    else:
        hearts -= 1
        print(f"You guessed {user_char}, that's not in the word. You lose a heart.")

if hearts == 0:
    print(stages[hearts])
    print(f"You lose !! The word was : {words.word_list[x]}")
elif correct_letters == len(target):
    print("You win!")
    print_status()
