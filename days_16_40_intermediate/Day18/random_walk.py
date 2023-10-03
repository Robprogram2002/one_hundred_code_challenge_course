import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.hideturtle()
timmy.pensize(12)
timmy.speed("fast")

screen = Screen()
screen.colormode(255)


# colors = ["red", "blue", "purple", "green",
#           "pink", "orange", "black", "brown"]


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


directions = [0, 90, 180, 270]

count = 0
while count < 100:
    # timmy.color(random.choice(colors))
    timmy.pencolor(get_random_color())
    timmy.forward(30)
    timmy.right(random.choice(directions))
    count += 1

screen.exitonclick()
