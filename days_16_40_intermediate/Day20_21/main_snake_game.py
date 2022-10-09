from turtle import Screen
import time
from snake_class import Snake
from food_class import Food
from scordboard_class import ScoredBoard

game_over = False
screen = Screen()
snake = Snake()
food = Food()
scored_board = ScoredBoard()

# setup screen game
screen.setup(width=600, height=600)
screen.title("The Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# setup key events listeners
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")


while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scored_board.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over = True
        scored_board.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over = True
            scored_board.game_over()

screen.exitonclick()
