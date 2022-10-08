################### Scope ####################

enemies = 1  # global scope


def increase_enemies():
    enemies = 2  # local scope
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# print(potion_strength)  # the variable doesn't exist in the scope of the function

# Global Scope
player_health = 10


def game():
    def drink_potion():  # local scope function
        potion_strength = 2
        print(player_health)

    drink_potion()


print(player_health)

# There is no Block Scope

game_level = 3


def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Modifying Global Scope

enemies = 1


def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants

PI = 3.14159
URL = "https://www.google.com"

# Note: Remember that conditional statements and loops statements don't create local scope , but functions does.

