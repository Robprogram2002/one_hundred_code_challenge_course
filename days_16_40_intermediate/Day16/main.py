import CoffeeMachine

my_coffee_machine = CoffeeMachine.CoffeeMachine()

while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "report":
        my_coffee_machine.show_report()
    elif user_choice == "off":
        print(my_coffee_machine.turn_off())
        break
    elif user_choice == "menu":
        my_coffee_machine.show_menu()
    else:
        result = my_coffee_machine.make_coffee(user_choice)

        if result is None:
            print("Please, type a valid choice")
        else:
            print(result)
