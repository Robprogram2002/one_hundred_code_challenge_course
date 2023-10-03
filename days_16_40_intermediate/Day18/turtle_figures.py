import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
screen = Screen()

colors = ["aquamarine", "brown", "chartreuse", "coral", "cyan", "dark goldenrod", "dark gray",
          "dark orange", "dark salmon", "dark magenta", "DarkGoldenrod", "dark violet", "DeepPink"]
random.shuffle(colors)


def draw_figure(turtle: Turtle, sides: int, length: float, direction: str):
    angle = 360 / sides
    for t in range(sides):
        turtle.forward(length)
        if direction == 'right':
            turtle.right(angle)
        else:
            turtle.left(angle)


def play(sides: int, streng: int):
    timmy.pensize(streng)
    timmy.penup()
    timmy.back(60)
    timmy.left(90)
    timmy.forward(60)
    timmy.right(90)
    timmy.pendown()

    for i in range(3, sides + 1):
        timmy.color(colors[i])
        draw_figure(timmy, i, 70, 'right')
        draw_figure(timmy, i, 70, 'left')

    timmy.penup()
    timmy.forward(35)
    timmy.right(90)
    timmy.forward(35)
    timmy.left(180)
    timmy.pendown()

    for i in range(3, sides + 1):
        timmy.color(colors[i])
        draw_figure(timmy, i, 70, 'right')
        draw_figure(timmy, i, 70, 'left')

    timmy.hideturtle()


play(6, 3)

screen.exitonclick()
