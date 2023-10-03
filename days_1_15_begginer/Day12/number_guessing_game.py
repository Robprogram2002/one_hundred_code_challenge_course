import random

welcome = "Welcome to the Number Guessing Game!"
start = "I'm thinking of a number between 1 and 100."

question = "Choose a difficulty. Type 'easy' or 'hard': "
levels = {
    "easy": 10,
    "hard": 5
}


def status(attempts):
    print(f"You have {attempts} attempts remaining to guess the number")


def error_mess(text, tries):
    print(text)
    if tries - 1 > 0:
        print("Guess again")


def game():
    print(welcome)
    print(start)
    target = random.randint(1, 100)
    l = input(question)
    tries = levels[l]

    correct = False
    while tries > 0 and not correct:
        status(tries)
        guess = int(input("Make a guess: "))
        if guess == target:
            correct = True
            continue
        elif guess < target:
            error_mess("Too low", tries)
        else:
            error_mess("Too high", tries)

        tries -= 1

    if correct:
        print(f"You got it !! The answer was {target}")
    else:
        print(f"You lose !! The answer was {target}")

    again = input("Do you want to play again ? Type 'y' or 'n'. ")
    if again == 'y':
        game()
    else:
        print("Good Bye!!")


game()
