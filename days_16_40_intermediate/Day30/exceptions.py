# catching exceptions
try:
    # something that may cause an exception
    file = open("a_file.txt")
    dict = {"key": "val"}
    print(dict["akldsad"])
except FileNotFoundError:  # we want to specify the type of error our code may generate
    # Do this if there was an exception
    print("The file doesn't exist. Let's created")
    file = open("a_file.txt", mode="w")
    file.write("First line")
except KeyError as error_message:
    print(f"There is no key with the name {error_message}")
else:
    # Do this if there were not  an exception
    lines = file.readlines()
    for s in lines:
        print(s)
finally:
    # Do this no matter what happens
    file.close()
    print("File was closed")

# raising exceptions
height = float(input("What's your height: "))
weight = float(input("What's your weight: "))

if height > 3:
    raise ValueError("Human height should not be greater than 3 meters.")

fruits = ["Apple", "Pear", "Orange"]


# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        # print(f"List index out of range: {index}")
        print("Fruit Pie")
    else:
        print(fruit + " pie")


make_pie(4)

#  TODO: prevent the program from crashing.

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        post_likes = post["Likes"]
    except KeyError:
        post_likes = 0
    finally:
        total_likes = total_likes + post_likes

print(total_likes)
