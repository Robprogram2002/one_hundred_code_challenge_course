from turtle import Turtle, Screen
import random
import colorgram

COLORS = {
    0: "red",
    1: "blue",
    2: "purple",
    3: "green",
    4: "pink",
    5: "orange",
    6: "black",
    7: "brown"
}

DIRECTIONS = ["right", "left", "forward", "backward"]
COLORS2 = ["red","blue", "orange", "purple", "black", "brown", "green"]

tim = Turtle()
tim.pensize(2)
tim.speed("fastest")

rgb_colors = []

if len(rgb_colors) == 0:
    colors = colorgram.extract("color_image.jpg", 30)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb_color = (r, g, b)
        rgb_colors.append(rgb_color)

def random_color():
    random_r = random.random()
    random_b = random.random()
    random_g = random.random()
    new_color = (random_r, random_g, random_b)
    return new_color


def draw_shapes(side_num, index_color):
    angle = 360 / side_num
    # tim.color(COLORS[index_color])
    tim.color(random_color())
    for _ in range(side_num):
        tim.forward(50)
        tim.right(angle)


# for index, shape_side_n in enumerate(range(3, 10)):
#    draw_shapes(shape_side_n, index)


def draw_walk(distance):
    random_direction = random.choice(DIRECTIONS)
    tim.color(random.choice(COLORS2))

    if random_direction == "right":
        tim.right(90)
    elif random_direction == "left":
        tim.left(90)
    elif random_direction == "backward":
        tim.left(180)

    tim.forward(distance)


# step_distance = 3
# for i in range(1, 361, step_distance):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.left(step_distance)


screen = Screen()
screen.exitonclick()
