from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")


def draw_square(turtle: Turtle):
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_eq_triangle(turtle: Turtle):
    turtle.forward(100)
    turtle.left(135)
    turtle.forward(50 * (2 ** (1 / 2)))
    turtle.left(90)
    turtle.forward(50 * (2 ** (1 / 2)))
    turtle.left(135)


def draw_dash_line(turtle: Turtle, dashes: int, length: float):
    for i in range(dashes):
        turtle.forward(length)
        turtle.penup()
        turtle.forward(length)
        turtle.pendown()


screen = Screen()
draw_eq_triangle(timmy)
timmy.color("red")
draw_square(timmy)
timmy.left(180)
draw_dash_line(timmy, 15, 8)

screen.exitonclick()
