import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password(nr_letters=6, nr_numbers=3, nr_symbols=3):
    password = []
    for i in range(nr_letters):
        x = random.randint(0, len(letters) - 1)
        password.append(letters[x])
    for j in range(nr_symbols):
        x = random.randint(0, len(symbols) - 1)
        password.append(symbols[x])
    for k in range(nr_numbers):
        x = random.randint(0, len(numbers) - 1)
        password.append(numbers[x])
    random.shuffle(password)
    return "".join(password)
