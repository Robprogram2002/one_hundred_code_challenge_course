from data import MENU, resources

# TODO: promp user to ask him what he wants
money = 0.0


def handle_choice(choice, current_money):
    if choice == "report":
        for item in resources:
            print(f"{item} : {resources[item]}")
        print(f"Money: ${current_money}")
    elif choice == "off":
        return "off"

    for coffee_type in MENU:
        if user_choice == coffee_type:
            for ingredient in MENU[user_choice]["ingredients"]:
                if resources[ingredient] < MENU[user_choice]["ingredients"][ingredient]:
                    return f"Sorry there is no enough {ingredient}"

            print("Please insert coins")
            quarters = float(input("how many quarters? : "))
            dimes = float(input("how many dimes? : "))
            nickles = float(input("how many nickles? : "))
            pennies = float(input("how many pennies? : "))

            total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            cost = MENU[user_choice]["cost"]
            if total >= cost:
                money_change = round(total - cost, 2)
                print(f"Here is ${money_change} in change.")
                print(f"Here is your {user_choice} Enjoy!!")

                for ingredient in MENU[user_choice]["ingredients"]:
                    resources[ingredient] -= MENU[user_choice]["ingredients"][ingredient]

                return "pass"
            else:
                money_difference = round(cost - total, 2)
                return f"You don't have enough money. You put ${total} and the cost is ${cost} "


while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    result = handle_choice(user_choice, money)

    if result == "pass":
        money += MENU[user_choice]["cost"]
    elif result == "off":
        break
    elif result is None and user_choice != "report":
        print("Please, type a valid choice")
    elif result is not None:
        print(result)
