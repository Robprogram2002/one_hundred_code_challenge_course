from typing import Optional

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def make_calculation(num1, num2, operation):
    result = 0
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    else:
        result = num1 / num2
    return result


def calc_resp(a: float):
    op = input("Pick an operation: ")
    b = float(input("What's the next number?: "))
    res = make_calculation(a, b, op)
    print(f"{a} {op} {b} = {res}")
    return res


def calculator(initial: Optional[float]):
    operations = ["+", "-", "*", "/"]
    if initial:
        a = initial
    else:
        print(logo)
        a = float(input("What's the first number?: "))
        for c in operations:
            print(c)
    res = calc_resp(a)
    restart = input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation or type 'e' "
                    f"to exit: ")
    if restart == 'y':
        calculator(res)
    elif restart == 'n':
        calculator(None)
    else:
        print('Good Bye!!')


calculator(None)
