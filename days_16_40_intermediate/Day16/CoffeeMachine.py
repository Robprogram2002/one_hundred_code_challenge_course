class CoffeeMachine:
    def __init__(self):
        self.menu = {
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "coffee": 18,
                },
                "cost": 1.5,
            },
            "latte": {
                "ingredients": {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
                "cost": 2.5,
            },
            "cappuccino": {
                "ingredients": {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
                "cost": 3.0,
            }
        },
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            },
        self.money = 0.0

    def show_report(self):
        for item in self.resources[0]:
            print(f"{item} : {self.resources[0][item]}")
        print(f"Money: ${self.money}")

    def show_menu(self):
        for coffee in self.menu[0]:
            print(f"{coffee} : ${self.menu[0][coffee]['cost']}")

    @staticmethod
    def turn_off():
        return "off"

    @staticmethod
    def process_input_coins():
        print("Please insert coins")
        quarters = float(input("how many quarters? : "))
        dimes = float(input("how many dimes? : "))
        nickles = float(input("how many nickles? : "))
        pennies = float(input("how many pennies? : "))

        total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        return total

    def make_coffee(self, user_choice):
        for coffee_type in self.menu[0]:
            if user_choice == coffee_type:
                for ingredient in self.menu[0][user_choice]["ingredients"]:
                    if self.resources[0][ingredient] < self.menu[0][user_choice]["ingredients"][ingredient]:
                        return f"Sorry there is no enough {ingredient}"

                cost = self.menu[0][user_choice]["cost"]
                total = self.process_input_coins()

                if total >= cost:
                    money_change = round(total - cost, 2)

                    for ingredient in self.menu[0][user_choice]["ingredients"]:
                        self.resources[0][ingredient] -= self.menu[0][user_choice]["ingredients"][ingredient]

                    self.money += cost
                    return f"Here is ${money_change} in change.\nHere is your {user_choice} Enjoy!!"
                else:
                    return f"You don't have enough money. You put ${total} and the cost is ${cost} "
