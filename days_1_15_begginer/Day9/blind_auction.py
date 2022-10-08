logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def add_user(participants):
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))
    participants[name] = bid


print(logo)
print("Welcome to the secret auction program.")


def game():
    other = "yes"
    users = {}

    while other != "no":
        add_user(users)
        other = input("Are there any other bidders? Type 'yes' or 'no'. ")
    winner = ""
    max_val = 0

    for k in users.keys():

        if users[k] > max_val:
            winner = k
            max_val = users[k]

    print(f"The winner is {winner} with a bid of ${max_val}")


should_end = False
while not should_end:
    game()
    respond = input("Do you want to make another auction? Type 'yes' or 'no' . ")
    if respond == 'no':
        should_end = True
        print("Good Bye!!")
