import random
import art
import data

question = "Who has more followers on Instagram? Type 'A' or 'B': "


def get_person(skip: [int]):
    x = random.randint(0, len(data.data) - 1)
    while x in skip:
        x = random.randint(0, len(data.data) - 1)

    return [x, data.data[x]]


def print_info(person, label):
    print(f"Compare {label}: {person['name']}, {person['description']}, from {person['country']}")


def check_answer(numA, numB, user_answer):
    if (numA > numB and user_answer == 'A') or (numB > numA and user_answer == 'B'):
        return True
    else:
        return False


def game(previous, score, skip_list):
    print(skip_list)
    if previous:
        a = previous
    else:
        a = get_person(skip_list)
    b = get_person(skip_list)

    check = False
    while not check:
        if b[0] == a[0]:
            b = get_person(skip_list)
        else:
            check = True

    print(art.logo)
    print_info(a[1], 'A')
    print(art.vs)
    print_info(b[1], 'B')

    answer = input(question)
    is_correct = check_answer(a[1]['follower_count'], b[1]['follower_count'], answer)

    if is_correct:
        score += 1
        print(f"You're right! \t Current score {score}")
        if answer == 'A':
            skip_list.append(b[0])
            game(a, score, skip_list)
        else:
            skip_list.append(a[0])
            game(b, score, skip_list)
    else:
        print(f"Sorry that's wrong. Final score: {score}")

        re_start = input("Do you want to play again? Type 'y' or 'n': ")
        if re_start == 'y':
            game(None, 0, [])
        else:
            print("Good Bye !!")


game(None, 0, [])
