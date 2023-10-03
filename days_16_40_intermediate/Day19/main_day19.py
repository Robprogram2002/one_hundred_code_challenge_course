from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def turn_counter_clockwise():
    tim.left(10)


def turn_clockwise():
    tim.right(10)


def clean_draw():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# start listen
screen.listen()

screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_counter_clockwise, key="a")
screen.onkey(fun=turn_clockwise, key="d")
screen.onkey(fun=clean_draw, key="c")

screen.exitonclick()
