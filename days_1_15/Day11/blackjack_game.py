import random

############### Blackjack Project #####################

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


init_phrase = "Do you want to play another game of Blackjack? Type 'y' or 'n': "
step_phrase = "Type 'y' to get another card, type 'n' to pass: "


def get_random_cart(n: int):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if n == 1:
        return random.choices(cards)[0]
    else:
        return random.choices(cards, k=n)


def count_hand(hand: [int]):
    count = 0
    is_ass = None
    for n in range(len(hand)):
        if hand[n] == 11:
            is_ass = n
            continue
        count += hand[n]
    if is_ass:
        if count + 11 <= 21:
            count += 11
        else:
            hand[is_ass] = 1
            count += 1
    return count


def user_game(user, computer):
    def user_status():
        print(f"Your cards: {user} \t Current score: {user_count}")

    user_count = count_hand(user)
    user_status()

    print(f"Computer's first card: {computer[0]}")

    while user_count < 21:
        other = input(step_phrase)
        if other == 'y':
            user.append(get_random_cart(1))
            user_count = count_hand(user)
            if user_count < 21:
                user_status()
        else:
            break
    return user_count


def computer_game(computer):
    computer_count = count_hand(computer)
    x = random.randint(0, 1)
    while x == 1 and computer_count < 21:
        computer.append(get_random_cart(1))
        computer_count = count_hand(computer)
    return computer_count


def game():
    print(logo)
    user = get_random_cart(2)
    computer = get_random_cart(2)

    user_count = user_game(user, computer)

    if user_count > 21:
        print(f"Your final hand: {user} \t Final score: {user_count}")
        print(f"Computer's final hand: {computer} \t Final score: {count_hand(computer)}")

        print("You lose !!")

        start = input(init_phrase)
        if start == 'y':
            game()
        else:
            return

    computer_count = computer_game(computer)

    print(f"Your final hand: {user} \t Final score: {user_count}")
    print(f"Computer's final hand: {computer} \t Final score: {computer_count}")

    if user_count == 21 or user_count > computer_count or computer_count > 21:
        print("You win !!")
    else:
        print("You lose !!")

    start = input(init_phrase)
    if start == 'y':
        game()

game()
