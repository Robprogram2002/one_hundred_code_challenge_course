import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.pensize(2)
timmy.speed("fastest")
screen = Screen()
screen.colormode(255)


def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        timmy.color(get_random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(6)

screen.exitonclick()
