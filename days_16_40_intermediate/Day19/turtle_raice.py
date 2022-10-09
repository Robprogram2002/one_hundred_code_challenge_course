from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "green", "yellow", "purple", "brown", "black", "pink"]
Y_POSITIONS = [-100, -70, -40, -10, 20, 50, 80, 110]

screen = Screen()
screen.setup(width=500, height=400)
user_pet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color : ")
turtle_players = []
game_over = True

for index, turtle_color in enumerate(COLORS):
    tim = Turtle()
    tim.shape("turtle")
    tim.penup()
    tim.color(COLORS[index])
    tim.goto(-230, Y_POSITIONS[index])
    turtle_players.append(tim)

if user_pet:
    game_over = False

while not game_over:

    for turtle in turtle_players:

        if turtle.xcor() > 230:
            game_over = True
            winning_turtle_color = turtle.pencolor()

            if winning_turtle_color == user_pet:
                print(f"You have won! The turtle with color {winning_turtle_color} is the winner")
            else:
                print(f"You have lost! The turtle with color {winning_turtle_color} is the winner")

        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
